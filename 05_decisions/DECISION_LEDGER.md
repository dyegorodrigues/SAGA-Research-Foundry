# Decision Ledger — v0.99

| ID | Decisão | Status |
|---|---|---|
| D001 | Thinking como função transversal | KEEP |
| D002 | Content Graph soberano | KEEP |
| D003 | Thinking Graph duro | REJECT |
| D004 | Practice Ontology suave | KEEP |
| D005 | Loop/condição/estado/modularidade separados conceitualmente | KEEP |
| D006 | P0–P4 como estado persistido | MODIFY |
| D007 | Receipts/perfil derivado apenas se necessário | EXPERIMENT |
| D008 | Telemetria bruta extensa | REJECT MVP |
| D009 | Generalizar filosofia `Evidencia` | EXPERIMENT HIGH |
| D010 | Transfer Ladder | KEEP |
| D011 | Bridge Pair + invariantes | KEEP |
| D012 | Delayed transfer probe | KEEP HYPOTHESIS |
| D013 | One Novelty Axis universal | MODIFY |
| D014 | Novelty Budget numérico arbitrário | REJECT |
| D015 | TaskKind ≠ Mechanic ≠ Stage | KEEP |
| D016 | Muitas primitives novas | REJECT |
| D017 | Reuse audit real | KEEP |
| D018 | Probe/Mission/Bridge/Project | KEEP |
| D019 | Teach the Agent | EXPERIMENT |
| D020 | S0–S6 paralelo ao SAGA | REJECT |
| D021 | Fresh item após modelagem | KEEP |
| D022 | Metacognitive Sampling determinístico | KEEP/EXPERIMENT |
| D023 | Fala bruta persistida | REJECT DEFAULT |
| D024 | Spatial thinking transversal | KEEP |
| D025 | Productive Failure | EXPERIMENT SELECTIVE |
| D026 | Programação por sintaxe precoce | REJECT |
| D027 | Programação visual como formalização | KEEP |
| D028 | Robótica obrigatória | REJECT |
| D029 | IA = prompt engineering | REJECT |
| D030 | Runtime LLM soberano | REJECT |
| D031 | Score global/“QI SAGA” | REJECT |
| D032 | RT como Thinking mastery | REJECT |
| D033 | Diagnóstico clínico por gameplay | REJECT |
| D034 | Falsification Gate | KEEP HIGH |
| D035 | Lab como aba agora | REJECT |
| D036 | Percentual semanal rígido | REJECT |
| D037 | AL.02 como anchor de regularidade | KEEP |
| D038 | N2.01 como anchor de representação | KEEP |
| D039 | N1.12 como arena espacial/tracing | EXPERIMENT |
| D040 | Thinking Coverage derivada | KEEP FUTURE |
| D041 | Segundo Composer | REJECT |
| D042 | Segundo Tutor | REJECT |
| D043 | Open problems julgados por LLM para mastery | REJECT |
| D044 | Criteria/constraints evaluation | KEEP |
| D045 | Feature flag/rollback para slice | KEEP |
| D046 | Implementar Thinking agora | REJECT |
| D047 | Analogia estrutural = identidade conceitual | REJECT |
| D048 | `gateEvidenceBeforeAdvance` = Bridge Engine pronto | REJECT |
| D049 | Reuse audit com percentuais hardcoded como autoridade | REJECT |
| D050 | Protótipos TS atuais = código validado | REJECT |
| D051 | Metacognitive Sampling requer LLM | REJECT |
| D052 | Teach Agent requer mini-interpreter geral | REJECT |
| D053 | Idade como gate rígido | REJECT |
| D054 | Foundry como memória persistente de P&D | KEEP |
| D055 | Produção e P&D em repositórios separados | KEEP |
| D056 | Registro Reconciliado de Detalhe v0.98 preserva microdecisões/insights sem promover runtime | KEEP |
| D057 | Recibo de Sessão estruturado (evento de item) | EXPERIMENT |
| D058 | Evento de prescrição do Sensei como observabilidade pura | EXPERIMENT HIGH |
| D059 | Avaliação de aprendizagem fora do motor adaptativo | KEEP |
| D060 | Justificativa oral como anotação escrita do adulto | KEEP |
| D061 | Calibração descritiva de item sem engine psicométrico | KEEP |
| D062 | Personas sintéticas como instrumento de auditoria longitudinal | KEEP |
| D063 | Portão de continuidade por achado aberto, não por razão fixa | EXPERIMENT |
| D064 | Costuras de expansão sem runtime (domínio, ponte, aprendiz único) | KEEP |
| D065 | Naming diferido; SAGA permanece codinome interno | DEFER |
| D066 | `MANIFEST.sha256.json` é snapshot histórico, não gate; vermelho intencional não se conserta | KEEP |
| D067 | Issue #47 é autoridade do pós-90/90; Observatório é subordinado, não fila paralela | KEEP |
| D068 | Portão de invariante não usa lista de inclusão manual; usa descoberta ou medição | KEEP |
| D069 | Parada por condição, não por domínio, com autoverificação obrigatória | EXPERIMENT |

