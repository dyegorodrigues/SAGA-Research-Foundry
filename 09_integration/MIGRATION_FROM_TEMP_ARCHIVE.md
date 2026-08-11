# Migração da branch temporária

Fonte temporária histórica:
- repo: `dyegorodrigues/SAGA`
- branch: `archive/thinking-engine-rd-2026-08-10`
- pasta: `AI_Studio_Lab/research/thinking_engine_archive_2026-08-10/`

## Estado da migração

A migração estrutural para a Foundry foi **concluída** em 2026-08-10. A atestação de integridade byte-a-byte do pacote histórico foi **REABERTA em 2026-08-11** depois de a auditoria executar `tools/verify_integrity.py` e registrar divergência nas partes `part05` e `part08`.

1. [x] Criar `dyegorodrigues/SAGA-Research-Foundry`.
2. [x] Publicar a estrutura.
3. [x] Copiar/organizar fontes históricas da branch temporária.
4. [x] Comparar Decision Ledger e documentos reconciliados.
5. [ ] **Verificar hashes/manifesto do archive transport — REABERTO em 11/08.**
6. [x] Fazer segunda revisão de navegação e links.
7. [x] Fazer mega revisão de detalhe e corrigir compactação documental via `RECONCILED_DETAIL_REGISTER_V0_98.md`.
8. [x] Reancorar PR/HEAD/CI do SAGA no snapshot de 10/08.
9. [x] Confirmar ausência final da branch temporária em duas buscas (`archive/thinking-engine-rd-2026-08-10` e `thinking-engine`).

## Proveniência e recuperação

O transporte histórico continua presente em 8 partes Base64 em `06_research/external_reviews/`, mas **não deve ser descrito como verificado enquanto o verificador falhar**.

Em 11/08 foram localizados individualmente, na File Library de origem, os 10 materiais externos listados no README da pasta, inclusive os dois protótipos que não eram recuperáveis pelo stream danificado segundo a auditoria. O estado detalhado está em:

- `06_research/external_reviews/RECOVERY_STATUS_2026-08-11.md`.

Isso elimina a hipótese de perda intelectual irreversível conhecida, mas **não restaura automaticamente o SHA lógico histórico do ZIP**.

## Regra permanente

A Foundry é a memória persistente de P&D; o SAGA produtivo é a fonte da verdade operacional. Migração concluída não promove automaticamente nenhuma proposta para runtime. Protótipos recuperados permanecem proveniência histórica até validação explícita.
