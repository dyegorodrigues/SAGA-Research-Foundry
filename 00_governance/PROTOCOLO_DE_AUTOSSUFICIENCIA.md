# Protocolo de Autossuficiência

**Status:** `PROPOSTA` · sujeito a D067 · não altera runtime

Por que o trabalho vem parando a cada domínio, e o que muda para ele seguir sozinho.

## 1. O diagnóstico

Oito lotes do Gate B foram executados. Em todos, a sessão de produção fez o trabalho
corretamente e parou. Em vários, uma verificação externa encontrou algo que ela não
tinha visto. O ciclo virou: executa → para → verificação externa acha algo → novo
comando → executa.

O gargalo **não é competência**. É que três coisas ficaram fora do protocolo dela.

### 1.1 A regra de parada virou freio permanente

`PARE ao terminar o domínio` foi escrita quando o método era novo e não havia
histórico. Depois de oito lotes com escopo respeitado, `AUDIT-ONLY` obedecido e
governança intacta, ela deixou de proteger e passou a custar uma rodada por domínio.

### 1.2 Falta autoverificação antes de reportar

Toda rodada externa repetiu os mesmos quatro passos: conferir escopo do diff,
conferir `main`, conferir recibo contra o SHA real, e **medir a alegação**. Os três
primeiros a sessão já faz. O quarto é o que produziu quase todos os achados.

### 1.3 O padrão que se repetiu três vezes

| Ocorrência | Lista | O que escapou |
|---|---|---|
| W36 | cânone nominal por lista | `ficha_runtime_map.cjs` comprimido |
| Catraca documental | 6 caminhos à mão | 60 de 64 arquivos |
| CLASS-006 | allowlist de 25 ids | 18 competências |

Duas dessas listas nasceram para impedir a falha anterior.

## 2. As quatro regras

### R1 — Medir, não ler

> Nenhuma classe é declarada fechada por leitura de código. Fecha por **medição
> executada**, sobre todas as competências ativas, com amostra e limiar declarados.

Ler o código diz o que ele *pretende* fazer. Medir diz o que ele *faz*. Toda vez que
a leitura e a medição divergiram neste projeto, a medição estava certa.

### R2 — Varrer o repositório inteiro, não o domínio do lote

> Achado que possa existir fora do domínio corrente é **varrido em todas as 90**
> antes de ser dimensionado. O lote descobre; a varredura mede.

Foi assim que a conformance ficha↔DAG fechou em 10 casos com `GM.04` aparecendo
antes do lote de GM, e que os 18 geradores com `lvl` ignorado apareceram antes do
lote de N3.

### R3 — Lista de inclusão é suspeita até prova em contrário

> Portão de invariante não usa lista de **inclusão** escrita à mão. Usa descoberta
> ou medição. Lista, quando existir, é de **exceção** explícita, justificada, e que
> **não dispensa a medição**.

Esquecer de incluir abre buraco silencioso. Esquecer de excluir produz teste
vermelho. A assimetria é o ponto.

### R4 — O gate também é código, e também erra

> Ao usar um portão novo pela primeira vez contra o produto corrigido, verificar o
> próprio portão: ele mede todos os casos? o limiar faz sentido para a cardinalidade?
> a amostragem é homogênea?

O gate da CLASS-006 nasceu com três defeitos — não media `shapecanvas`, usava limiar
fixo severo para k=2 e frouxo para k=4, e misturava listas de tamanhos diferentes.
Todos apareceram ao rodá-lo, nenhum ao lê-lo.

## 3. O que muda na operação

### 3.1 A parada passa a ser por condição, não por domínio

Segue sozinho pelos domínios restantes. **Para** quando:

- aparecer classe estrutural nova — classe muda o plano e precisa de decisão;
- um gate ficar vermelho e o reparo não couber no escopo `AUDIT-ONLY`;
- a varredura da R2 revelar algo fora do domínio corrente que exija correção;
- surgir divergência entre cânone e runtime que peça julgamento humano, como a
  `DECISAO-001/GM.04`;
- o escopo do diff sair dos arquivos autorizados;
- `main`, PR ou governança forem tocados por qualquer motivo.

Fora disso: fecha o lote, abre o próximo, segue.

### 3.2 Autoverificação obrigatória antes de reportar

Checklist executado pela própria sessão, com resultado no relatório:

1. `git diff --stat` contra o SHA anterior — só os arquivos autorizados;
2. `main` no SHA protegido; PR `open + draft + unmerged`;
3. cada recibo citado confere com o `head_sha` real do run;
4. **medição da alegação principal do lote**, com número, não com adjetivo;
5. se o lote tocou gate: mutação provando que ele reprova quando deve.

O item 4 é o que dispensa a rodada externa.

### 3.3 Relatório em duas camadas

Uma linha de veredito por lote, e o detalhe abaixo. Quem lê decide em cinco
segundos se precisa intervir. Hoje o relatório é uniforme e obriga a ler tudo.

## 4. O que continua inegociável

Nada aqui afrouxa governança. Continuam valendo: `main` intocada, PR `draft`, sem
`ready`, sem auto-merge, sem merge, `AUDIT-ONLY` no Gate B, promoção atômica com
canário + ledger + Matrix no mesmo SHA, recibo do mesmo SHA, sem reaproveitar
recibo, e Creature Engine fora de escopo.

A mudança é de **cadência e autoverificação**, não de rigor.