## Reconciliação D057–D065

Frente: `03_architecture/OBSERVATORIO_E_AUDITORIA.md`. Registrada em 18/08/2026,
com a fábrica curricular em W47 e 4 fallbacks restantes.

### D057 · Recibo de Sessão

Instância concreta de D007 (`receipts/perfil derivado apenas se necessário`).

Necessidade demonstrada: `Progress` é fotografia de estado; nenhuma auditoria
longitudinal é derivável de `Evidencia` ou dos contratos atuais.

**Não** contradiz D008 (`telemetria bruta extensa` → REJECT MVP): schema fechado,
dois tipos de evento, sem áudio, sem texto livre da criança, sem localização,
pseudônimo obrigatório. Se o schema crescer por conveniência, D008 volta a valer
e esta decisão é revogada.

### D058 · Evento de prescrição

Não existe hoje em nenhuma forma. Registra a decisão do orquestrador
(escolha, razão, candidatos, estado relevante) sem alterá-la.

Preserva o invariante de que o Sensei é autoridade única de prescrição
(D041, D042) e que IA generativa não é autoridade pedagógica de runtime (D030).

### D059 · Avaliação fora do motor

Estende D034 (`Falsification Gate` → KEEP HIGH) para o eixo longitudinal.
Os 12 gates de `FALSIFICATION_GATES.md` validam a ficha antes da promoção;
D059 valida o efeito depois, na criança.

Guardrails herdados: proibido score global ou composto (D031); RT não eleva
domínio conceitual (D032); idade não é gate (D053).

### D060 · Justificativa oral

Correção de escopo. A proposta original previa gravação de áudio, o que colide
com D023 (`fala bruta persistida` → REJECT DEFAULT).

Vigente: o adulto anota por escrito o que a criança justificou. Nenhum áudio é
capturado ou persistido.

### D061 · Calibração de item

Proporção de acerto no primeiro contato, descritiva, para achar item trivial
(p>0,95) e item quebrado (p<0,30).

Limite explícito: `ARCHITECTURE_MINIMUM.md` proíbe `psychometric engine
precoce` e `RL de prescrição`. p-valor é leitura de dado, não modelo latente.
Nada aqui autoriza IRT, calibração adaptativa ou prescrição aprendida.

### D062 · Personas sintéticas

Estende as simulações longitudinais existentes de teste de invariante para
instrumento de medida.

Limite epistêmico registrado: valida coerência do motor, nunca aprendizagem.
Não pode ser citada como evidência de eficácia pedagógica.

### D063 · Portão de continuidade

A proposta original era razão fixa 3:1 entre ondas e entregas de observatório.
**Retirada** por colidir com D036 (`percentual semanal rígido` → REJECT):
mesma família de arbitrariedade numérica sobre cadência de trabalho.

Vigente: nenhuma onda nova abre com achado de auditoria aberto de severidade
alta. Condição verificável, no formato dos gates existentes.

### D064 · Costuras de expansão

Mantém D046 (`implementar Thinking agora` → REJECT), D026, D027, D028, D029 e
o roadmap R1–R8 de `FUTURE_PROOFING.md`.

Autoriza apenas anotação e neutralidade de domínio, sem consumidor em runtime.
O contrato de ponte declarativo materializa D011 e D037 e respeita D047
(`analogia estrutural ≠ identidade conceitual`).

Gatilho de expansão: evidência de retenção e transferência em criança real,
não calendário.

### D065 · Naming

Evidência: 32 candidatos verificados por RDAP em `.com` e `.com.br`;
31 ocupados. O espaço de palavra curta pronunciável está esgotado.

Pré-requisito para abrir a frente: existir criança fora de casa usando o
produto. Até lá, `SAGA` é codinome interno sem investimento de marca.

### D066 · Manifesto histórico não é gate

Formaliza no Ledger o que `06_research/external_reviews/RECOVERY_STATUS_2026-08-11.md`
já estabelecia, porque a regra estava enterrada num documento de recuperação e uma
sessão posterior a violou justamente por não encontrá-la.

