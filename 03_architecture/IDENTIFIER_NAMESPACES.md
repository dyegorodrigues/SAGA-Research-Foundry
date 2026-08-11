# Identifier Namespaces

**Status:** contrato de leitura da Foundry · 11/08/2026

## Problema

Materiais históricos externos e o Decision Ledger da Foundry usam identificadores curtos como `D017`. Esses números nasceram em documentos diferentes e **não formam um namespace global**. Comparar apenas o sufixo numérico pode fazer duas decisões distintas parecerem a mesma decisão.

## Regra a partir de agora

Ao citar identificadores fora do documento em que nasceram, use namespace explícito:

- `FD-Dxxx` — decisão da **F**oun**d**ry em `05_decisions/DECISION_LEDGER.md`;
- `EXT:<arquivo>:Dxxx` — decisão/âncora preservada em material externo/histórico;
- `SAGA:<id>` — competência/entidade cujo identificador pertence ao produto, por exemplo `SAGA:N2.01` ou `SAGA:GM.05`.

Os documentos antigos **não precisam ser reescritos**: dentro do próprio Decision Ledger, `D017` continua legível como `FD-D017`; dentro de um original preservado, `D017` continua sendo o identificador daquele original.

## Proibição

Nunca afirmar que `FD-D017 == EXT:<arquivo>:D017` apenas porque o número coincide. Equivalência semântica exige comparação de conteúdo e deve ser registrada como mapeamento explícito.

## Exemplos

- correto: `FD-D046` mantém “Implementar Thinking agora” como REJECT;
- correto: `EXT:DOSSIE_COMPLETO_THINKING_ENGINE_SAGA_2026-08-10.md:D017`;
- incorreto: “D017 foi confirmado pela Foundry” sem dizer qual namespace.

## Migração futura

Se algum identificador precisar virar contrato consumido por máquina, o prefixo namespaced é obrigatório no schema. O número curto é apenas compatibilidade documental humana.
