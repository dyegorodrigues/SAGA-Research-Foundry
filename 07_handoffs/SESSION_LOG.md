# Session Log

## 2026-08-10 — Fundação e publicação da Foundry
- Frente Thinking consolidada após múltiplas rodadas ChatGPT + revisões externas.
- Decisão arquitetural: separar P&D do SAGA produtivo.
- Workspace criado: `dyegorodrigues/SAGA-Research-Foundry`.
- Repositório mantido público por decisão explícita do usuário neste momento.
- O SAGA produtivo permanece separado; nenhuma decisão desta Foundry autoriza alteração automática em `main` ou `codex/integrar-bloco-f0`.

## 2026-08-10 — Mega revisão pós-publicação
- Auditoria estrutural da Foundry executada contra `FILE_TREE.md`, manifesto, documentos nucleares e reancoragem do SAGA remoto.
- Achado material: os documentos reconciliados existentes preservavam a essência, mas comprimiam parte do nível fino desenvolvido nas rodadas de design.
- Correção aplicada: criado `02_pedagogy/thinking_engine/RECONCILED_DETAIL_REGISTER_V0_98.md`.
- O registro v0.98 consolida explicitamente ontologia 8 famílias/40 práticas, P0–P4, F0–F4, Transfer Ladder T0–T4, Bridge Pairs, Challenge Grammar, TaskKinds, mechanics, One Novelty Axis, evidência de processo, scaffolding, metacognitive sampling, debugging, dieta A/B/C, programação, engenharia, robótica, IA, narrativa, roadmap R0–R10, autoria, QA, privacy e guardrails.
- `START_HERE_NEW_AI.md` foi atualizado para exigir leitura do registro reconciliado.
- `DECISION_LEDGER.md` avançou para v0.98 com D056.
- SAGA reancorado: PR #29 segue `open + draft + unmerged`, HEAD `2e48bb985e2e896e4d61834075fcb7de16696ecf`.
- CI reancorado: workflow `CI` run #1058 / `31444601708` = `success`; quatro jobs verificadas com sucesso.
- A branch temporária `archive/thinking-engine-rd-2026-08-10` não foi encontrada em duas buscas independentes no repositório SAGA; migração marcada como concluída.
- A Foundry continua pré-canônica: documentação e pesquisa não promovem runtime automaticamente.

## 2026-08-18 — Frente Observatório e reancoragem de estado
- Reancoragem do SAGA produtivo por `git fetch` da branch remota: HEAD `22433a3`, 18/08/2026 00:35 -03.
- Achado material: `CURRENT_STATE.yaml` estava obsoleto em **40 ondas** — declarava PR #29 / W6 enquanto a linha viva está em PR #35 com W1–W46 fechadas e W47 em regression-first validado.
- Bloco `production` corrigido. Blocos `last_verified_runtime_snapshot`, `selection_document_snapshot`, `w6_selection` e a `read_order` de `next_session_contract` marcados como `superseded` em vez de apagados ou reescritos com dados não verificados.
- Registrado que a porta operacional viva do SAGA passou a ser `PROMPT_DE_RETOMADA.md`, com `ESTADO_DO_FECHAMENTO.md` como índice e `RETOMADA.md` reduzido a ponte atemporal. A Foundry não sabia disso.
- Matrix real observada nos documentos vivos: `71 Composer / 15 legado / 4 fallback / 86 servidas / 11 divergências`. Fallbacks restantes: `GM.11, N5.05, N6.02, PE.04`.
- Consequência estratégica registrada: a fábrica curricular termina sozinha em poucas ondas. O risco deixou de ser "a fábrica consome o projeto" e passou a ser "o vazio pós-fechamento ser ocupado por outra fila interna antes de qualquer observação de criança real".
- Nova frente registrada: `03_architecture/OBSERVATORIO_E_AUDITORIA.md` — Recibo de Sessão, avaliação fora do motor, sete auditorias de sistema, personas sintéticas, costuras de expansão.
- Ledger avançou para v0.99 com D057–D065, cada uma reconciliada contra decisão anterior.
- Duas propostas foram **retiradas na reconciliação**, não aceitas: gravação de áudio da justificativa (colide com D023) e portão de razão fixa 3:1 entre ondas e observatório (colide com D036). Substituídas por anotação escrita e por portão orientado a achado aberto.
- Limites duros registrados: p-valor descritivo não autoriza engine psicométrico nem RL de prescrição (`ARCHITECTURE_MINIMUM.md`); personas sintéticas validam coerência do motor e nunca aprendizagem.
- Naming diferido (D065) com evidência RDAP: 32 candidatos verificados em `.com` e `.com.br`, 31 ocupados.
- Nada nesta sessão altera o SAGA produtivo. `implementation_authorized: false` permanece.

