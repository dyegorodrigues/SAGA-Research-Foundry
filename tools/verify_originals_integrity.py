from pathlib import Path
import base64
import binascii
import hashlib
import io
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REVIEWS = ROOT / "06_research" / "external_reviews"
MANIFEST_PATH = REVIEWS / "ORIGINALS_MANIFEST.sha256.json"

manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
errors: list[str] = []
chunks: list[str] = []

for filename, expected_hash in manifest["parts"].items():
    path = REVIEWS / filename
    if not path.exists():
        errors.append(f"MISSING {filename}")
        continue

    raw = path.read_bytes()
    actual_hash = hashlib.sha256(raw).hexdigest()
    if actual_hash != expected_hash:
        errors.append(f"HASH {filename}: {actual_hash} != {expected_hash}")

    try:
        chunks.append(raw.decode("ascii").strip())
    except UnicodeDecodeError:
        errors.append(f"ASCII {filename}: conteúdo não é ASCII/Base64")

stream = "".join(chunks)
if len(chunks) == len(manifest["parts"]):
    if len(stream) % 4 != 0:
        errors.append(f"BASE64_LENGTH {len(stream)}: não é múltiplo de 4")

    archive_bytes = None
    try:
        archive_bytes = base64.b64decode(stream, validate=True)
    except (binascii.Error, ValueError) as exc:
        errors.append(f"BASE64_DECODE: {exc}")

    if archive_bytes is not None:
        archive_hash = hashlib.sha256(archive_bytes).hexdigest()
        if archive_hash != manifest["archive_sha256"]:
            errors.append(
                f"ZIP_HASH {archive_hash} != {manifest['archive_sha256']}"
            )

        try:
            with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
                bad_crc = archive.testzip()
                if bad_crc:
                    errors.append(f"ZIP_CRC {bad_crc}: CRC inválido")

                actual_files = sorted(
                    name for name in archive.namelist() if not name.endswith("/")
                )
                expected_files = sorted(manifest["expected_files"])
                if actual_files != expected_files:
                    missing = sorted(set(expected_files) - set(actual_files))
                    extra = sorted(set(actual_files) - set(expected_files))
                    if missing:
                        errors.append(f"ZIP_MISSING {', '.join(missing)}")
                    if extra:
                        errors.append(f"ZIP_EXTRA {', '.join(extra)}")
        except zipfile.BadZipFile as exc:
            errors.append(f"ZIP_INVALID: {exc}")

if errors:
    print("ORIGINALS INTEGRITY: FAIL")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("ORIGINALS INTEGRITY: OK")
print(f"- parts: {len(manifest['parts'])}")
print(f"- archive_sha256: {manifest['archive_sha256']}")
print(f"- expected_files: {len(manifest['expected_files'])}")