Vigente:

- `MANIFEST.sha256.json` é snapshot do repositório em 10/08/2026. Contém documentos
  mutáveis. **Não é portão** e não deve ser ressincronizado para "ficar verde".
- A autoridade mecânica de integridade é `ORIGINALS_MANIFEST.sha256.json` +
  `tools/verify_originals_integrity.py`, executados por `.github/workflows/integrity.yml`.
  O escopo estreito é correto: git já protege conteúdo de texto versionado; o pacote
  Base64 reconstruído é a única coisa que git não protege.
- Os hashes de `ORIGINALS_*.base64.part05` e `part08` permanecem vermelhos por decisão.
  Só mudam com recuperação real do conteúdo, nunca para acomodar dano — Issue #1.
- `tools/verify_integrity.py` roda somente sob pedido humano, sobre um snapshot
  histórico. Saída vermelha nele é o comportamento esperado e não indica corrupção.

Precedente: em 18/08/2026 uma sessão leu o vermelho como bug, classificou-o como
"gate falhando há sete dias" e atualizou o manifesto para sete arquivos. A alteração
foi revertida e o arquivo conferido contra `4b89c51`. `part05`/`part08` não foram
atingidos. O incidente fica registrado porque o modo de falha é atraente: um
verificador vermelho convida à correção, e aqui corrigir é o erro.

### D067 · Issue #47 é a autoridade do pós-90/90

A frente Observatório (D057–D065) foi registrada em 18/08. A Issue #47 do SAGA
— *Integração Sistêmica e Child-Ready* — foi aberta em 17/08, é mais completa e
vive no repositório de produção.

Sobreposição material identificada: evento de prescrição ≡ Gate D (decision trace),
Recibo de Sessão ≡ Gate E (telemetria), personas sintéticas ≡ Gate G (Aprendiz
Simulado), criança sozinha ≡ Gate J (piloto silencioso), auditorias A2/A3 ≡ Gate B.

Vigente: **#47 vence em qualquer divergência.** O Observatório passa a ser material
de apoio das gates de #47 e não abre fila concorrente. Isso cumpre a própria §15 de
#47, que proíbe paralelismo que crie duas autoridades.

Contribuição que permanece exclusiva desta frente: **medição de aprendizagem fora
do motor adaptativo** — linha de base, pós-teste, retenção atrasada, transferência,
prova de papel e justificativa anotada. #47 mede usabilidade, coerência longitudinal
e observabilidade; nenhuma dessas responde se a criança aprendeu.

Restrição temporal registrada: a linha de base é recurso não renovável e precisa ser
coletada **antes** do piloto do Gate J. Depois do primeiro uso sério ela é
irrecuperável e o ganho deixa de ser interpretável.

### D068 · Lista de inclusão manual não sustenta invariante

Três ocorrências do mesmo modo de falha: cânone nominal por lista na W36,
catraca documental com seis caminhos escritos à mão e allowlist de vinte e cinco
ids na CLASS-006. Duas delas foram criadas para impedir a falha anterior.

Vigente: portão de invariante estrutural usa **descoberta** ou **medição**. Lista,
quando existir, é de **exceção** — explícita, justificada, e que não dispensa a
medição. A assimetria é o ponto: esquecer de incluir abre buraco silencioso;
esquecer de excluir produz teste vermelho.

Corolário registrado em R4 do protocolo: o portão também é código e também erra.
O gate da CLASS-006 nasceu com três defeitos, todos visíveis ao rodá-lo e nenhum
ao lê-lo.

### D069 · Parada por condição, não por domínio

`PARE ao terminar o domínio` protegia quando o método era novo. Depois de oito
lotes com escopo respeitado e governança intacta, passou a custar uma rodada por
domínio sem reduzir risco.

Vigente: a sessão segue pelos domínios restantes e para por **condição** — classe
estrutural nova, gate vermelho fora do escopo `AUDIT-ONLY`, achado transversal que
exija correção, divergência que peça julgamento humano, escopo de diff fora do
autorizado, ou qualquer toque em `main`, PR ou governança.

Acompanha autoverificação obrigatória antes de reportar, cujo item central é
**medir a alegação principal do lote**. Os outros itens a sessão já fazia; foi a
ausência da medição que produziu quase todos os achados externos.

`EXPERIMENT` e não `KEEP`: se um lote fechar com achado que a autoverificação
deveria ter pego, a parada por domínio volta.