### Retificação — o "achado" do manifesto era falso

Durante esta sessão registrei que `tools/verify_integrity.py` estaria falhando há
sete dias sem gate que observasse, e tratei o vermelho como bug. **Estava errado
nos dois pontos, e a correção ficou registrada aqui em vez de ser apagada.**

O que o repositório já dizia desde 11/08, em
`06_research/external_reviews/RECOVERY_STATUS_2026-08-11.md`:

- `MANIFEST.sha256.json` é um **snapshot do repositório em 10/08**, contém
  documentos mutáveis e **não deve virar bloqueio** que trate edição legítima de
  documentação como corrupção;
- a autoridade mecânica de integridade passou para `ORIGINALS_MANIFEST.sha256.json`
  + `tools/verify_originals_integrity.py`, executados por
  `.github/workflows/integrity.yml`;
- os hashes de `part05` e `part08` **não foram atualizados de propósito**: o
  mecanismo deve continuar vermelho até recuperação real.

Ou seja: o vermelho não era negligência, era decisão explícita e documentada.
O CI da Foundry está correto ao verificar apenas o transporte imutável dos
originais (`f64f9f3`, 11/08 10:05).

Erro cometido e desfeito nesta sessão: atualizei `MANIFEST.sha256.json` para sete
arquivos, misturando hashes de 18/08 num snapshot de 10/08. O arquivo foi
restaurado ao estado de `4b89c51` e conferido byte a byte. `part05` e `part08`
nunca foram tocados — a única linha cuja violação teria sido grave.

Consequência registrada como **D066**, para que o próximo agente não repita:
manifesto histórico não é gate, e vermelho intencional não se conserta.

### Complemento — material que só existia fora do repositório
Dois documentos foram extraídos da sessão para a Foundry, porque continham detalhe
que não sobreviveria ao fim da conversa:

- `02_pedagogy/PRINCIPIOS_NOMEADOS.md` — os 18 princípios de ciência da aprendizagem
  já implementados no SAGA, com nome técnico e localização no código. É o índice da
  propriedade intelectual pedagógica e a base das perguntas de auditoria.
- `01_vision/NAMING_BRIEF.md` — critérios, processo de 5 passos, evidência RDAP
  (31 de 32 candidatos ocupados) e a colisão conhecida da marca SAGA. Suporta D065.

Nenhum dos dois altera decisão vigente. `MANIFEST.sha256.json` não foi tocado,
conforme D066.

## 2026-08-19 — Verificação independente do 90/90 e subordinação à Issue #47

Verificação do fechamento reportado pela sessão de produção, contra o remoto:

- HEAD `dc6c21c` e promoção `efd270b` confirmados por git;
- `N5.05` presente em `composerCanaryIds.ts`; canário com 75 competências;
- ledger `W50-N5.05` em `coverage_matrix_core.ts` com delta `{composer:+1, fallback:-1, served:+1}`;
- contrato em `coverageMatrix.test.ts` observa `75 / 15 / 0 / 90 / 11`, `modeSwaps=12`, `toolIntroductions=44`;
- CI `32196855192` → head_sha `efd270b`, run 1523, `completed/success`;
- CI `32197697198` → head_sha `dc6c21c`, run 1524, `completed/success`;
- SHAs distintos por recibo — nenhuma reutilização;
- `main` intocada em `106dfe0`; PR #35 segue `open + draft + unmerged`;
- seção "Frente paralela — Observatório" preservada e **corrigida** pela sessão de
  produção, que separou D066 de D057–D065. A correção está certa.

Suíte não executada localmente (sem `node_modules`); a verificação de execução real
apoia-se nos dois runs de CI acima, conferidos por API.

### Achado principal — risco de autoridade dupla

