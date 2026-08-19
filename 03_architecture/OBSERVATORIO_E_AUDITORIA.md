# Observatório e Auditoria

**Status:** `PRE-CANONICAL` · **NÃO AUTORIZA IMPLEMENTAÇÃO** · decisões correlatas: D057–D065

Proposta de camada de observação e auditoria para o período **pós-fechamento curricular**.

## Problema

O SAGA verifica exaustivamente o que pode ser verificado sem sair de casa
(2.516+ testes, sondas Chrome real, canário, Matrix, DAG) e não verifica nada
que exija observar uma criança.

Duas perguntas não têm instrumento hoje:

1. a criança aprendeu?
2. o motor decidiu certo?

`Progress` responde *onde ela está*. Não responde *como chegou* nem *por que o
Sensei escolheu aquilo*.

## Janela

Restam 4 fallbacks (`GM.11, N5.05, N6.02, PE.04`). A fábrica curricular termina
sozinha em poucas ondas.

O risco não é a fábrica consumir o projeto para sempre — é o vazio no dia
seguinte ser preenchido por outra fila interna (divergências, legado, `Moedas`,
backlog P2) antes que exista qualquer observação de criança real.

Esta camada precisa estar pronta para ser a fila seguinte.

## Parte 1 — Recibo de Sessão (D057, D058)

Dois eventos. Schema fechado. Sem áudio, sem texto livre da criança, sem
localização. Pseudônimo desde o primeiro byte (LGPD art. 14).

### Evento de item

```
sessao_id · aprendiz(pseudo) · build · ts
competencia · ficha · nivel · modo
item_sig · resultado · rt_ms · tentativas · ajuda · pulou
misconception · mastery_antes · mastery_depois
review_force · e_revisao · dias_desde_ultima_pratica
```

### Evento de prescrição

```
sessao_id · ts · motor · escolha
razao: fronteira | revisao_vencida | resgate_causal
     | fluencia | intercalacao | evidencia_faltante
candidatos[]: { id, score, motivo }
estado_relevante: { prereqs, revisoes_vencidas, resgates_abertos }
```

O evento de prescrição é a peça inexistente em qualquer forma hoje. Ele não
altera comportamento: o Sensei continua sendo autoridade única de prescrição.
É observabilidade pura.

Justificativa evidence-first: as perguntas da Parte 3 não são deriváveis de
`Evidencia` nem dos contratos atuais, porque `Progress` é fotografia e a decisão
do orquestrador não é persistida em lugar nenhum.

## Parte 2 — Avaliar a criança (D059, D060)

Acerto dentro do motor não é evidência de aprendizagem: um sistema adaptativo
correto mantém a criança perto de 80% **por construção**. Medir acerto interno
mede o motor.

Cinco instrumentos, todos fora do motor adaptativo:

| Instrumento | Momento | Responde |
|---|---|---|
| Linha de base | antes de qualquer uso | de onde partiu |
| Pós-teste | 4–6 semanas | avançou |
| Retenção atrasada | 3 e 8 semanas após parar | ficou ou evaporou |
| Transferência | formato nunca visto, fora da tela | entendeu ou aprendeu o SAGA |
| Justificativa | oral, anotada | há compreensão sob o acerto |

Prova de papel: seis contas escritas à mão, sem tablet. É o teste mais barato e
o único que não se pode enganar a si mesmo.

Guardrails: nenhum score global ou composto (D031); RT é telemetria de fluência
e nunca critério de domínio conceitual (D032); justificativa é anotação escrita
do adulto, nunca áudio persistido (D023).

## Parte 3 — Auditar o sistema (D061, D062)

Estende `FALSIFICATION_GATES.md` num eixo novo. Os 12 gates existentes
perguntam *"esta ficha é honesta antes de promover?"*. Estas auditorias
perguntam *"o motor decidiu certo ao longo do tempo?"*.

| # | Auditoria | Método | Métrica |
|---|---|---|---|
| A1 | Prescrição | 50 eventos classificados à mão | taxa de decisão correta |
| A2 | Validade do DAG | acerto no 1º contato com Y, com X vs sem X | aresta real ou decorativa |
| A3 | Calibração de item | proporção de acerto no 1º contato | p>0,95 não ensina; p<0,30 quebrado |
| A4 | Diagnóstico | 30 erros com tag, verificação manual | falso positivo e falso negativo |
| A5 | Intervenção | taxa da misconception 2 semanas após | intervenção validada ou inerte |
| A6 | Limiar de domínio | coroados que sobrevivem à revisão 21/45d | limiar frouxo ou apertado |
| A7 | Saúde de sessão | abandono, `helpClicks`, `skips` por ficha | problema de tela, não de matemática |

