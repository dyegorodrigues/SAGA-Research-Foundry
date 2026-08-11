# Thinking Engine / Thinking Lab — Registro Reconciliado de Detalhe v0.98

> **Status:** especificação de P&D pré-canônica.
>
> Este arquivo preserva o nível fino de detalhe desenvolvido nas rodadas de pesquisa, auditoria e design sem transformar hipótese em runtime.
> Para estado operacional, código, CI, mastery, unlock, prereqs e decisões de implementação, o repositório `dyegorodrigues/SAGA` continua soberano.

## 1. North Star

O Thinking do SAGA existe para formar uma criança que:

> **sabe o que fazer quando ainda não sabe a resposta.**

Formulação funcional:

> **Thinking Lab é a superfície de experiências em que a criança mobiliza, combina e transfere ferramentas de pensamento. Thinking Engine é a infraestrutura que observa essas práticas longitudinalmente e as conecta ao conhecimento real da criança.**

Formulação técnica:

> **Content Graph governa conhecimento. Practice Ontology descreve práticas. Challenge Grammar fabrica experiências. Evidence observa processo. Learner State reconcilia tudo. Sensei decide a próxima dose.**

O objetivo não é prometer que todo conteúdo será “fácil”, nem treinar uma inteligência genérica descontextualizada. O objetivo é tornar familiar o ciclo de transformar confusão em estrutura: observar, representar, testar, revisar, explicar e transferir.

## 2. Arquitetura conceitual reconciliada

### 2.1 Três dimensões

1. **Content Graph** — o que a criança sabe.
2. **Practice Ontology / Thinking Graph suave** — como a criança mobiliza ferramentas de pensamento.
3. **Application Arenas** — onde essas ferramentas são aplicadas: matemática, ciência, engenharia, programação, robótica, dados/IA, linguagem/humanidades e situações cotidianas.

Relação conceitual:

`Content Graph × Practice Ontology × Arena/Representação`

### 2.2 Autoridade

- Content Graph continua soberano para prereqs, mastery e unlock.
- Practice Ontology não cria hard gates curriculares.
- Thinking não cria segundo Tutor, segundo Composer ou segundo Curriculum Graph.
- Telemetria observa; não reescreve automaticamente o grafo.
- Um perfil de prática só deve ser persistido se mudar uma decisão útil do Sensei, QA ou comunicação responsável.
- Não existe score global de raciocínio, “QI SAGA” ou rótulo de criança “lógica/não lógica”.

## 3. Loop nuclear de raciocínio

Experiências Thinking devem, quando apropriado, materializar o seguinte ciclo:

`perceber → estruturar → planejar → tentar → observar resultado → testar/depurar → revisar → explicar → transferir`

Nem toda tarefa precisa mostrar todas as etapas. O autor deve saber qual etapa é alvo e qual evidência torna essa etapa observável.

## 4. Toolbelt infantil

Vocabulário de ação antes do termo técnico:

- **Olha**
- **Separa**
- **Quebra**
- **Mostra**
- **Planeja**
- **Testa**
- **Caça o bug**
- **Tenta de outro jeito**
- **Confere**
- **O que prova?**

Os termos formais — algoritmo, condição, estado, variável, abstração, causalidade etc. — podem aparecer depois que a criança já viveu a estrutura cognitiva.

## 5. Practice Ontology — 8 famílias / 40 práticas

A ontologia é descritiva, não um segundo currículo.

### OBS — Observar e estruturar
- `TH-OBS-01` — notar atributos relevantes;
- `TH-OBS-02` — classificar por regra;
- `TH-OBS-03` — selecionar informação relevante;
- `TH-OBS-04` — detectar regularidade/padrão;
- `TH-OBS-05` — generalizar e procurar contraexemplo.

### MOD — Representar e modelar
- `TH-MOD-01` — externalizar uma situação;
- `TH-MOD-02` — escolher representação útil;
- `TH-MOD-03` — converter entre representações;
- `TH-MOD-04` — abstrair detalhes irrelevantes;
- `TH-MOD-05` — construir, usar e criticar modelos.

