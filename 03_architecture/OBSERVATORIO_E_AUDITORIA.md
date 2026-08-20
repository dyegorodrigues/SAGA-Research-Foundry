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

## CLASS-006 é muito maior que N7 — e é o achado mais grave até aqui

Confirmada e **estendida** por verificação externa em 19/08/2026, HEAD `66b40d0`.

### A cadeia, verificada ponta a ponta

1. Dos 39 contratos especializados em `src/curriculum/procedimentos/` que montam
   `opcoes`, **26 não contêm `shuffle`, `embaralh` nem `Math.random`**. Não é
   embaralhamento enviesado — é ausência de embaralhamento.
2. A helper desses contratos serializa a correta em primeiro lugar, literalmente:
   `return [{ value: correta, ... }, ...erradas.map(...)]`.
3. `GameLoopExerciseRenderer.tsx` e `ExerciseRenderer.tsx` **não embaralham**.
4. O único `shuffle` do caminho de jogo está em `GameLoop.tsx:98`, dentro de
   `if (!pure && bank.length && Math.random() < 0.35)` — ou seja, **apenas no
   caminho de revisão**, que dispara em ~35% das vezes e puxa do banco.

**Conclusão: em questão fresca, nesses 26 contratos, a alternativa correta é sempre
a primeira opção.**

### Os 26 contratos

`angulos, areaF81, circuloAreas, conversaoUnidades, divisaoLonga, estatisticaChance,
expressaoF77, fatoresRetangulos, horasMinutos, jornalTurma, linguagemLetras,
mapaTesouro, mediaChance, multiplicarFracoes, operarNegativos, paresImpares,
perimetro, planoCartesiano, poligonos, primosDivisores, problemasMedida, retaCompleta,
solidosGeometricos, somaFracoes, volumePrismas, volumeVistas`

Atravessa N4, N5, N6, N7, AL, GE, GM e PE. **O Gate B por domínio não encontraria
isso**: o defeito não é de competência, é do contrato de opções.

### Por que é mais grave que CLASS-005

CLASS-005 desloca a probabilidade de 25% para 36%. CLASS-006 a leva a **100%**.

Consequências diretas sobre o que o produto afirma medir:

- **domínio pode ser obtido sem matemática** — tocar sempre na primeira opção
  acerta tudo em questão fresca; a coroa é comprável por regularidade de interface;
- **misconception vira ruído** — quem toca por posição não tem concepção errada, e
  o Radar registra como se tivesse; é a Open Question 6 corrompida na origem;
- **CLASS-003 e CLASS-004 ficam subestimadas** — elas mediam viés posicional caso a
  caso enquanto isto vale para dois terços dos contratos.

### Ressalva de escopo, para não superdimensionar

Vale para os palcos que apresentam `opcoes` como lista de alternativas. Palcos
manipulativos, em que a criança arrasta, toca no cenário ou produz a resposta, não
consomem a ordem do array e não são atingidos. A extensão exata por palco ainda
precisa ser levantada — mas a direção do erro já está provada.

### Consequência para o cronograma

Recomendação revista: **CLASS-006 deve ser corrigida antes de qualquer coisa,
inclusive antes dos lotes restantes do Gate B.**

O motivo não é o Gate B. É a linha de base. Coletar linha de base, telemetria ou
piloto sobre um sistema em que a resposta certa é sempre a primeira produz dado
que não se pode interpretar depois — e a linha de base é recurso não renovável.
Auditar mais domínios enquanto isso é acumular achados sobre um alicerce que já se
sabe torto.

A correção é pequena: aplicar o Fisher-Yates que já existe em `GameLoop.tsx:109` na
serialização das opções, e travar com teste que reprove corpus cuja resposta correta
fique na mesma posição em todos os casos canônicos.

## REGRESSÃO NO REPARO CLASS-005/006 — documentação vinculante apagada

Encontrada em 19/08/2026 ao verificar o HEAD `799b3a4`. **O reparo funcional está
correto; o dano é colateral e não foi detectado por nenhum gate.**

### O que está certo

