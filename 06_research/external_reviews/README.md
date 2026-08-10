# External Reviews / Originals

Os materiais externos e protótipos recebidos nesta rodada foram preservados **byte a byte** em:

`ORIGINALS_2026-08-10.zip.base64`

## Integridade

- formato lógico: ZIP
- transporte no GitHub: Base64 UTF-8
- SHA-256 do ZIP reconstruído: `01120172a2d7692e93fc932a3bc3c8c5f88277884af3615d2381c358eb25b2a0`
- arquivos preservados: 10

## Arquivos
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

## Como reconstruir

```bash
base64 -d ORIGINALS_2026-08-10.zip.base64 > ORIGINALS_2026-08-10.zip
sha256sum ORIGINALS_2026-08-10.zip
unzip ORIGINALS_2026-08-10.zip
```

## Regra epistemológica

Esses arquivos são **proveniência histórica**:
- auditorias/dossiês = fontes de crítica e hipótese;
- `.ts` = protótipos/spec drafts, não patches prontos;
- números hardcoded não viram evidência por parecerem quantitativos;
- testes tautológicos não provam integração real.

O `05_decisions/DECISION_LEDGER.md` e o pré-cânone reconciliado vencem propostas antigas enquanto não houver nova revisão explícita.
