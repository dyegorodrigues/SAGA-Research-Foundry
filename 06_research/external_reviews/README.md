# External Reviews / Originals

> **STATUS EM 11/08/2026: TRANSPORTE DO ARCHIVE NÃO VERIFICADO.**
> As 8 partes Base64 continuam preservadas como proveniência histórica, mas `part05` e `part08` não batem os hashes esperados e o ZIP reconstruído não pode ser tratado como preservação byte a byte válida. Os 10 arquivos-fonte listados abaixo foram localizados individualmente fora desse transporte; isso preserva o conteúdo intelectual conhecido, mas não reconstitui automaticamente o ZIP histórico.

Os materiais externos e protótipos desta rodada foram originalmente empacotados como um ZIP dividido em 8 partes Base64:

- `ORIGINALS_2026-08-10.zip.base64.part01`
- `ORIGINALS_2026-08-10.zip.base64.part02`
- `ORIGINALS_2026-08-10.zip.base64.part03`
- `ORIGINALS_2026-08-10.zip.base64.part04`
- `ORIGINALS_2026-08-10.zip.base64.part05`
- `ORIGINALS_2026-08-10.zip.base64.part06`
- `ORIGINALS_2026-08-10.zip.base64.part07`
- `ORIGINALS_2026-08-10.zip.base64.part08`

## Integridade

Referência histórica pretendida:

- formato lógico: ZIP;
- transporte no GitHub: Base64 UTF-8 dividido em partes;
- SHA-256 esperado do ZIP reconstruído: `01120172a2d7692e93fc932a3bc3c8c5f88277884af3615d2381c358eb25b2a0`;
- membros esperados: 10.

Estado comprovado em 11/08:

- `part05` e `part08`: divergentes dos hashes de referência;
- archive transport: **UNVERIFIED**;
- `originals_archive_verified`: **false** em `CURRENT_STATE.yaml`;
- 10/10 arquivos-fonte: localizados individualmente na File Library de origem;
- perda intelectual irreversível conhecida: **não**;
- recuperação byte-a-byte do transporte: **ainda aberta** no Issue #1.

Mecanismo dedicado:

- `ORIGINALS_MANIFEST.sha256.json` — hashes esperados das 8 partes, SHA do ZIP e membros esperados;
- `tools/verify_originals_integrity.py` — valida partes, Base64, ZIP, CRC e membros;
- `.github/workflows/integrity.yml` — mecanismo versionado para automatizar essa verificação;
- `RECOVERY_STATUS_2026-08-11.md` — estado e limites da recuperação.

**Importante:** o workflow está versionado, mas commits feitos pelo conector em 11/08 não produziram um run remoto observável pelo mecanismo de consulta usado na reconciliação. Portanto não descrever a automação como “CI comprovado” até existir uma execução observável. Isso não invalida a divergência já apurada pela execução do verificador histórico na auditoria de 11/08.

## Arquivos esperados / recuperados individualmente

- `AUDITORIA_ADVERSARIAL_THINKING_ENGINE_PRE_CANONE_v09.md`
- `CP_TEMPLATE_THINKING.md`
- `CP_TEMPLATE_THINKING_REPO (1).md`
- `DOSSE_SAGA_THINKING_ENGINE_INTEGRADO.md`
- `DOSSIE_COMPLETO_THINKING_ENGINE_SAGA_2026-08-10.md`
- `SAGA_THINKING_ENGINE_PLANO_EXPANSAO_v096.md`
- `SAGA_THINKING_v096_VALIDADO_REPO (1).md`
- `audit-thinking-reuse (1).ts`
- `thinking-extensions (1).ts`
- `thinking-integration.test (1).ts`

## Como testar o transporte histórico

```bash
python3 tools/verify_originals_integrity.py
```

O procedimento manual de reconstrução continua útil para investigação, **não como prova automática de que o conteúdo atual é válido**:

```bash
cat ORIGINALS_2026-08-10.zip.base64.part* > ORIGINALS_2026-08-10.zip.base64
base64 -d ORIGINALS_2026-08-10.zip.base64 > ORIGINALS_2026-08-10.zip
sha256sum ORIGINALS_2026-08-10.zip
unzip ORIGINALS_2026-08-10.zip
```

## Regra epistemológica

Esses arquivos são **proveniência histórica**:

- auditorias/dossiês = fontes de crítica e hipótese;
- `.ts` = protótipos/spec drafts, não patches prontos;
- números hardcoded não viram evidência por parecerem quantitativos;
- testes tautológicos não provam integração real;
- conteúdo recuperado individualmente não equivale, por si só, a transporte ZIP byte a byte restaurado.

O `05_decisions/DECISION_LEDGER.md` e o pré-cânone reconciliado vencem propostas antigas enquanto não houver nova revisão explícita.