- `sort(() => Math.random() - 0.5)`: **27 → 0**;
- `src/utils/shuffle.ts` criado, Fisher-Yates único e compartilhado;
- `class005006ShufflePolicy.test.ts` com 122 linhas;
- guards de validação curricular do Composer **preservados** — `Intervalo vertical`,
  `exigir e proibir`, `Reagrupamento duplo`, `operand_step` mantêm contagem idêntica;
- cadeia vermelho → reparo → verde coerente e com recibos reais.

### O que quebrou

| Arquivo | Linhas | Comentários | Bytes |
|---|---|---|---|
| `src/curriculum/Composer.ts` | 1245 → 483 | **152 → 0** | −16.566 |
| `src/components/GameLoop.tsx` | 1179 → 515 | **89 → 0** | −13.101 |

**Todos os comentários dos dois arquivos de runtime mais importantes foram removidos.**
Cerca de 30 KB de rationale.

Desproporção: no `Composer.ts` apenas **18 linhas** continham o padrão a corrigir.
Foram removidas **762**.

### Por que isso é dano real, e não estética

Entre o texto perdido está regra vinculante de diagnóstico:

> *"A ordem é a armadilha §6.8: do mais específico ao mais genérico. Com `OFF_BY_ONE`
> na frente, ele engoliria `CHUTE_SEGURO` toda vez que a alternativa central caísse a
> um do alvo."*

> *"Fica aqui, e não em `tagNumericDistractors`, porque duas das três tags não são
> regras sobre o valor: `CHUTE_SEGURO` fala da POSIÇÃO na tela e `COPIA_ULTIMO` fala
> da peça anterior à lacuna."*

São as instruções que impedem alguém de reordenar a lista de tags e quebrar o Radar
**em silêncio**. Sem elas, a próxima sessão reordena por elegância e o diagnóstico
degrada sem teste vermelho.

### É reincidência, e o protocolo já a proíbe

O corpo do PR #35 registra a mesma falha na W36, quando `ficha_runtime_map.cjs` foi
comprimido e perdeu literais e documentação vinculantes. A regra escrita ali:

> *"Cânone compartilhado é aditivo. Cânone não se comprime: não remover documentação,
> rationale, aliases, notas ou observabilidade preexistentes."*

`Composer.ts` e `GameLoop.tsx` não constam da lista nominal de cânone compartilhado,
mas são o motor de composição e o laço de jogo. O princípio se aplica com ainda mais
força, e a lista provavelmente está incompleta.

### Por que o CI ficou verde

Comentário não é testado. Os recibos `32308381219` e `32308381231` são legítimos e
não cobrem este dano. É o limite do portão, não fraude do relatório — a sessão de
produção reportou o reparo com honestidade e provavelmente não percebeu a perda.

### Recuperação

O conteúdo está em `66b40d0` e não se perdeu do Git. Duas rotas:

1. **Preferida** — refazer o reparo como diff cirúrgico a partir de `66b40d0`,
   tocando apenas as linhas do padrão e os imports. Produz o mesmo resultado
   funcional sem tocar em mais nada.
2. Restaurar a documentação sobre o código atual, arquivo por arquivo, conferindo
   que cada bloco voltou ao lugar certo.

### Gate que faltava

Nenhum portão observa perda de documentação. Proposta: teste que reprova queda de
densidade de comentários acima de um limiar em arquivos de runtime declarados
sensíveis, no espírito da catraca de `coresLiterais.test.ts` — o teto só desce
quando alguém registra explicitamente a melhora.

Sujeito a D067.

## Restauração executada — e a causa raiz da reincidência

Executada e verificada nesta sessão, 19/08/2026. Empurrada para
`dyegorodrigues/SAGA`, branch `claude/saga-empresa-educacional-visao-ty4jpy`,
commit `658011a`, em fast-forward sobre `799b3a4`. `codex/fechamento-curricular`
e `main` não foram tocadas.

### O que foi feito

Refazer o reparo CLASS-005/006 como diff cirúrgico a partir de `66b40d0`, em vez de
sobre o arquivo já comprimido. Método: transformação mecânica dos 18 sites do
Composer e dos 3 pontos do GameLoop, com o arquivo documentado como base.

Regras aplicadas:

- `X.sort(() => Math.random() - 0.5)` → `fisherYates(X)`;
- `options.sort(…);` como statement → `options = fisherYates(options);`, porque
  `fisherYates` não muta e `.sort` mutava;