A Issue #47 (17/08) cobre, com mais detalhe, quase toda a frente Observatório
registrada em 18/08: Gate D ≡ evento de prescrição, Gate E ≡ Recibo de Sessão,
Gate G ≡ personas sintéticas, Gate J ≡ criança sozinha, Gate B ≡ auditorias A2/A3.

Registrado **D067**: #47 é a autoridade do pós-90/90 e o Observatório é subordinado.
Cumpre a §15 da própria #47, que proíbe paralelismo com autoridades concorrentes.

Contribuição exclusiva preservada: medição de aprendizagem **fora** do motor
adaptativo — #47 mede usabilidade, coerência longitudinal e observabilidade, e
nenhuma dessas responde se a criança aprendeu. Com o guardrail de que acerto
dentro de motor adaptativo não é evidência de aprendizagem.

Restrição temporal: a linha de base é recurso não renovável e precede o Gate J.

`MANIFEST.sha256.json` não foi tocado, conforme D066.

### Transição pós-90/90 verificada — 19/08/2026
SHA `b116e6c5`, CI `32203533458` `completed/success`, run 1525, head_sha conferido por API.
Escopo real: 2 arquivos — `ROADMAP_90_90_CHILD_READY.md` (índice de 118 linhas, aponta
para fontes canônicas sem copiá-las) e transição de `PROMPT_DE_RETOMADA.md`. `main`
intocada em `106dfe0`; PR #35 segue open+draft+unmerged.

Gate A `FECHADO-COM-RECIBO`; Gates B–J `NÃO INICIADO`. Dívidas classificadas pela §0.2:
15 legado, 11 divergências, `Moedas`/GM.03 e hardening/bundle como `CONFIRMADO-ATUAL`;
Issue #48 e Observatório como `DÍVIDA-REGISTRADA`. D067 foi absorvida corretamente na
porta operacional.

A precondição LINHA DE BASE entrou no Gate J como não renovável, com coleta não iniciada.

Observação registrada para a próxima sessão: entre Gate A e Gate J há nove gates de
trabalho interno. A linha de base **não depende de nenhum deles** — é em papel e pode
ser coletada imediatamente. É o único item irreversível do quadro e o único cujo custo
de adiamento é permanente.

### Gate B · Lote 1 (N1) verificado — 19/08/2026
SHA `ad1b239`, CI `32209683689` `completed/success` run 1526, head_sha conferido por API.
Escopo: 3 arquivos documentais; nenhum arquivo de `src/`. AUDIT-ONLY respeitado.
`main` intocada em `106dfe0`; PR #35 open+draft+unmerged.

Amostragem independente de dois dos dez achados, contra a fonte executável:
- **GAP-011** — `N1.13` aparece uma única vez em `curriculum/grafo_saga.yaml`, como nó
  próprio com `prereqs: [N1.02, N1.04]`; nenhuma competência a lista como pré-requisito.
  É folha. Achado real.
- **GAP-007** — grafo declara `N1.12 faixa: F1`; a ficha viva declara `faixa: "F0/F1"`.
  Divergência real.

Dois de dois conferem. A auditoria é confiável.

Contribuição registrada: taxonomia de **via de resolução** (`CODIGO` / `SIMULACAO` /
`CRIANCA`) para os achados do Gate B. Sem ela, os ~70 achados projetados para os
domínios restantes viram registro que só cresce. Consequência relevante: parte dos
achados só fecha por observação de criança, o que torna o Gate J mecanismo de
resolução do Gate B — e não apenas etapa final. Reforça a precondição de linha de base.

### Gate B · Lote 2 (N2) verificado — 19/08/2026
SHA `a5101b3`, escopo de 3 arquivos documentais, nenhum `src/`, `main` intocada em
`106dfe0`. Amostragem contra a fonte confirmou dois achados:
- **GAP-021** — grafo declara `N2.07 faixa: F3`; ficha TS declara `"F2"`.
- **GAP-018** — `gN2_05` recebe `lvl` e nunca o usa; `base = ri(1,9)*10` fixa dois
  dígitos e todos os níveis viram "arredonde para a dezena".

CI `32216926616` não foi reconferido por API nesta rodada; as três verificações
anteriores de CI conferiram, e o escopo do diff foi validado por git.