A1 é manual e insubstituível. A4 responde a Open Question 6.
A5 é o loop que valida a biblioteca de intervenções — o ativo mais raro que
este projeto pode produzir.

Limite duro: p-valor descritivo é leitura, não modelo. Nada aqui autoriza
engine psicométrico, IRT ou RL de prescrição (`ARCHITECTURE_MINIMUM.md`).

## Parte 4 — Personas sintéticas (D062)

Estende `longitudinalSenseiSimulation.test.ts` e
`longitudinalAutomaticitySimulation.test.ts`, que hoje testam invariantes
binários, para instrumento de medida.

| Persona | Comportamento | Caça |
|---|---|---|
| Ideal | aprende conforme o modelo | o caminho feliz termina |
| Lenta sólida | acerta, RT acima do alvo | reprovação injusta por tempo |
| Buraco fundacional | tudo menos composição do dez | resgate acha a raiz ou o sintoma |
| Chutadora | ~30% por sorte, RT baixíssimo | o limiar coroa quem chuta |
| Esquecida | perde tudo em 10 dias | espaçamento reage ou avança |
| Desistente | ajuda sempre, pula muito | andaime desvanece ou vicia |
| Irregular | some 3 semanas, volta | revisão ou parede |

200 sessões por persona, no CI. Audita a inteligência do motor sem depender de
criança e pega regressão longitudinal que teste de invariante não pega.

Limite: persona sintética valida **coerência** do motor, nunca **aprendizagem**.
Prova que o sistema faz o que foi projetado; não prova que o projetado ensina.

## Parte 5 — Continuidade (D063)

A proposta original desta frente era um portão de razão fixa (1 entrega de
observatório a cada 3 ondas). Ela foi **retirada**: é a mesma família de
`percentual semanal rígido`, já rejeitada em D036.

Substituição: portão orientado a achado.

> Nenhuma onda nova abre enquanto existir achado de auditoria aberto de
> severidade alta.

Condição verificável, no formato dos gates que já existem (canário, Matrix),
e não quota de calendário.

## Parte 6 — Costuras de expansão (D064)

Não implementar lógica, computação, programação ou IA. Manter D046, D026, D028,
D029 e o roadmap R1–R8 de `FUTURE_PROOFING.md`.

Três costuras baratas que preservam o caminho sem runtime novo:

1. `dominio` explícito no schema de competência; motores deixam de assumir
   matemática.
2. Contrato de ponte declarativo em ficha (`pontes: [{ para, tipo }]`), sem
   consumidor. Anota o que D011/D037/D047 já decidiram, enquanto as fichas são
   escritas.
3. `Progress`, `MasteryEvidence` e o Recibo nunca assumem domínio. `skill_id` é
   `skill_id`.

Regra: nenhuma competência de outro domínio entra em runtime antes de existir
retenção e transferência medidas em criança real, em pelo menos uma competência
de matemática.

## Integração com o SAGA produtivo

Nada aqui altera o SAGA. Quando houver autorização explícita, o caminho é:

1. `PROMPT_DE_RETOMADA.md` ganha uma seção de fase para a frente Observatório;
2. `ESTADO_DO_FECHAMENTO.md` passa a registrar achados de auditoria abertos;
3. o Recibo entra como módulo isolado, sem tocar canário, Matrix, ledger ou
   runtime map;
4. personas sintéticas entram como suíte nova, sem alterar as existentes.

Ordem sugerida: Recibo → linha de base dos filhos (tem prazo: antes de qualquer
uso sério) → personas sintéticas → criança sozinha → painel de auditoria.

## Naming (D065)

Diferido. `SAGA` permanece codinome interno e não deve receber investimento de
marca.

Evidência: 32 candidatos testados por RDAP em `.com` e `.com.br` — 31 ocupados.
O espaço de palavra curta pronunciável está esgotado, o que é a razão estrutural
de existirem Duolingo, Kahoot, Quizlet e Sphero. Qualquer processo de naming que
comece gerando "palavras bonitas" desperdiça o esforço antes da busca de
anterioridade.