### LOG — Inferir, julgar e pensar causalmente
- `TH-LOG-01` — relações e lógica básica;
- `TH-LOG-02` — inferir a partir de pistas;
- `TH-LOG-03` — julgar plausibilidade;
- `TH-LOG-04` — distinguir evidência, hipótese e explicação;
- `TH-LOG-05` — raciocinar sobre causalidade e sistemas.

### ALG — Decompor e algoritmizar
- `TH-ALG-01` — ordenar sequência;
- `TH-ALG-02` — decompor problema;
- `TH-ALG-03` — criar procedimento/algoritmo;
- `TH-ALG-04` — reconhecer e usar repetição/loop;
- `TH-ALG-05` — usar condição/evento;
- `TH-ALG-06` — compreender estado/variáveis;
- `TH-ALG-07` — modularizar e reutilizar.

### DBG — Testar, depurar e otimizar
- `TH-DBG-01` — comparar esperado vs observado;
- `TH-DBG-02` — localizar a primeira divergência;
- `TH-DBG-03` — formular hipótese de bug;
- `TH-DBG-04` — criar/usar casos de teste;
- `TH-DBG-05` — iterar e otimizar.

### DAT — Dados e incerteza
- `TH-DAT-01` — coletar e organizar dados;
- `TH-DAT-02` — ler/comparar representações de dados;
- `TH-DAT-03` — formular pergunta respondível por dados;
- `TH-DAT-04` — raciocinar sobre incerteza/probabilidade;
- `TH-DAT-05` — compreender relação entre dado, amostra e modelo.

### ENG — Criar, projetar e construir
- `TH-ENG-01` — definir necessidade/problema;
- `TH-ENG-02` — explicitar critérios e restrições;
- `TH-ENG-03` — gerar alternativas;
- `TH-ENG-04` — prototipar e testar;
- `TH-ENG-05` — comparar, justificar e redesenhar.

### META — Metacognição, estratégia e transferência
- `TH-META-01` — definir objetivo e plano;
- `TH-META-02` — monitorar progresso;
- `TH-META-03` — explicar estratégia/evidência;
- `TH-META-04` — comparar e selecionar estratégias;
- `TH-META-05` — reconhecer estrutura profunda e transferir.

## 6. Maturidade de prática — P0–P4

Esta escala é **conceitual** e separada dos níveis curriculares da Jornada.

- `P0` — participa/modela com forte apoio;
- `P1` — usa a prática com suporte;
- `P2` — usa de forma independente em contexto familiar;
- `P3` — seleciona/combina a prática em situação nova próxima;
- `P4` — generaliza, testa limites, explica ou ensina a estratégia.

Decisão vigente: não persistir P0–P4 automaticamente como um segundo sistema de mastery. Primeiro testar derivação por `Evidencia`/receipts; persistir somente se houver utilidade demonstrada.

## 7. Progressão 4–12+ detalhada

Idade orienta apresentação; evidência governa progressão.

### F0 — aproximadamente 4–5
- atributos e classificação;
- sequências simples;
- informação relevante;
- decomposição concreta;
- causalidade imediata;
- representação manipulável;
- algoritmo linear;
- primeira cultura de “funcionou/não funcionou/onde mudou?”.

### F1 — aproximadamente 5–7
- caminhos e instruções;
- repetição;
- `se... então...` concreto;
- escolha entre estratégias simples;
- padrões com mais de um atributo;
- prever regra;
- começo de sistemas/máquinas simples.

### F2 — aproximadamente 7–9
- decomposição explícita;
- diagramas, tabelas e mapas;
- estado intuitivo;
- variável intuitiva;
- condições;
- testes sistemáticos;
- múltiplas soluções;
- critérios/restrições;
- pseudocódigo e blocos.