**Achado estrutural desta sessão:** a função seguinte a `gN2_05` tem o mesmo defeito,
o que motivou varredura. Em `generatorsF2.ts`, 4 de 8 geradores declaram `lvl` e o
ignoram: `gN3_11`, `gN3_12`, `gN2_05`, `gN3_13`. Três são N3 — domínio do Lote 3.
É classe, não quatro candidatas. Fecha com um teste que proíbe o padrão.
`src/utils/generators.ts` usa outra estrutura e não foi mapeado.

### Gate B · Lote 3 (N3) verificado — 19/08/2026
SHA `9c6b6d4`, 3 arquivos documentais, nenhum `src/`, `main` intocada.
- **GAP-026** confirmado: YAML exige `N3.10 prereqs [N3.03, N3.04]`; ficha TS declara `["N3.03"]`.
- **CLASS-001** confirmado por varredura independente: 18 geradores, mesmos nomes,
  mesmos arquivos. 48 geradores recebem `lvl`, 30 usam, 18 ignoram — 37,5%.
  `generatorsVisual.ts` ignora em 6 de 6.

Registrada a lacuna estrutural: o plano não tem fase de reparo para a saída do Gate B.
27 candidatas abertas, 23 delas via `CODIGO`, e a projeção para os 57 competências
restantes é de mais 40–50. Sem Gate B′, o piloto infantil rodaria sobre defeitos
confirmados e a observação da criança ficaria ininterpretável.

### Gate B · Lote 4 (N4) verificado — 19/08/2026
SHA `4a2ad53`, 3 arquivos documentais, `main` intocada. A refutação do CLASS-002 foi
verificada e está correta: `unlockEngine.ts` importa `GrafoSaga` de `utils/grafoSaga`,
derivado de `curriculum/grafo_saga.ts`, e itera `node.prereqs`; a ficha não participa
do desbloqueio. Não há liberação precoce.

**Varredura própria sobre as 90 competências** (não só as 45 auditadas) para dimensionar
a classe de conformance ficha↔DAG: 6 divergências de `prereqs` e 4 de `faixa`, total 10.
A classe está **fechada** — o repositório inteiro foi varrido.

Um caso não foi encontrado pelo Gate B por estar em domínio não auditado: **`GM.04`**,
ficha `[N2.01, AL.01]` contra DAG `[N1.06]`, disjuntos, mais faixa F2 contra F1. É o
único caso que não é subconjunto, e por isso é discordância pedagógica sobre quando a
competência pode ser ensinada — não higiene de metadado.

Proposta registrada: unificar CLASS-002 + GAP-026 + GAP-007 + GAP-021 numa classe única
fechável por um teste ficha↔DAG, e tratar `GM.04` como decisão à parte.

### Paleta de trilhas — decisão pendente de §4 resolvida por prova — 19/08/2026
`03_architecture/PALETA_DE_TRILHAS.md`. Também verificado o Lote 5 (N5): escopo de 3
arquivos documentais, `main` intocada, e a correção aritmética dele está certa — são
10 divergências de campo em 9 competências, porque `GM.04` responde por duas.

O documento de design pedia escolher entre "estender a paleta para 11 tons" ou
"aceitar compartilhamento". Varredura dos 360° mostra que a primeira opção é
impossível: com erro, acerto e as quatro cores de operação travadas, restam **3
matizes livres** (79°, 246°, 316°) para 11 trilhas. As 4 colisões observadas eram
sintoma, não descuido.

Proposta: matiz passa a identificar **família** e não trilha. Cinco famílias cabem nas
cinco vagas — três matizes livres, o reuso das cores de operação e um neutro.
Dentro da família, claridade distingue. Todas as 11 cores ≥4,5:1 no branco, mínimo
4,91:1, sem colisão com operação nem feedback.

Limite registrado: 11 trilhas distinguíveis sob daltonismo é impossível. Vale para
trilha a mesma regra já travada para operação — cor é reforço, nome e ícone são a
informação.

Também respondidas as outras duas decisões de §4: ficar com `#1e293b` (351 usos
contra 49) e manter `Nunito` no texto por razão técnica de legibilidade infantil,
reavaliando apenas `Fredoka` no display, que é a face que envelhece mal para os 11 anos.