Brief e processo ficam registrados quando a frente for aberta. Pré-requisito:
existir criança fora de casa usando o produto.

## Reconciliação com a Issue #47 — quem manda

**A Issue #47 do SAGA é a autoridade do pós-90/90.** Ela foi escrita em 17/08, é
mais completa que esta frente e vive no repositório de produção. Esta frente é
**subordinada** a ela e não cria fila paralela.

Sobreposição real, já coberta por #47 e que **não deve ser reimplementada aqui**:

| Parte desta frente | Autoridade em #47 |
|---|---|
| Evento de prescrição | Gate D — decision trace obrigatório |
| Recibo de Sessão | Gate E — telemetria e observabilidade |
| Personas sintéticas | Gate G — Aprendiz Simulado (lista mais completa) |
| Criança sozinha | Gate J — piloto infantil silencioso |
| Auditorias A2/A3 | Gate B — mega-auditoria de microprogressão |

Onde houver divergência de detalhe, **#47 vence**. Este documento passa a ser
material de apoio dessas gates, não plano concorrente.

### O que esta frente acrescenta e #47 não tem

Uma coisa só, e é substantiva:

> **Medir se a criança aprendeu, fora do motor adaptativo.**

#47 mede usabilidade (Gate J), coerência longitudinal (Gate G) e observabilidade
(Gate E). Nenhum desses responde *"a criança aprendeu matemática?"*.

Instrumentos ausentes em #47, definidos na Parte 2 deste documento:

- linha de base antes do primeiro uso — **irrecuperável depois**;
- pós-teste e retenção atrasada (3 e 8 semanas após parar);
- itens de transferência fora da tela;
- prova de papel;
- justificativa oral anotada.

E o guardrail que os sustenta: **taxa de acerto dentro do motor não é evidência
de aprendizagem** — um sistema adaptativo correto mantém a criança perto de 80%
por construção. Medir acerto interno mede o motor, não a criança.

Proposta de encaixe: esses instrumentos entram como sub-item do Gate J de #47,
ou como gate próprio entre J e a calibração. Decisão do usuário.

### Recurso não renovável

A linha de base só pode ser coletada uma vez por criança, antes do primeiro uso
sério. Se o piloto do Gate J acontecer antes dela, o dado de partida some para
sempre e nenhuma medida posterior de ganho é interpretável.

É o único item desta frente com prazo, e ele é anterior ao Gate J.

## Via de resolução — taxonomia proposta para os achados do Gate B

Observação a partir do Lote 1 (N1, 13 competências, 10 achados, todos
`HIPÓTESE-A-PROVAR`).

Classificar o achado é metade do trabalho. A outra metade — que o Lote 1 ainda não
faz — é dizer **como cada hipótese pode ser resolvida**. Sem isso, o Gate B tende a
produzir ~70 hipóteses ao longo dos domínios restantes sem caminho de fechamento,
e um registro que só cresce deixa de ser instrumento.

Três vias, mutuamente exclusivas:

| Via | Como fecha | Exemplos do Lote 1 |
|---|---|---|
| `CODIGO` | inspeção de fonte executável; fecha hoje, sem criança | GAP-007 (faixa grafo≠ficha), GAP-011 (N1.13 folha no DAG), GAP-003, GAP-008, GAP-010 |
| `SIMULACAO` | campanha de Aprendiz Simulado — Gate G | achados sobre progressão, mastery frouxa, loop |
| `CRIANCA` | só observação em piloto — Gate J | GAP-005, GAP-006, GAP-009 — "falta ponte/microtutorial" é hipótese sobre confusão, e confusão não se prova lendo código |

Duas consequências:

1. A via `CODIGO` fecha em paralelo, barata, sem depender de gate nenhum.
   Dois achados do Lote 1 foram confirmados por inspeção direta em minutos.
2. A via `CRIANCA` reposiciona o Gate J: ele não é só a última etapa de validação —
   é o **mecanismo de resolução** de uma fração relevante da saída do Gate B.
   Isso reforça a precondição de linha de base, que precede o Gate J.

Proposta: cada achado do Lote 2 em diante nasce com `via` declarada. Achados de via
`CODIGO` podem ser fechados sem esperar os gates seguintes.