### F3 — aproximadamente 9–11
- abstração;
- modelagem;
- casos de teste e edge cases iniciais;
- eficiência;
- causalidade vs coincidência;
- dados/probabilidade;
- sistemas e trade-offs;
- programação visual;
- engenharia virtual.

### F4 — aproximadamente 11–12+
- generalização e invariantes;
- modularidade, funções e parâmetros;
- debugging sistemático;
- experimentos controlados;
- redes/sistemas;
- modelos computacionais;
- dados, limitações e viés em IA;
- código textual opcional.

## 8. Transferência — Ladder T0–T4

Transferência não é assumida; é ensinada e sondada.

- `T0` — mesma estrutura, pequenas variações;
- `T1` — mesma estrutura, nova representação;
- `T2` — mesmo domínio, nova superfície/contexto;
- `T3` — outro domínio;
- `T4` — transferência aberta: a criança reconhece sozinha qual ferramenta usar.

### Bridge Pair

Um Bridge Pair é um par de tarefas estruturalmente isomorfas cuja superfície muda de propósito.

`TransferSignature` deve declarar:
- `structure`;
- `invariants`;
- `requiredPractices`;
- `surfaceFeatures`;
- `sourceDomain`;
- `targetDomain`.

Pergunta pedagógica útil: **“O que ficou igual mesmo parecendo diferente?”**

Não declarar transferência apenas porque uma tarefa B veio depois de A. Delayed probes são candidatos importantes para distinguir repetição imediata de transferência mais robusta.

## 9. Challenge Grammar

Modelo reconciliado:

`ThinkingExperience = ContentAnchor × TaskKind × Mechanic × StageCapability × Presentation × EvidenceContract × ScaffoldPolicy × TransferSignature`

Outra visão útil de autoria:

`Challenge Kernel × Narrative Skin × Interaction Mechanic`

- **Kernel** = estrutura cognitiva profunda;
- **Skin** = mundo/narrativa;
- **Mechanic** = gesto/gramática de interação.

Trocar Skin mantendo Kernel ajuda a testar transferência sem fingir que “contexto novo” = “habilidade nova”.

## 10. TaskKinds, envelopes e arquétipos

### TaskKinds
- CLASSIFY
- SEQUENCE
- PREDICT
- REPRESENT
- PLAN_TRACE
- DEBUG
- TEST
- COMPARE
- OPTIMIZE
- MODEL_SIMULATE
- DESIGN_BUILD
- BRIDGE_TRANSFER

### Experience envelopes de runtime/autoria
- Probe
- Mission
- Bridge
- Project

### Arquétipos de experiência preservados para design
Estes nomes são famílias de design, não enums obrigatórios:
- Quick Puzzle;
- Guided Investigation;
- Debug Mission;
- Strategy Duel;
- Bridge Pair;
- Open Build;
- Design Challenge;
- Simulation Lab;
- Teach Back.

## 11. Mechanics / primitives de design

Catálogo reconciliado atual:
- classify_into_bins
- identify_outlier
- reorder_dependencies
- continue_pattern
- find_pattern_bug
- compose_command_sequence
- plan_spatial_route
- compress_repetition
- conditional_behavior
- infer_transform
- find_first_divergence
- run_compare_revise
- filter_relevant_information
- compare_strategies
- causal_structure
- probabilistic_experiment
- constraint_design
- teach_agent

Vocabulário histórico preservado como aliases/ideias de ferramenta — **não como obrigação de Stage**:
`sortBins`, `oddOneOut`, `sequenceCards`, `patternRail`, `routePlanner`, `commandQueue`, `ruleMachine`, `ifThenBoard`, `loopComposer`, `bugHunter`, `testBench`, `relevanceFilter`, `representationBuilder`, `strategyCompare`, `causeMap`, `dataLab`, `chanceLab`, `constraintBuilder`, `modelSimulator`, `teachCreature`.

