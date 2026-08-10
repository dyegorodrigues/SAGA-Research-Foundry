# Arquitetura mínima

## Não criar
- segundo Curriculum Graph;
- segundo Tutor;
- segundo Composer;
- QI/score global;
- psychometric engine precoce;
- RL de prescrição.

## Possível evolução
LearnerState
├── curriculumProgress
├── dojoTracks
└── practiceReceipts?  # somente se necessário

## Evidence-first
Pergunta inicial:
“Conseguimos observar/derivar isso com `Evidencia` e os contratos existentes?”

Se sim, não criar novo estado.

## Reuse-first
TaskKind → Mechanic → Stage atual? → modo? → composição? → só então Stage novo.