Sem autoridade sobre a Issue #47 — proposta metodológica, sujeita a D067.

## Achado estrutural — `lvl` declarado e ignorado em `generatorsF2.ts`

Encontrado ao verificar o GAP-018 do Lote 2 (N2.05) contra a fonte, em 19/08/2026.

`gN2_05` recebe `lvl: number` e **nunca o referencia no corpo**. `base = ri(1,9)*10`
produz sempre um número de dois dígitos, e o enunciado é sempre *"arredonde para a
dezena mais próxima"*. Os cinco níveis entregam a mesma tarefa. A ficha promete
dezena → centena → milhar → precisão → estimativa.

Isso confirma o GAP-018 — mas a função imediatamente seguinte no arquivo tem o
mesmo defeito, o que sugeriu padrão em vez de caso isolado.

Varredura de `src/utils/generatorsF2.ts` no HEAD `a5101b3`:

| | |
|---|---|
| geradores com parâmetro `lvl` | 8 |
| **usam** `lvl` | 4 |
| **declaram e ignoram** `lvl` | **4** — `gN3_11`, `gN3_12`, `gN2_05`, `gN3_13` |

Escopo da varredura: apenas `generatorsF2.ts`. `src/utils/generators.ts` não contém
geradores nesse formato e não foi mapeado — a varredura precisa ser refeita com o
padrão correto antes de qualquer afirmação sobre ele.

### Por que isso muda o Gate B

1. **Três dos quatro são N3** — domínio do Lote 3. O padrão foi identificado antes
   do lote que iria encontrá-lo.
2. É **um achado estrutural, não quatro candidatas independentes**. Tratar como
   quatro GAPs separados perde a causa comum e multiplica o registro sem multiplicar
   a informação.
3. É via `CODIGO` de verificação trivial: um teste que falha quando um gerador
   declara `lvl` e não o usa fecha a classe inteira e impede reincidência — em vez
   de auditar competência por competência.

Proposta: o Lote 3 deve começar verificando se o padrão se estende, e o registro
deve tratá-lo como classe. Sujeito a D067 — sem autoridade sobre a Issue #47.

## CLASS-001 confirmado por varredura independente — e a lacuna que ele expõe

Varredura própria no HEAD `9c6b6d4`, com parser que cobre `const NOME = (args) =>`
e `function NOME(args)`, sobre os quatro arquivos de geradores:

| Arquivo | com `lvl` | usam | ignoram |
|---|---|---|---|
| `generators.ts` | 26 | 22 | 4 |
| `generatorsF1.ts` | 8 | 4 | 4 |
| `generatorsF2.ts` | 8 | 4 | 4 |
| `generatorsVisual.ts` | 6 | **0** | **6** |
| **total** | **48** | 30 | **18** |

Bate exatamente com o CLASS-001 do Lote 3, nome por nome. **37,5% dos geradores que
recebem nível descartam o nível.** `generatorsVisual.ts` não tem diferenciação de
nível alguma — 6 de 6.

### A lacuna estrutural do plano

Gate B produz achados e é AUDIT-ONLY por desenho, o que está certo. Mas a §15 da
Issue #47 encadeia B → C → D → E → … e **não define fase de reparo para a saída do
Gate B**.

Estado após três lotes (33 de 90 competências):

| | |
|---|---|
| candidatas abertas | 27 |
| via `CODIGO` | 23 |
| via `SIMULACAO` | 1 |
| via `CRIANCA` | 3 |
| classes confirmadas | 1 (CLASS-001, 18 casos) |

Extrapolando a taxa observada, os ~57 competências restantes devem gerar algo entre
40 e 50 candidatas adicionais. Sem fase de reparo declarada, o Gate J — piloto com
criança — aconteceria sobre um app com dezenas de defeitos **conhecidos e
confirmados**, o que invalida a leitura do piloto: não se distingue confusão da
criança de defeito já catalogado.

### Proposta — Gate B′ entre B e C

Fase de reparo explícita, dividida por via:

1. **`CODIGO` primeiro.** Fecha sem criança e sem gate. Inclui CLASS-001, que fecha
   como classe: um teste estático que reprova gerador declarando `lvl` sem uso, com
   `_lvl` como supressão explícita e wrapper que encaminha passando.