Regra: **reuse-first**. Verificar TaskKind → Mechanic → Stage atual → modo/composição antes de criar software novo.

## 12. One Novelty Axis

Na aquisição, tentar manter uma novidade dominante por vez para preservar interpretabilidade diagnóstica.

Eixos possíveis:
- conteúdo;
- prática;
- representação;
- mechanic/UI;
- contexto.

Isso é heurística, não fórmula rígida. “Novelty Budget” numérico arbitrário está rejeitado.

## 13. Evidência de processo

Acerto final sozinho não prova a prática.

Campos candidatos de observação/derivação:
- `success`;
- `independence`;
- `strategySelected`;
- `representationUsed`;
- `representationChanged`;
- `testsRun`;
- `revisionCount`;
- `bugLocalized`;
- `evidenceSelected`;
- `explanationMode`;
- `robustAcrossCases`;
- `transferLevel`;
- `contextNovelty`;
- `scaffoldLevel`.

Exemplo conceitual: duas crianças podem chegar ao mesmo resultado; uma tenta aleatoriamente muitas vezes, outra planeja, testa, localiza divergência e revisa. `success=true` não torna os processos equivalentes.

### Candidate ThinkingState — somente se necessário

Possíveis campos:
- `practiceId`;
- `maturity`;
- `confidence` da inferência/instrumento;
- contextos/domínios vistos;
- representações vistas;
- `transferMax`;
- evidence IDs;
- tendência de scaffold;
- tags de erro/misconception.

Não criar esse schema antes de demonstrar que `Evidencia`/derivação não bastam.

## 14. Scaffolding

O runtime deve reutilizar a linguagem/estrutura de scaffolding do SAGA.

Escada conceitual de apoio — **não criar enum paralelo S0–S6**:
1. nenhum apoio;
2. foco atencional;
3. reexpressar objetivo;
4. oferecer/induzir representação;
5. sugerir família de estratégia;
6. entregar passo parcial;
7. modelagem completa.

Regra crítica:
- modelagem completa **ensina**, mas não prova independência;
- após modelagem completa, usar fresh item estruturalmente semelhante para colher evidência independente.

## 15. Metacognitive Sampling

Não perguntar “como você pensou?” em toda tarefa.

Amostragem metacognitiva deve ocorrer em momentos informativos, por exemplo:
- depois de troca de estratégia;
- após erro produtivo;
- após comparação de duas soluções;
- em Bridge;
- após revisão;
- quando a justificativa ajuda a distinguir acaso de compreensão.

Objetivo: metacognição contextual, não fricção verbal constante.

## 16. Debugging como cultura

Loop infantil/operacional:
1. O que você esperava?
2. O que aconteceu?
3. Onde apareceu a primeira diferença?
4. Qual é sua hipótese?
5. Mude uma coisa.
6. Teste de novo.
7. Teste outro caso.

Debugging não deve ser tratado como punição por errar; é uma forma normal de aprender sobre sistemas.

## 17. Dieta de problemas

O Thinking não pode ser composto só por puzzles convergentes.

- **Tipo A — convergente:** uma resposta/solução-alvo clara.
- **Tipo B — multi-estratégia:** mesma meta, múltiplos caminhos defensáveis.
- **Tipo C — aberto:** múltiplas soluções válidas, com critérios/restrições explícitos.

Problemas abertos não devem entregar mastery a um julgador LLM soberano. Avaliação deve se apoiar em contratos observáveis, critérios, restrições, testes e evidência verificável.

## 18. Ponte para programação

Progressão conceitual:

`sequência → procedimento → algoritmo → repetição → condição → estado → variável → modularidade → teste → debugging → generalização → otimização → programação visual → sistemas → robótica → dados/modelos → IA`

Regra de experiência:
- ação antes da terminologia;
- formalização depois da vivência;
- sintaxe textual precoce não é objetivo.

## 19. Engenharia e robótica

Loop de engenharia:

