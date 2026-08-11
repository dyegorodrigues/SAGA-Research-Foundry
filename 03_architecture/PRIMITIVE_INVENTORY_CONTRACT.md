# Primitive Inventory Contract

**Status:** contrato de interpretação · 11/08/2026

## Por que este arquivo existe

A pesquisa acumulou números diferentes para “primitivas”: ~11–13 ligadas em certos recortes históricos, 18 em inventários anteriores, 26 declaradas nas fichas e outros totais em protótipos. Esses números só são comparáveis quando a definição do universo é a mesma.

A Foundry não congela um novo total. **O inventário real vem do SAGA produtivo e dos gates executáveis.**

## Universos que NÃO devem ser misturados

### 1. Primitivas declaradas por fichas

Saída do `npm run fichas:auditar` no snapshot reancorado de 11/08/2026:

- **26 nomes de primitivas declaradas** no catálogo autoral.

Esse número responde: “quantos nomes de ferramenta/primitive aparecem nas fichas?”.

### 2. Estado do mapa ficha → runtime

Na mesma auditoria executável:

- **21 executáveis**;
- **4 renderer-sem-builder**;
- **1 componente-isolado**;
- **0 ausentes** segundo essa taxonomia do mapa;
- `Moedas` continua sendo a única primitiva marcada como bloqueadora pela Coverage Matrix, porque seu contrato necessário para `GM.03` não está implementado como o método exige.

Essas categorias respondem a uma pergunta de wiring/runtime, não à quantidade de competências em Composer.

### 3. Competências em Composer

- **30 Composer ativos** no snapshot.

Esse 30 é contagem de **competências**, não de primitivas. Portanto `30 Composer` nunca deve ser apresentado como “30 primitivas Composer”.

### 4. Inventários históricos/protótipos

Contagens preservadas em dossiês, audits e `.ts` históricos são evidência de proveniência. Elas não ganham autoridade por estarem mais detalhadas nem por terem percentuais calculados.

## Regra para toda auditoria futura de reuse

Antes de calcular cobertura/reuso:

1. reancorar o HEAD do SAGA produtivo;
2. executar `fichas:auditar` e Coverage Matrix;
3. declarar explicitamente o universo sendo contado;
4. separar `declarada`, `renderer`, `builder`, `componente isolado`, `executável` e `bloqueadora`;
5. só então calcular reuse por família/mode.

Percentual hardcoded em protótipo não é evidência operacional.

## Regra de deriva

Este arquivo registra **definições**, não um baseline eterno. Os números acima são um snapshot de 11/08/2026 e devem ser substituídos por saída executada quando o produto mudar.
