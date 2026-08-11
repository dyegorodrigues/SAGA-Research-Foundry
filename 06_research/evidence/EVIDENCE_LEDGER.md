# Evidence Ledger

**Status:** ledger de pesquisa pré-canônica. Evidência externa limita hipóteses; não autoriza runtime por si só.

## Taxonomia obrigatória

Toda claim nova deve ser marcada como uma das quatro classes:

- `SOURCE-DERIVED` — derivada de fonte externa identificável;
- `REPO-DERIVED` — observada no repositório/gates do SAGA;
- `INFERENCE` — conclusão argumentativa apoiada por fontes/estado;
- `DESIGN-HYPOTHESIS` — proposta ainda dependente de experimento.

Para fonte externa, registrar também **o que ela NÃO prova**.

## E01 · Transferência CT → STEM

**Classe:** SOURCE-DERIVED

**Fonte:** Li, Z.; Oon, P. T. (2024). *The transfer effect of computational thinking (CT)-STEM: a systematic literature review and meta-analysis*. International Journal of STEM Education, 11:44. DOI: `10.1186/s40594-024-00498-z`.

**Leitura usada pela Foundry:** a síntese encontrou transferência próxima mais robusta que transferência distante e heterogeneidade relevante.

**Implicação de design:** transferência não deve ser presumida; Bridge + probe/delayed probe permanecem hipóteses coerentes para ensiná-la e medi-la.

**Não prova:** que o Transfer Ladder ou qualquer Bridge Pair específico do SAGA funciona.

## E02 · Treino espacial e matemática

**Classe:** SOURCE-DERIVED

**Fonte:** Hawes, Z. C. K.; Gilligan-Lee, K. A.; Mix, K. S. (2022). *Effects of Spatial Training on Mathematics Performance: A Meta-Analysis*. Developmental Psychology, 58(1), 112–137. DOI: `10.1037/dev0001281`.

**Leitura usada pela Foundry:** efeito positivo médio em matemática, aproximadamente `g ≈ .28` no material de origem.

**Implicação de design:** spatial thinking merece integração transversal com matemática.

**Não prova:** benefício de um minigame espacial isolado nem um motor separado de mastery.

## E03 · Metacognição e autorregulação

**Classe:** SOURCE-DERIVED

**Fonte:** Education Endowment Foundation (2025). *Metacognition and Self-Regulated Learning, Second Edition*.

**Eixos usados:** planejar, monitorar, avaliar, modelagem/scaffolding e integração em tarefas reais.

**Implicação de design:** favorecer Metacognitive Sampling contextual, não uma disciplina separada de “metacognição”.

**Não prova:** frequência ótima de prompts, schema de state ou eficácia específica no SAGA.

## E04 · Guided play

**Classe:** SOURCE-DERIVED

**Fonte:** Skene, K. et al. (2022). *Can guidance during play enhance children’s learning and development in educational contexts?* Child Development, 93(4), 1162–1180. DOI: `10.1111/cdev.13730`.

**Implicação de design:** F0/F1 pode preservar agência dentro de ambiente intencional e guiado.

**Não prova:** superioridade universal de guided play para todo objetivo ou faixa.

## E05 · Productive Failure

**Classe:** SOURCE-DERIVED / REFERÊNCIA A COMPLETAR

O material de origem registra literatura favorável a problem-solving-before-instruction em condições específicas, com consolidação posterior que explora gaps/erros.

**Implicação de design:** candidato seletivo para debugging, bridges e design em faixas/tarefas adequadas.

**Não prova:** que Productive Failure deva ser regra geral, especialmente em F0.

**Pendência documental:** adicionar referência bibliográfica completa antes de qualquer claim quantitativa ou guideline mais forte.

## E06 · Learning by Teaching

**Classe:** SOURCE-DERIVED / REFERÊNCIA A COMPLETAR

O material de origem registra meta-análise de geração de materiais para ensinar outros, 23 artigos / 62 comparações, efeito médio global aproximado de `0.17`.

**Implicação de design:** `teach_agent` / Teach the Creature merece experimento controlado.

**Não prova:** eficácia específica no SAGA nem justificativa para criar primitive dedicada.

**Pendência documental:** promover a citação bibliográfica completa do estudo antes de usar o número como evidência de decisão.

## E07 · CSTA 2026

**Classe:** SOURCE-DERIVED

**Fonte:** Computer Science Teachers Association. *2026 CSTA PK–12 Computer Science Standards*. DOI registrado no pacote de origem: `10.1145/3820482`.

**Leitura usada:** computação não se reduz a coding; algoritmos/design, dados, sistemas, impacto humano e caminhos de IA/data science/physical computing importam.

**Implicação de design:** programação formal deve nomear/expandir estruturas já vividas; não deve substituir fundações cognitivas e matemáticas.

**Não prova:** uma sequência etária única nem a arquitetura do Thinking Engine.

## E08 · UNESCO AI Competency Framework

**Classe:** SOURCE-DERIVED

**Fonte:** UNESCO (2024). *AI Competency Framework for Students*.

**Leitura usada:** competências envolvem mentalidade centrada no humano, ética, técnicas/aplicações e design de sistemas, com progressão de compreensão para aplicação/criação.

**Implicação de design:** AI literacy futura não pode virar “curso de prompts”; deve incluir dados, limites, impacto e design responsável.

**Não prova:** que IA deva entrar cedo no runtime do SAGA.

## E09 · Evidência interna do SAGA

**Classe:** REPO-DERIVED

Fontes operacionais que devem ser reancoradas no produto antes de uso:

- `src/constants/evidencias.ts` — condições de evidência existentes;
- `AL.02` — regularidade/unidade de repetição;
- `N2.01` — representação bidirecional numeral↔material;
- `PADRAO_OURO.md` — reuso, QA visual, seed, sonda e progressão de linguagem visual;
- `RETOMADA.md` — estado operacional e precedência.

**Regra:** fatos de estado do produto envelhecem; reexecutar gates/Matrix e não congelar números deste ledger.

## Força atual das decisões

### Alta confiança
- Content Graph separado de Practice Evidence;
- runtime determinístico no core;
- RT não é mastery;
- transferência precisa ser sondada em vez de presumida;
- metacognição contextual;
- reuse-first;
- sem score global de inteligência.

### Moderada
- Teach Agent;
- envelopes Probe/Mission/Bridge/Project;
- Practice Receipt específico;
- delayed probe integrado a infraestrutura de revisão existente.

### Experimental
- práticas do primeiro slice;
- thresholds e profile derivado;
- timing de Productive Failure;
- momento de criar Lab visível;
- mechanics/stages definitivos.

## Regra final

> Evidência externa define limites e hipóteses. O repositório define o que existe. O cânone SAGA define identidade pedagógica. Experimentos decidem o que ainda é incerto.