`objetivo/necessidade → critérios → restrições → alternativas → plano → protótipo → teste → dados → falha → redesign`

Robótica não é obrigatória para validar Thinking. A mesma gramática pode começar em ambiente digital e, quando houver hardware/infraestrutura, migrar para sistemas físicos.

## 20. Fundamentos para IA

IA não deve virar “aula de prompt”.

Fundamentos progressivos:
- exemplos;
- atributos/características;
- categorias;
- dados;
- representações;
- regras;
- erro;
- incerteza;
- amostra;
- treino/teste;
- limitações;
- viés;
- privacidade;
- impacto humano.

A criança deve compreender que modelos podem errar e que dados/decisões humanas importam.

## 21. Narrativa, mascotes e Creature Engine

Narrativa pode materializar problemas:
- rotas;
- energia;
- repetição;
- restrições;
- causalidade;
- otimização;
- sistemas.

Mascotes podem funcionar como “aluno” que a criança ensina (`teach_agent/teachCreature`).

Guardrail:
- Creature Engine é camada narrativa/experiencial;
- não se torna autoridade de mastery;
- não reescreve learner state;
- integra por contratos/eventos quando houver autorização futura.

## 22. Navegação / superfície de produto

Não criar sexta aba apenas porque Thinking é um pilar.

Estratégia preferida:
1. começar com Thinking Missions contextuais prescritas pelo Sensei;
2. observar massa crítica, uso e necessidade;
3. só depois decidir se existe um Lab/hub dedicado.

## 23. Roadmap de integração preservado

- `R0` — documentação/P&D apenas;
- `R1` — anotar currículo existente com práticas, sem alterar progressão;
- `R2` — audit/Thinking Coverage Matrix;
- `R3` — três mechanics/primitives reutilizáveis;
- `R4` — eventos de processo;
- `R5` — Thinking State experimental, feature-flagged, sem unlock;
- `R6` — Bridge Pairs / Transfer Engine;
- `R7` — missões contextuais do Lab;
- `R8` — programação visual;
- `R9` — Maker/Forja;
- `R10` — robótica/IA.

Este roadmap não atropela a fábrica curricular produtiva. O marco de entrada ainda depende de decisão explícita e do estado real do SAGA.

## 24. Primeiro piloto recomendado

Três alvos de alto valor e alta observabilidade:
1. sequência/algoritmo;
2. debugging/primeira divergência;
3. representação/modelagem.

Anchors candidatos já registrados:
- AL.02 — regularidade/bridge;
- N2.01 — representação;
- N1.12 — arena espacial/tracing experimental.

## 25. Orquestração de autoria — papéis

Papéis de autoria/revisão; não agentes soberanos de runtime:
- Evidence Scout;
- Cognitive Architect;
- Child Development Pedagogue;
- Domain Specialist;
- Challenge Designer;
- Diagnostic/Psychometrics Reviewer;
- UX/Audio Designer;
- Software Architect;
- Red Team / QA.

Fluxo:
`evidence ledger → practice ontology → conteúdo/anchor → adaptação F0–F4 → kernel → evidência → mechanic → contratos → red team → coverage → factory`

Nenhum papel altera cânone automaticamente.

## 26. Research Ledger

Toda decisão de pesquisa deve separar:
- fonte/evidência;
- o que a fonte realmente sustenta;
- inferência de design;
- risco/limite;
- hipótese testável;
- decisão;
- condição de revisão.

Categorias de proveniência:
- SOURCE-DERIVED;
- REPO-DERIVED;
- INFERENCE;
- DESIGN-HYPOTHESIS.

## 27. QA e falsificação

Dimensões mínimas:
- correção de conteúdo;
- observabilidade da prática;
- adequação ao desenvolvimento;
- validade da evidência;
- isomorfismo de Bridge;
- UX/áudio;
- ética/privacidade;
- reprodutibilidade do gerador.

