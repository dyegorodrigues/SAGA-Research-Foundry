# Recovery status — external originals

**Data:** 11/08/2026 · **Status:** ARCHIVE TRANSPORT UNVERIFIED / SOURCE CONTENT RECOVERABLE

## Motivo

A auditoria de 11/08 executou o verificador histórico `python3 tools/verify_integrity.py` e registrou divergência de SHA-256 em:

- `ORIGINALS_2026-08-10.zip.base64.part05`;
- `ORIGINALS_2026-08-10.zip.base64.part08`.

Enquanto essa divergência não for eliminada pela reconstrução a partir do ZIP original ou por outra prova byte-a-byte equivalente, é incorreto declarar o arquivo Base64 como verificado.

## O que foi recuperado fora do archive transport

A File Library de origem ainda contém individualmente os **10 arquivos** listados em `README.md`:

1. `AUDITORIA_ADVERSARIAL_THINKING_ENGINE_PRE_CANONE_v09.md`;
2. `CP_TEMPLATE_THINKING.md`;
3. `CP_TEMPLATE_THINKING_REPO (1).md`;
4. `DOSSE_SAGA_THINKING_ENGINE_INTEGRADO.md`;
5. `DOSSIE_COMPLETO_THINKING_ENGINE_SAGA_2026-08-10.md`;
6. `SAGA_THINKING_ENGINE_PLANO_EXPANSAO_v096.md`;
7. `SAGA_THINKING_v096_VALIDADO_REPO (1).md`;
8. `audit-thinking-reuse (1).ts`;
9. `thinking-extensions (1).ts`;
10. `thinking-integration.test (1).ts`.

Os dois protótipos que a auditoria classificou como perdidos (`thinking-extensions` e `thinking-integration.test`) também estão presentes individualmente. Portanto, **não há perda intelectual irreversível conhecida** neste momento.

## O que isto NÃO prova

Disponibilidade individual dos arquivos não prova que:

- o ZIP reconstruído terá o SHA lógico histórico `01120172a2d7692e93fc932a3bc3c8c5f88277884af3615d2381c358eb25b2a0`;
- metadados/compressão/ordem do ZIP original foram preservados;
- as partes Base64 atuais são byte-a-byte idênticas ao transporte original.

Por isso o status correto do pacote continua sendo **UNVERIFIED** até o verificador dedicado passar contra a referência intencional.

## Mecanismo vigente de integridade

O manifesto histórico `MANIFEST.sha256.json` é um **snapshot do repositório em 10/08** e inclui documentos mutáveis. Ele não deve virar um bloqueio que trate toda edição legítima de documentação como corrupção dos originais.

Para o problema crítico deste pacote, a autoridade mecânica passou a ser:

- `ORIGINALS_MANIFEST.sha256.json` — hashes esperados das 8 partes, SHA-256 lógico do ZIP e os 10 membros esperados;
- `tools/verify_originals_integrity.py` — verifica hashes das partes, validade Base64, SHA do ZIP reconstruído, integridade ZIP/CRC e lista de membros;
- `.github/workflows/integrity.yml` — executa o verificador dedicado automaticamente.

Os hashes esperados de `part05` e `part08` **não foram atualizados para acomodar o conteúdo danificado**. O mecanismo deve continuar vermelho até recuperação real.

## Regra epistemológica

Os `.ts` recuperados continuam sendo **protótipos/spec drafts**. Em particular:

- `thinking-integration.test` contém stubs e asserções locais que não provam integração real no SAGA;
- `audit-thinking-reuse` contém inventário e percentuais hardcoded e não é autoridade sobre reuse real;
- nenhum arquivo desta pasta autoriza patch no runtime produtivo.

## Próximo fechamento

1. localizar/reconstruir o ZIP original ou substituir o mecanismo de transporte por preservação individual com hashes verificáveis;
2. executar `python3 tools/verify_originals_integrity.py`;
3. somente após saída verde voltar a declarar `originals_archive_verified: true`;
4. manter CI automático para impedir nova falsa atestação.
