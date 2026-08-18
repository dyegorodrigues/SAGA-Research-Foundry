# Princípios Nomeados

Índice da propriedade intelectual pedagógica do SAGA: os princípios estabelecidos
de ciência da aprendizagem que já estão implementados, com o nome técnico e o
lugar onde vivem no código.

Existe porque o método foi construído por dedução e boa intuição, sem os rótulos.
Sem o nome não se pesquisa o estado da arte, não se defende a decisão e não se
conversa com uma pedagoga contratada.

Cada linha também vira uma pergunta auditável em `03_architecture/OBSERVATORIO_E_AUDITORIA.md`.

| Princípio | O que significa | Onde vive |
|---|---|---|
| Aprendizagem por domínio | não avança sem dominar; o tempo varia, o padrão não | `dom`, `MasteryEvidence`, `masteryRule` |
| Domínio multidimensional | domínio ≠ acerto: compreensão + independência + retenção + evidência | `comprehensionStreak`, `independenceStreak`, `retentionPasses`, `evidenciaDaFicha` |
| CPA (concreto→pictórico→abstrato) | manipular, depois desenhar, depois simbolizar; nunca começar pelo símbolo | escada L1→L5 das fichas |
| Andaime desvanecente | o apoio existe e some progressivamente | progressão de níveis, `helpClicks` |
| Automaticidade / fluência | saber não basta; lento consome a memória de trabalho do passo seguinte | `FactStrength`, `ProcStrength`, `rt`, `avgCorrectRtMs`, trilha FD do Dojo |
| Prática de recuperação | puxar da memória ensina mais que reler; testar é estudar | o Dojo |
| Repetição espaçada | revisar quando está quase esquecendo é o que fixa | `reviewForce` (Leitner 1–5), agenda 2→4→7→12→21→45 |
| Intercalação | misturar tipos de problema é pior no treino e melhor no resultado | `mixedChallenge` |
| Dificuldades desejáveis | o esforço certo na hora certa gera aprendizado; facilitar apaga o efeito | regra de domínio; ver D025 (Productive Failure) |
| Grafo de pré-requisitos | conhecimento tem ordem causal; falhar em X pode ser sintoma de não ter Y | `curriculum/grafo_saga.yaml`, `prereqs` |
| Fronteira / ZPD | ensinar onde a criança consegue com apoio, nem abaixo nem acima | `planAula`, `plan.fronteira` |
| Ensino dirigido por erro | o erro é uma teoria errada e consistente, não ruído | ~110 tags em `constants/misconceptions.ts`, `radarEngine` |
| Remediação causal | ao travar, voltar ao pré-requisito que explica o travamento | `rescuePlanner`, `jardimCausalPrescription`, `rescueAttempts` |
| Avaliação formativa | toda interação é medida; não existe "momento da prova" | cada item alimenta `Progress` |
| Teoria da variação | só se entende vendo o que muda e o que não muda entre exemplos | condições da §9 das fichas |
| Transferência | aplicar em contexto nunca visto; único teste honesto de compreensão | `evidenciaDaFicha`, `evidenciasVistas` |
| Carga cognitiva | a tela tem orçamento de atenção; ornamento gasta o orçamento do conceito | gate de onboarding visual, sondas de layout |
| Senso numérico / subitização | reconhecer quantidade sem contar, decompor, estimar | trilhas N1/N2, `TenFrame`, `Grupo`, `NumberBond` |

## Uso

Ao auditar, cada princípio vira pergunta: *o andaime desvanece na velocidade certa?*
*a agenda de espaçamento está sendo respeitada?* *a remediação causal resolve ou repete?*

Sem os nomes, essas perguntas não se formulam.
