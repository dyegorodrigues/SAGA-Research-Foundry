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
