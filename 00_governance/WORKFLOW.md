# Workflow

## Fluxo A — produção
Ocorre no `dyegorodrigues/SAGA` e tem um único writer ativo por branch.

## Fluxo B — P&D
Ocorre nesta Foundry.

Ciclo:

pesquisar → propor → red-team → registrar → decidir → experimentar → revisar → promover

## Promoção para produção
Nunca automática.

Uma ideia só pode ser promovida quando houver:
- problema claro;
- decisão no Ledger;
- Invariant Impact Review;
- plano mínimo;
- reuse audit real;
- gates;
- rollback/feature flag quando aplicável;
- autorização explícita do usuário.

## Sincronização
A Foundry não tenta espelhar o SAGA inteiro.
Ela armazena links, snapshots e decisões.