Contratos/testes candidatos:
- `challenge_has_valid_solution`;
- `challenge_respects_age_profile`;
- `challenge_audio_exists_when_required`;
- `challenge_primary_practice_is_observable`;
- `bridge_pair_preserves_invariants`;
- `bridge_pair_changes_surface`;
- `modeled_item_cannot_prove_independence`;
- `motor_error_does_not_emit_thinking_misconception`;
- `speed_does_not_raise_thinking_profile`;
- `content_mastery_does_not_imply_thinking_mastery`;
- `thinking_profile_does_not_unlock_content`.

Geradores determinísticos devem aceitar seed/reprodução e, quando aplicável, property-based tests.

## 28. Thinking Coverage Matrix

A futura matriz deve ser **projeção derivada**, não nova fonte soberana.

Campos candidatos:
`practice → kernels → age bands → mechanics → domains → evidence dimensions → transfer levels → bridge pairs → tests → status → debt`

Ela deve responder onde há cobertura e dívida sem virar currículo paralelo.

## 29. Dados, privacidade e limites de inferência

- minimizar telemetria infantil;
- não guardar áudio bruto por padrão;
- não usar gaze/biometria comportamental sem necessidade/justificativa;
- separar uso de pesquisa de uso de produto;
- consentimento parental quando aplicável;
- não inferir diagnóstico clínico, personalidade ou “inteligência” a partir do gameplay;
- confiança da inferência é sobre o instrumento/evidência, não um julgamento da criança.

## 30. Papel da IA

### IA de autoria pode
- gerar candidatos;
- variar skins;
- sugerir distratores/edge cases;
- revisar consistência;
- auxiliar documentação/pesquisa.

### IA não pode, sem contrato/validação
- atribuir inteligência;
- conceder mastery;
- alterar Curriculum Graph;
- inventar prereqs;
- diagnosticar psicologia;
- julgar problema aberto como soberano;
- reescrever learner state livremente.

### Futuro tutor/LLM de runtime

Recebe:
- Learner State estruturado;
- objetivo autorizado;
- política de scaffolding;
- challenge/evidence contract.

Não recebe mandato aberto para “ensinar qualquer coisa” ou alterar estado soberano sem validação.

## 31. Erros de arquitetura já identificados e corrigidos conceitualmente

- Thinking Graph duro → rejeitado;
- segundo Composer/Tutor/Curriculum Graph → rejeitado;
- score global/QI → rejeitado;
- RT/velocidade como mastery de Thinking → rejeitado;
- telemetria bruta extensa → rejeitada no MVP;
- enum de scaffolding paralelo S0–S6 → rejeitado;
- “One Novelty Axis” como fórmula rígida → rejeitado; permanece heurística;
- muitos Stages novos por entusiasmo → rejeitado; reuse-first;
- LLM soberano para problemas abertos → rejeitado;
- programação por sintaxe precoce → rejeitada;
- robótica obrigatória → rejeitada;
- IA = prompt engineering → rejeitada;
- idade como hard gate → rejeitada;
- protótipos TS históricos como código validado → rejeitado.

## 32. Regra de promoção

Nenhum item deste arquivo entra no SAGA produtivo porque “está bem pensado”.

Promoção exige:
1. reancoragem no GitHub remoto do SAGA;
2. impacto/invariant review quando necessário;
3. alinhamento com Curriculum Graph e learner state;
4. feature flag/rollback quando aplicável;
5. falsification gates;
6. QA real;
7. evidência suficiente para a decisão específica.

## 33. Estado epistemológico deste arquivo

Este registro existe para impedir perda de detalhe.

Ele:
- preserva decisões e insights finos;
- reconcilia ideias antigas com decisões mais novas;
- marca explicitamente o que é heurística, hipótese, candidato ou rejeição;
- não substitui o `DECISION_LEDGER.md`;
- não substitui o `EVIDENCE_LEDGER.md`;
- não substitui o estado operacional do SAGA;
- deve ser revisado quando uma decisão material mudar.