2. **`SIMULACAO`** migra para o Gate G como entrada, não como dívida solta.
3. **`CRIANCA`** migra para o Gate J como roteiro de observação — vira o que se
   olha no piloto, em vez de ficar esperando.

Regra: nenhuma candidata de via `CODIGO` deve continuar aberta quando o Gate J
começar. Sujeito a D067 — proposta, sem autoridade sobre a Issue #47.

## Conformance ficha ↔ DAG — classe fechada em 10 casos

Varredura própria em 19/08/2026 sobre **todas as 90 competências** do HEAD `4a2ad53`
— não apenas as 45 já auditadas pelo Gate B. Compara `prereqs` e `faixa` de cada
ficha TS contra `src/curriculum/grafo_saga.ts`.

### prereqs divergentes — 6

| Competência | Ficha | DAG | Já achado? |
|---|---|---|---|
| `N3.10` | `[N3.03]` | `[N3.03, N3.04]` | GAP-026 |
| `N4.03` | `[N4.01]` | `[AL.03, N4.01]` | CLASS-002 |
| `N4.06` | `[N4.03]` | `[N4.03, N4.05]` | CLASS-002 |
| `N4.07` | `[N4.04]` | `[N4.04, N4.06]` | CLASS-002 |
| `N4.08` | `[N4.07]` | `[N2.04, N3.11, N4.07]` | CLASS-002 |
| **`GM.04`** | `[N2.01, AL.01]` | `[N1.06]` | **não — domínio não auditado** |

### faixa divergente — 4

`N1.08` (F1↔F0) · `N1.12` (F0/F1↔F1) · `N2.07` (F2↔F3) · **`GM.04`** (F2↔F1)

### Duas consequências

**1. A classe está fechada em 10 casos.** Não é dívida aberta que cresce a cada lote:
o repositório inteiro foi varrido e não há mais nada. Isso permite dimensionar o
reparo agora, sem esperar os cinco lotes restantes.

**2. `GM.04` é de natureza diferente e mais grave.** Todos os outros são *ficha
declara subconjunto do DAG* — direção segura, porque o `unlockEngine` usa
`GrafoSaga`, derivado do DAG, e portanto aplica a regra mais estrita. `GM.04`
declara pré-requisitos **disjuntos**: `[N2.01, AL.01]` na ficha contra `[N1.06]` no
DAG, sem interseção. O runtime segue o DAG, então "Horas" desbloqueia após `N1.06`
enquanto a autoria da ficha pressupunha sistema decimal e álgebra inicial.

Não é higiene de metadado: é uma discordância pedagógica real sobre quando a
competência pode ser ensinada, e alguém precisa decidir qual das duas está certa.

### Sobre CLASS-002

A refutação registrada no Lote 4 está **correta e foi verificada**: `unlockEngine.ts`
importa `GrafoSaga` de `utils/grafoSaga`, que deriva de `curriculum/grafo_saga.ts`,
e itera `node.prereqs`. A ficha não participa da decisão de desbloqueio. Não há
liberação precoce hoje.

Proposta: unificar CLASS-002, GAP-026, GAP-007, GAP-021 e o caso `GM.04` numa única
classe de conformance ficha↔DAG, fechável por um teste que compara os dois. `GM.04`
sai dessa classe e vira decisão pedagógica própria. Sujeito a D067.

## DECISAO-001 / GM.04 — recomendação com diagnóstico

A divergência de metadado é sintoma. A causa está no conteúdo.

| | DAG | Ficha |
|---|---|---|
| nome | "Horas (ponteiros e digital)" | "Relógio: **Horas e Minutos**" |
| faixa | F1 | F2 |
| prereqs | `[N1.06]` — Numerais 0-10 | `[N2.01, AL.01]` |

Os micros da ficha GM.04:

- `a` — "ler **horas exatas** no relógio analógico" → é a GM.04 do DAG;
- `b` — "avançar o tempo em **frações de 15 minutos**" → é território da GM.06.

E a GM.06 já existe no DAG como *"Horas e minutos; duração"*, F2, prereqs
`[GM.04, AL.03]`, com ficha viva ensinando *"cada número do mostrador vale 5
minutos"* e *"descobrir uma duração"*.

### Diagnóstico

A ficha GM.04 absorveu conteúdo de minutos que pertence à GM.06, e então
reescreveu os próprios prereqs e a faixa para justificar o conteúdo invasor. Por
isso os prereqs ficaram disjuntos: `[N2.01, AL.01]` sustenta *contar de 5 em 5*,
não *ler a hora cheia*.