### Gate B · Lote 6 (N6) verificado + candidata a CLASS-005 — 19/08/2026
Lote 6: SHA `3c2ed8e`, 3 arquivos documentais, `main` intocada. **CLASS-004 confirmada
na fonte e é pior que o relatado**: `decimalContract.ts:62` fixa
`[[0.5,0.25],[0.4,0.35],[0.7,0.62],[0.3,0.28]]`, sempre atribui `par[0]` à esquerda, e
`par[0] > par[1]` nos quatro. O ternário `par[0] > par[1] ? "esquerda" : "direita"` é
código morto — a resposta é **sempre** esquerda.

Verificado também que a preocupação análoga no L5 **não** procede: `GameLoop.tsx:98`
embaralha as opções, e o `shuffle` da linha 109 é Fisher-Yates correto.

**Achado novo, transversal:** `.sort(() => Math.random() - 0.5)` em 26 pontos de `src/`,
18 deles em `Composer.ts`. Medido em Node com 200 mil execuções sobre array de 4: o
primeiro elemento cai na primeira posição em 36% em vez de 25%, pior desvio 15,5 pontos
percentuais contra 0,2 do Fisher-Yates. Como a resposta correta costuma ser o primeiro
elemento, chutar a primeira opção rende 44% acima do acaso.

Contamina evidência de domínio, detecção de misconception e a própria premissa da
CLASS-004. Registrado como candidata a CLASS-005, via CODIGO, prioridade antes do Gate J.

### Gate B · Lote 7 (N7) verificado — CLASS-006 é muito maior — 19/08/2026
Escopo do lote correto: 3 commits, 3 arquivos documentais, `main` intocada.

**Correção contra mim:** a contagem de `sort(() => Math.random() - 0.5)` é **27**, não
26. Recontei e a sessão de produção está certa; eu somei errado a lista por arquivo.

**CLASS-006 confirmada e estendida.** Não é fenômeno de N7: de 39 contratos
especializados que montam `opcoes`, **26 não têm aleatorização alguma**, e a helper
serializa a correta como primeiro elemento. Nenhum renderizador embaralha, e o único
`shuffle` do caminho de jogo está restrito ao ramo de revisão de `GameLoop.tsx:94`
(`Math.random() < 0.35`). Logo, **em questão fresca a resposta certa é sempre a
primeira opção**, em contratos que atravessam N4, N5, N6, N7, AL, GE, GM e PE.

Gravidade: CLASS-005 leva o acerto por posição de 25% para 36%; CLASS-006 leva a 100%.
Domínio pode ser obtido sem matemática e misconception vira ruído.

Recomendação revista e registrada: corrigir CLASS-006 **antes** dos lotes restantes do
Gate B e antes de qualquer linha de base, telemetria ou piloto. A linha de base é
recurso não renovável e não se interpreta dado colhido sobre este defeito.

### Reparo CLASS-005/006 verificado — regressão documental encontrada — 19/08/2026
Relatório confirmado como **atual**: HEAD real é `799b3a4`, cadeia `25580ed` (vermelho,
18:54) → `cf7885f` (reparo, 19:12) → `799b3a4` (final, 19:20). `main` intocada.

Funcionalmente o reparo está correto: `sort(() => Math.random() - 0.5)` foi de 27 a 0,
`src/utils/shuffle.ts` existe, a política tem teste de 122 linhas, e os guards de
validação curricular do Composer sobreviveram com contagem idêntica.

**Mas o reparo apagou toda a documentação de dois arquivos de runtime:** `Composer.ts`
de 152 comentários para 0, `GameLoop.tsx` de 89 para 0 — cerca de 30 KB de rationale.
No Composer, 18 linhas continham o padrão a corrigir e 762 foram removidas.

Entre o perdido está a regra de ordem das tags de misconception, que existe justamente
para impedir que alguém reordene a lista e degrade o Radar sem teste vermelho.

É a mesma falha da W36 com `ficha_runtime_map.cjs`, e o corpo do PR #35 já a proíbe:
cânone não se comprime. O CI verde é legítimo e simplesmente não cobre comentário.

Recomendação: bloquear o Lote 8 até refazer o reparo como diff cirúrgico a partir de
`66b40d0`, e criar portão que observe queda de densidade de documentação em runtime.

### Restauração documental EXECUTADA — 19/08/2026
A sessão de produção não conseguiu concluir. Esta sessão executou.