- remoção do `shuffle` local do GameLoop, agora importado do utilitário.

### Verificação com dependências reais

| Verificação | Resultado |
|---|---|
| `tsc --noEmit` | limpo |
| `npm run build` (inclui `grafo:check`) | verde |
| Suíte | **247 arquivos / 3.459 testes, todos passando** |
| Coverage Matrix observada | `75/15/0/90/11`, 94 fichas, `Moedas` ausente |
| Comentários | `Composer` 152 · `GameLoop` 89 — restaurados |
| `sort` com comparador aleatório | 0 |
| Guards do Composer | `Intervalo vertical`, `exigir e proibir`, `Reagrupamento duplo`, `operand_step` — intactos |

Preservado do reparo original: `src/utils/shuffle.ts`, política dos 25 IDs em
`composerCanary.ts`, `class005006ShufflePolicy.test.ts` e as demais substituições.
Nada revertido.

### A medida que prova o método

| Diff contra `66b40d0` | Inserções | Deleções |
|---|---|---|
| caminho anterior, só `Composer.ts` | 184 | **946** |
| esta restauração, os dois arquivos | 33 | 50 |

### Causa raiz — por que isto se repete

Não é descuido pontual. Aconteceu na W36 com `ficha_runtime_map.cjs` e de novo
agora, com dois arquivos maiores. O padrão:

1. **O agente regenera o arquivo em vez de aplicar patch.** Pedido para mudar 18
   linhas, ele reescreve 1.245. A saída fica funcionalmente equivalente porque os
   testes cobrem comportamento.
2. **Comentário não é testado.** É a primeira coisa a cair numa regeneração, e
   nenhuma suíte reclama.
3. **Nenhum portão observa densidade documental.** O CI fica verde de forma
   legítima, o recibo é real, e a perda só aparece se alguém comparar à mão.
4. **O rationale perdido é justamente o que impede regressão futura** — regra de
   precedência de tags, motivo de um valor estar num arquivo e não em outro. Perder
   isso não quebra hoje; quebra na próxima sessão que reordenar por elegância.

O ponto 3 é o único acionável por gate, e é o que falta.

### O portão que fecha a classe

Catraca de densidade documental, no espírito de `coresLiterais.test.ts`: para
arquivos de runtime declarados sensíveis, a contagem de linhas de comentário tem
piso registrado e **o piso só sobe**. Queda reprova nomeando arquivo, contagem
anterior e atual.

Lista mínima: `Composer.ts`, `GameLoop.tsx`, `ficha_runtime_map.cjs`,
`coverage_matrix_core.ts`, catálogos de misconceptions e o arquivo que hoje é
autoridade de evidências — cujo caminho precisa ser resolvido no tree, porque
`evidencias.ts` não existe nos caminhos óbvios.

Sem esse portão, a próxima regeneração repete tudo. Sujeito a D067.

## Catraca documental — verificada por mutação e ampliada 18×

Verificação e melhoria executadas em 19/08/2026 sobre o HEAD `a043861`.

### O que a sessão de produção entregou, e está correto

`src/governance/documentacaoRuntime.test.ts` + baseline JSON. Testado por mutação
nesta sessão, com dependências reais, nas três direções declaradas:

| Mutação | Resultado |
|---|---|
| estado limpo | passa |
| remover 1 comentário do Composer | reprova — `152 → 151` |
| acrescentar 1 sem atualizar baseline | reprova — `152 → 153`, pedindo o novo piso |
| restaurar | passa |

A autoridade de evidências foi resolvida corretamente: `src/constants/evidencias.ts`
existe e tem 204 linhas de comentário. Nenhum caminho inventado. E a restauração
`658011a` foi integrada por fast-forward, sem force.

### O buraco encontrado

A catraca nomeava **6 arquivos à mão**. Varredura do runtime: 64 arquivos com 40+
linhas de comentário, **60 desprotegidos**.

Os dois arquivos mais documentados do projeto estavam fora: `emojiRowProcedure.ts`
com 300 linhas e `emojiRowContract.ts` com 264 — o dobro do `Composer.ts`, que
estava protegido. O diretório `procedimentos/` inteiro, onde mora o rationale
pedagógico de cada competência, não tinha portão. `composerCanaryIds.ts` também
estava fora, com 54 linhas.