### Recomendação

**O DAG está certo.** Ler hora cheia num relógio analógico exige reconhecer os
numerais de 1 a 12 e distinguir dois ponteiros — `N1.06` basta, e F1 é a faixa
correta. Uma criança de 5 anos aprende "o ponteiro curto está no 3, são 3 horas"
sem saber dezena nem contar de 5 em 5.

Ler **minutos** é outra competência: exige contagem de 5 em 5 até 60, ou seja,
estrutura decimal e salto — que é exatamente o que a GM.06 declara com
`[GM.04, AL.03]`.

Ação proposta, em três passos e nesta ordem:

1. Devolver a ficha GM.04 ao escopo de hora cheia — remover o micro de frações
   de 15 minutos, que já tem casa na GM.06.
2. Só então alinhar `faixa: "F1"` e `prereqs: ["N1.06"]` ao DAG.
3. Verificar se a GM.06 precisa absorver o micro removido ou se já o cobre.

Fazer só o passo 2 seria pior que não fazer nada: alinharia o metadado e deixaria
uma ficha F1, com pré-requisito de numerais, ensinando frações de 15 minutos.

**Continua sendo decisão do dono do projeto.** Esta é recomendação com evidência,
não escolha feita. Sujeita a D067.

## Candidata a CLASS-005 — embaralhamento enviesado em 26 pontos

Encontrado ao verificar CLASS-004 no Lote 6, em 19/08/2026. Não é achado por
competência: é infraestrutura transversal, e por isso o Gate B por domínio
dificilmente o encontraria.

### O fato

`.sort(() => Math.random() - 0.5)` aparece **26 vezes** em `src/`:

| Arquivo | Ocorrências |
|---|---|
| `src/curriculum/Composer.ts` | 18 |
| `src/utils/generatorsVisual.ts` | 3 |
| `src/curriculum/procedimentos/contagem20Contract.ts` | 2 |
| `src/curriculum/fichas/dojo/sensei/dojo_{add,sub,mul,div}.ts` | 1 cada |

Comparador aleatório em `sort` não produz permutação uniforme. Medido em Node,
200 mil execuções, array de 4 opções:

| | pos 0 | pos 1 | pos 2 | pos 3 |
|---|---|---|---|---|
| elemento 0 | **36,0%** | 17,3% | 15,7% | 31,0% |
| elemento 1 | 14,0% | **39,2%** | 37,3% | 9,5% |
| elemento 2 | 18,7% | 24,8% | 28,2% | 28,2% |
| elemento 3 | 31,3% | 18,7% | 18,8% | 31,2% |

Pior desvio do uniforme: **15,5 pontos percentuais**. Fisher-Yates nas mesmas
condições: 0,2 pontos.

`shuffle` em `src/components/GameLoop.tsx:109` **já é Fisher-Yates correto** e é
usado no caminho de revisão. A correção existe no repositório; só não foi aplicada
nos 26 pontos.

### Por que importa neste produto especificamente

Nos geradores, a resposta correta costuma ser construída como primeiro elemento do
array de opções. Ela cai na primeira posição em ~36% das vezes em vez de 25% — uma
criança que sempre toca na primeira opção acerta **44% mais** do que o acaso.

Isso contamina três coisas que o SAGA usa como verdade:

1. **evidência de domínio** — chutar por posição rende mais do que deveria, e a
   coroa pode ser comprada por regularidade de interface;
2. **detecção de misconception** — resposta escolhida por posição é registrada como
   erro conceitual, virando falso positivo no Radar; é a Open Question 6 sendo
   corrompida na origem;
3. **a própria auditoria** — CLASS-004 caça viés posicional competência a
   competência enquanto uma fonte sistêmica de viés posicional está em 26 pontos.

### Fechamento

Via `CODIGO`. Classe única, não 26 candidatas. Fecha substituindo por Fisher-Yates
e travando com um teste que proíbe o padrão `sort` com comparador aleatório — mesmo
formato do gate proposto para CLASS-001.

Recomendação de prioridade: **antes do Gate J**. Um piloto infantil rodando sobre
viés posicional produz dados de aprendizagem que não se pode interpretar.

Sujeito a D067 — proposta, sem autoridade sobre a Issue #47.
