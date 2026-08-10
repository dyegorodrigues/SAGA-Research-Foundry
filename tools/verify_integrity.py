from pathlib import Path
import hashlib, json, sys

root = Path(__file__).resolve().parents[1]
manifest_path = root / "MANIFEST.sha256.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

errors = []
for rel, expected in manifest["files"].items():
    p = root / rel
    if not p.exists():
        errors.append(f"MISSING {rel}")
        continue
    actual = hashlib.sha256(p.read_bytes()).hexdigest()
    if actual != expected:
        errors.append(f"HASH {rel}: {actual} != {expected}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"OK: {len(manifest['files'])} files verified")
