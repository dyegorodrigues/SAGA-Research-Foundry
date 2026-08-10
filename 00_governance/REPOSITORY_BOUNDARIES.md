# Repository Boundaries

## `dyegorodrigues/SAGA`
Produto e runtime.

Responde:
> O que existe, funciona e está validado agora?

Nunca é alterado automaticamente por decisões desta Foundry.

## `dyegorodrigues/SAGA-Research-Foundry`
Memória persistente de P&D.

Responde:
> O que estudamos, propusemos, rejeitamos, decidimos e pretendemos testar?

## `dyegorodrigues/PokeSagaLab`
Sandbox especializado existente. Não é a Foundry.

## Regra
Uma IA pode ler simultaneamente SAGA + Foundry, mas deve manter fontes de verdade separadas:
- fatos operacionais → SAGA;
- pesquisa/decisão futura → Foundry.