Refeito o reparo CLASS-005/006 como diff cirúrgico a partir de `66b40d0`. Commit
`658011a` na branch `claude/saga-empresa-educacional-visao-ty4jpy` do SAGA, em
fast-forward sobre `799b3a4`. `codex/fechamento-curricular` e `main` intocadas.

Verificado com dependências reais instaladas: `tsc --noEmit` limpo, `npm run build`
verde incluindo `grafo:check`, **247 arquivos de teste e 3.459 testes passando**,
Coverage Matrix observada `75/15/0/90/11` com 94 fichas e `Moedas` ausente.
Comentários de volta em 152 e 89, `sort` aleatório em 0, guards do Composer intactos.

Diff contra `66b40d0`: **33 inserções / 50 deleções** nos dois arquivos, contra 946
deleções só no Composer no caminho anterior.

Causa raiz registrada: o agente regenera arquivos em vez de aplicar patch; comentário
não é testado; nenhum portão observa densidade documental. Só o terceiro item é
acionável por gate, e é o que falta.

### Catraca documental verificada e ampliada — 19/08/2026
Restauração `658011a` confirmada integrada por fast-forward, sem force. Linha viva
em `a043861`, `main` intocada.

A catraca criada pela sessão de produção **funciona** — testada por mutação nesta
sessão nas três direções: limpa passa, remoção reprova `152 → 151`, acréscimo sem
baseline reprova `152 → 153`. Autoridade de evidências resolvida corretamente em
`src/constants/evidencias.ts`, sem caminho inventado.

**Buraco:** a lista era fixa com 6 caminhos. Existem 64 arquivos de runtime com 40+
linhas de comentário e **60 estavam desprotegidos** — inclusive `emojiRowProcedure.ts`
(300) e `emojiRowContract.ts` (264), os dois mais documentados do projeto, com o dobro
do `Composer.ts`. E `composerCanaryIds.ts` (54), apesar de o canário constar da
proposta de cânone do PR #35.

Ampliada para descoberta automática: todo runtime não-teste com ≥20 comentários entra,
mais cânone nominal sempre. **6 arquivos / 698 linhas → 108 arquivos / 7.468 linhas.**
Quatro invariantes verificados por mutação. `tsc` limpo, 248 arquivos e 3.463 testes.

Commit `c4fd3f2`, fast-forward sobre `a043861`.

### Gate B · Lote 8 (AL) verificado — CLASS-006 NÃO está fechada — 19/08/2026
Lote 8 correto: HEAD `f1f61ea`, 3 arquivos documentais, `main` intocada, e a
ampliação da catraca (`c4fd3f2`) foi integrada por fast-forward.

**Mas medi a CLASS-006 empiricamente** nas 75 competências ativas, níveis 1–5, 120
amostras por par, no HEAD `f1f61ea`: **288 pares medidos, 75 concentrados ≥60% numa
posição, 18 competências afetadas** — o Lote 8 reportou 4. A maioria em **100%**.

Causa no código: `composerCanary.ts` embaralha apenas se o id estiver em
`CLASS_006_FRESH_OPTION_IDS`, allowlist fixa de 25. O resto passa direto.

Dois casos decisivos:
- **`N6.01` está fora da allowlist** e é justamente a competência que originou a
  CLASS-004. Mede 100% na posição 0 nos cinco níveis. O defeito nunca foi corrigido.
- **`N2.06`** foi refutada como falso positivo por "alternar entre níveis". A medição
  mostra posição fixa dentro de cada nível; a criança pratica um nível por vez. A
  refutação estava errada.

Terceira ocorrência do mesmo padrão: W36 (cânone nominal por lista), catraca
documental (6 caminhos à mão) e agora CLASS-006 (allowlist de 25). Duas dessas listas
foram criadas para impedir a falha anterior.

Correção: embaralhar por default com exceção explícita, e o portão passa a ser
**medição, não lista**. Enquanto não fechar, nenhuma medição de aprendizagem é
interpretável.

### CLASS-006 FECHADA — 19/08/2026
A sessão de produção materializou o regression-first vermelho `ac855a1` e ficou sem
contexto antes da correção. Esta sessão executou.