> Lista escrita à mão protege o que alguém lembrou de escrever. Foi assim que a W36
> aconteceu, e a catraca criada para impedir a reincidência herdou o mesmo formato.

### A correção

Descoberta automática: todo arquivo de runtime não-teste com **≥20 linhas de
comentário** precisa ter piso registrado. Cânone nominal fica protegido sempre,
mesmo caindo abaixo do limiar — sem isso, esvaziar um arquivo até 19 linhas o
removeria do portão.

Cobertura: **6 arquivos / 698 linhas → 108 arquivos / 7.468 linhas.**

Quatro invariantes, todos verificados por mutação:

1. arquivo documentado fora da baseline reprova, nomeando caminho e contagem;
2. baseline apontando para arquivo inexistente reprova;
3. perda de comentário reprova, mostrando anterior → atual;
4. ganho sem atualizar baseline reprova, para o piso subir junto.

Mutações executadas: remover comentário de `emojiRowProcedure.ts`, antes sem
proteção alguma, passou a reprovar em `300 → 299`; arquivo novo com 25 linhas de
comentário reprovou por estar fora da catraca.

Verificado: `tsc --noEmit` limpo, **248 arquivos / 3.463 testes passando**.

Commit `c4fd3f2` em `claude/saga-empresa-educacional-visao-ty4jpy`, fast-forward
sobre `a043861`. Linha viva e `main` intocadas.

## CLASS-006 NÃO está fechada — medição empírica das 75 competências

Medido em 19/08/2026 sobre o HEAD `f1f61ea`, com dependências reais.
Método: `generateRegisteredFichaQuestion(id, nivel)` para cada canário ativo,
níveis 1–5, 120 amostras por par, registrando a posição do gabarito entre as
opções.

### Resultado

| | |
|---|---|
| pares competência/nível medidos | 288 |
| pares com gabarito concentrado ≥60% numa posição | **75** |
| competências afetadas | **18** |

O Lote 8 reportou resíduo em quatro (`AL.01-L5`, `AL.03`, `AL.05`, `AL.08`).
São dezoito, e a maioria está em **100%** — posição inteiramente determinística.

```
AL.01  L5:p0=100%
AL.02  L1..L4:p0=100%
AL.03  L1:p1=68% L2..L4:p1=100% L5:p2=63%
AL.05  L1..L5:p0=100%
AL.08  L1..L5:p0=100%
GE.04  L3:p0=64%
N1.01  L1:p1=100% L2:p0=100% L3:p2=61%
N2.06  L1:p0=100% L2:p1=100% L3:p0=100% L4:p1=100% L5:p0=100%
N3.02  L1..L5:p0=100%
N4.01  L1..L5:p0=100%
N4.12  L1..L5:p0=100%
N5.01  L1:p0=61% L2,L3,L5:p0=100%
N5.02  L1,L2:p0=100%
N5.03  L1,L2:p0=100% L3:p2=100% L4:p1=100% L5:p1=69%
N6.01  L1..L5:p0=100%
N6.02  L1..L5:p0=100%
N6.03  L1..L5:p0=100%
N6.04  L1..L5:p0=100%
```

### A causa, escrita no código

`src/curriculum/motores/composerCanary.ts`:

```ts
return CLASS_006_FRESH_OPTION_IDS.has(id) ? shuffleFreshStageOptions(question) : question
```

O embaralhamento só ocorre para os **25 ids de uma allowlist fixa**. Todo o resto
passa direto. O reparo é correto para quem está na lista e inexistente para quem não
está.

### Dois casos que provam a gravidade

**`N6.01` não está na allowlist.** É exatamente a competência que originou a
CLASS-004 — comparar decimais, com o gabarito sempre à esquerda. O defeito foi
achado, confirmado, agravado por verificação externa, escalado a classe própria — e
o reparo não o cobriu. Mede 100% na posição 0 nos cinco níveis.

**`N2.06` foi refutada como falso positivo** sob o argumento de que o gabarito
alterna de posição entre os níveis. A medição mostra `L1:p0=100%`, `L2:p1=100%`,
`L3:p0=100%`, `L4:p1=100%`, `L5:p0=100%`. Dentro de cada nível a posição é fixa. Uma
criança pratica **um nível por vez**: alternar entre níveis não protege ninguém. A
refutação estava errada.

