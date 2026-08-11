# Deferred Implementation Plan — Thinking Engine

**Status:** `DEFERRED` · **NÃO AUTORIZA IMPLEMENTAÇÃO** · **Foundry pre-canonical**

Este arquivo existe para impedir que o caminho de integração fique escondido em material histórico/ZIP. Ele não muda a decisão vigente de não implementar Thinking durante a fábrica curricular atual.

## Precedência

Antes de qualquer uso futuro:

1. reancorar o SAGA produtivo e seus gates;
2. reler `CURRENT_STATE.yaml`;
3. reler `05_decisions/DECISION_LEDGER.md`;
4. confirmar que a decisão equivalente a “implementar Thinking agora” deixou de ser REJECT por decisão explícita;
5. executar Invariant Impact Review no produto.

Se esses passos não ocorrerem, este documento é somente memória de engenharia.

## Restrições invariantes

- zero segundo Curriculum Graph de unlock;
- zero segundo sistema de mastery;
- Thinking nunca bloqueia/desbloqueia conteúdo;
- RT/velocidade não eleva perfil thinking;
- acerto genérico não prova prática;
- erro motor não vira erro cognitivo;
- item modelado não prova independência;
- Sensei continua autoridade de prescrição estruturada; não criar segundo tutor;
- Composer atual é reutilizado antes de qualquer Composer paralelo;
- primitive nova é último recurso;
- IA generativa não é autoridade pedagógica do runtime;
- Creature Engine é consumidor/skin, nunca autoridade curricular.

## Change proposal D1 — anotar sem comportamento

**Objetivo:** mapear o thinking que já existe no SAGA sem alterar criança, mastery ou prescrição.

Candidato futuro:

- metadata opcional em fichas/contrato irmão;
- prática candidata;
- condições de evidência possíveis;
- âncoras de conteúdo;
- bridge potential apenas para autoria.

**Gate:** feature flag/default off; zero mudança de runtime observável.

## Change proposal D2 — coverage observacional derivada

**Objetivo:** responder “onde o SAGA já mobiliza estas práticas?” sem persistir nova verdade.

- derivar Coverage Thinking de fichas/evidências reais;
- não editar resultado manualmente;
- não transformar coverage em unlock/mastery;
- reuse audit deve consultar inventário real do produto, nunca percentuais hardcoded de protótipo.

**Gate:** projeção pura e reproduzível.

## Change proposal D3 — evidence receipt mínimo

**Objetivo:** provar uma única prática em uma única experiência existente antes de criar qualquer superfície nova.

Candidato histórico preferencial: `AL.02` / padrão / `detectar_regularidade`.

Fluxo candidato:

```text
stage existente
→ AnswerMeta.evidencias observáveis
→ feature flag
→ receipt thinking mínimo
→ state separado de mastery de conteúdo
```

**Não basta:** `success=true`.

**Gate:** condições específicas + scaffold; sem alteração de dom/unlock.

## Change proposal D4 — primeiro Bridge Pair

**Objetivo:** testar transferência próxima, não presumir far transfer.

Requisitos:

- source e target preservam invariantes estruturais;
- superfície realmente muda;
- prática alvo é necessária/observável;
- source mastery de conteúdo não conta como transfer;
- probe posterior é preferível a inferência imediata;
- reutilizar stage/primitive atual antes de criar componente.

**Gate:** testes de invariantes + surface change + separação content/practice.

## Change proposal D5 — proposta tipada ao Sensei

**Objetivo:** permitir que evidence thinking informe uma micro-missão sem criar tutor concorrente.

Contrato candidato mínimo:

```ts
type ThinkingProposal = {
  kind: "probe" | "support" | "bridge"
  contentAnchor: string
  practices: string[]
  reason: string
}
```

O Sensei pode aceitar/rejeitar. Necessidade curricular crítica vence.

**Gate:** Thinking não desvia orçamento de sessão sem política explícita e não bloqueia Jornada.

## Change proposal D6 — superfície visível somente após prova

Somente depois de D1–D5 passarem e houver massa crítica:

- missão contextual / card especial antes de aba própria;
- debugging e representação antes de “curso de programação”;
- programação visual, Maker, robótica/dados/IA são fases posteriores;
- Lab visível só nasce se evidência de uso justificar a superfície.

## Ciclo de vida de evidência candidato

```text
interação observável
→ AnswerMeta/evidência existente
→ filtro motor × cognitivo
→ receipt thinking específico
→ learner state experimental separado
→ coverage derivada
→ proposal tipada
→ Sensei decide a próxima dose
```

Cada seta precisa de teste que prove separação de responsabilidade.

## Gates futuros mínimos

1. `thinking_state_cannot_unlock_or_lock_content`;
2. `motor_error_does_not_emit_misconception`;
3. `modeled_item_cannot_prove_independence`;
4. `success_alone_cannot_raise_practice_profile`;
5. `bridge_pair_preserves_invariants`;
6. `bridge_pair_changes_surface`;
7. `primary_practice_is_observable`;
8. `content_mastery_does_not_imply_transfer`;
9. `speed_does_not_raise_thinking_profile`;
10. `open_problem_has_objective_criteria_when_used_for_evidence`.

Esses nomes vêm de material de proveniência; não assumir que os protótipos `.ts` atuais os testam de verdade. Teste futuro deve chamar implementação real, não stubs que repetem a regra em memória.

## Condições para sair de DEFERRED

Não existe data. Existem condições:

- núcleo matemático no marco explicitamente escolhido pela governança;
- documentação/gates reconciliados;
- reuse audit real;
- pelo menos um Bridge Pair especificado e falsificável;
- evidence conditions observáveis;
- feature flag + rollback;
- simulação longitudinal;
- garantia automática de que Thinking não corrompe conteúdo/mastery;
- decisão explícita no Decision Ledger autorizando vertical slice.

Até lá, **preservar e melhorar este plano é permitido; implementá-lo no SAGA produtivo não é**.