Commit `c4b8c17`. Default invertido para **embaralhar sempre**;
`CLASS_006_ORDEM_SEMANTICA` guarda exceção justificada e **não dispensa medição**.
Única exceção: `N1.05`, alternativas são índices dos dois grupos do palco, medida em
50/50 nos cinco níveis.

**Três defeitos no próprio gate, encontrados ao usá-lo:**
1. helper de identidade só conhecia `value`; `shapecanvas` usa `figura`, e **GE.02
   saía silenciosamente da amostra** — ponto cego dentro do portão anti-ponto-cego;
2. limiar fixo de 60% é severo demais para k=2 (falso positivo em `N1.05/L3` a
   61,7%) e frouxo demais para k=4 (55% passaria sendo o dobro do esperado);
   virou `1/k + 4σ`;
3. o mesmo par gera listas de tamanhos diferentes quando duplicatas colapsam
   (`AL.02/L5` alterna 2 e 4); medir junto sub-representa as últimas posições e
   inventa viés. Medição agrupada por número de alternativas.

Verificado: `tsc` limpo, build verde, **248 arquivos / 3.437 testes**, gate vermelho
por mutação ao desligar o embaralhamento, medição independente com 288 pares e zero
concentração, e `AL.02` — última suspeita — medida com 3.000 amostras por nível em
52,0/48,0 e 48,8/51,2, dentro de variação normal.

Com isso, acerto volta a significar matemática e misconception volta a significar
concepção errada. Linha de base, telemetria e piloto passam a ser interpretáveis.

### Protocolo de autossuficiência — 19/08/2026
Verificado o HEAD `1088aed`: escopo nos três arquivos autorizados, `main` intocada,
`tsc` limpo, **248 arquivos / 3.437 testes**. A correção de shape foi conferida
independentemente — **171 pares com `uiProps.opcoes`, zero alternativa sem
identidade**. A regressão da Sonda F30 era real e a sessão de produção a tratou
corretamente, sem esconder com rerun. Ela pegou algo que a verificação externa não
tinha pego.

Escrito `00_governance/PROTOCOLO_DE_AUTOSSUFICIENCIA.md` e registradas D068 e D069.

Diagnóstico do ping-pong: o gargalo não é competência da sessão de produção. São
três lacunas de protocolo — a regra de parada por domínio virou freio permanente
depois de oito lotes bem executados; falta autoverificação por **medição** antes de
reportar; e o padrão de lista de inclusão manual se repetiu três vezes.

Quatro regras: medir e não ler; varrer as 90 e não só o domínio do lote; lista de
inclusão é suspeita; e o gate também é código e também erra — o da CLASS-006 nasceu
com três defeitos, todos visíveis ao rodá-lo e nenhum ao lê-lo.

Operação muda de parada por domínio para parada por condição, com checklist de
autoverificação cujo item central é medir a alegação principal do lote. Governança
segue inegociável.

### Gate B · Lote 9 (GE) verificado — CLASS-007 varrida em parte — 19/08/2026
Lote correto: HEAD `173af74`, 1 commit, 1 arquivo, +217, `main` intocada. **A parada
foi por condição D069, não por domínio** — o protocolo funcionou na primeira vez em
que foi usado.

A sessão de produção recusou-se a extrapolar prevalência da CLASS-007 sem varredura
global, citando R1/R2. A recusa está certa.

**Varredura da sub-forma de callback morto**, feita aqui: assinatura é primitiva
habilitada com callback no-op, descontando `disabled` literal, que é exibição
legítima. De 11 no-op encontrados, 8 são exibição e **3 são suspeitos**:
`GE.07/PoligonosStage/DragGroup` (é o GAP-048, confirma o método),
**`N2.07/FatoresRetangulosStage/ArrayGrid` — novo e fora do domínio GE**, e
`JourneyScene/onDone`, benigno por não ser affordance de resposta.

O testemunho de N2.07 vem de domínio já auditado no Lote 2. É R2 funcionando.

**Limite declarado:** a CLASS-007 tem uma segunda sub-forma — ação executável que
não condiciona mastery, como o experimento de GE.04 e a transformação de GE.09 — que
não tem assinatura estática. Exige comparar, por competência, a ação probatória
declarada na ficha contra a regra de mastery efetiva. Método definido, não executado.
A classe permanece ABERTA e não dimensionada.