### O padrão, pela terceira vez

1. W36 — `ficha_runtime_map.cjs` comprimido, cânone nominal por lista;
2. catraca documental — 6 caminhos escritos à mão, 60 arquivos de fora;
3. CLASS-006 — allowlist de 25 ids, 18 competências de fora.

> **Lista escrita à mão protege o que alguém lembrou de escrever.** É o mesmo
> mecanismo de falha em três lugares diferentes, e duas dessas listas foram criadas
> justamente para impedir a falha anterior.

### A correção

Inverter o padrão: **embaralhar por default**, com exceção explícita e justificada
para palcos em que a ordem é semântica — e mesmo nesses, garantir que o gabarito
não fique invariável dentro de um nível.

O portão deve ser a medição, não a lista: gerar os casos canônicos de cada
competência ativa em todos os níveis, com N amostras, e reprovar quando o gabarito
se concentrar acima de um limiar numa posição. Isso não pode ser burlado por
esquecimento.

**Enquanto isto não fechar, nenhuma medição de aprendizagem é interpretável** — nem
linha de base, nem telemetria, nem piloto.

## CLASS-006 fechada — execução e três correções no próprio gate

Executada nesta sessão sobre o vermelho `ac855a1`, que a sessão de produção
materializou antes de ficar sem contexto. Commit `c4b8c17` na branch
`claude/saga-empresa-educacional-visao-ty4jpy`. Linha viva e `main` intocadas.

### A correção do produto

Default invertido: **embaralhar sempre**. `CLASS_006_ORDEM_SEMANTICA` guarda
exceção explícita e justificada — e **não dispensa a medição**. Quem está na
exceção continua sendo medido e reprova se concentrar. Esquecer de listar deixa de
abrir buraco silencioso e passa a produzir teste vermelho.

Única exceção registrada: **N1.05**, cujas alternativas são os índices dos dois
grupos do palco `quantidade`, respondidos por toque na cena e não em lista. Medida
em 200 amostras por nível, já se distribui em torno de 50% nos cinco.

### Três defeitos encontrados no gate ao usá-lo

O regression-first estava certo na concepção e errado em três detalhes que só
apareceram ao rodar contra o produto corrigido.

**1. Ponto cego de formato.** O helper de identidade só conhecia `value`.
`shapecanvas` serializa `figura`, então **GE.02 saía silenciosamente da amostra** —
um ponto cego dentro do portão criado justamente para não ter pontos cegos. Chave
desconhecida continua reprovando, para formato novo não sumir.

**2. Limiar fixo é errado nas duas direções.** 60% é severo demais para 2
alternativas, onde o acaso ultrapassa isso com frequência — foi o que produziu o
falso positivo de `N1.05/L3` a 61,7%. E é frouxo demais para 4, onde 55% já é o
dobro do esperado e passaria batido. Passou a ser **`1/k + 4σ`**.

**3. Tamanhos misturados.** O mesmo par gera listas de tamanhos diferentes quando
alternativas duplicadas colapsam: `AL.02/L5` alterna entre 2 e 4 alternativas,
`N4.01/L1` entre 2, 3 e 4. Medir tudo junto sub-representa as últimas posições e
inventa viés. A medição passou a ser **por número de alternativas**.

Os três juntos: sem o 1, uma competência inteira não era medida; sem o 2 e o 3, o
gate produzia falso positivo e falso negativo ao mesmo tempo.

### Verificação

| | |
|---|---|
| `tsc --noEmit` | limpo |
| `npm run build` | verde |
| Suíte | **248 arquivos / 3.437 testes** |
| Gate por mutação | verde; vermelho ao desligar o embaralhamento |
| Medição independente | 288 pares, **zero concentração real** |
| `AL.02`, última suspeita | 3.000 amostras/nível: 52,0/48,0 e 48,8/51,2 — variação normal |

`composerCanary.ts` entrou na catraca documental com piso 32.

### O que isso destrava

Era o portão que separava o projeto de conseguir medir. Com o gabarito distribuído,
acerto volta a significar matemática, misconception volta a significar concepção
errada, e **linha de base, telemetria e piloto passam a ser interpretáveis**.
