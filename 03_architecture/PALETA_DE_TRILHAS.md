# Paleta de Trilhas — resolução da decisão pendente

**Status:** `PROPOSTA` · não altera runtime · sujeita a D067
**Resolve:** decisão 2 de `AI_Studio_Lab/codex/DESIGN_ESTADO_E_DECISOES.md` §4
**Preserva:** todas as decisões travadas em §1 — cores de operação, regra do símbolo, vermelho reservado

## 1. A promessa era impossível

O mapa promete *"cada ilha tem sua cor"* para 11 trilhas. Isso nunca pôde funcionar,
e as 4 colisões observadas (N7=N1, AL=N6, GE=N5, PE=N2) não foram descuido — foram o
sintoma.

Matizes já ocupados e intocáveis:

| Matiz | Papel |
|---|---|
| 0° | erro |
| 17° | subtração `#C2410C` |
| 142° | acerto |
| 175° | divisão `#0F766E` |
| 221° | adição `#2563EB` |
| 272° | multiplicação `#7E22CE` |

Varrendo os 360° e exigindo separação mínima de cada um deles:

| Separação exigida | Faixas livres |
|---|---|
| ≥40° | **2** — 57–102° e 312–320° |
| ≥30° | **2** — 47–112° e 302–330° |
| ≥25° | **3** — 42–117°, 246–247°, 297–335° |

**Três matizes livres para onze trilhas.** A promessa é aritmeticamente impossível.

## 2. Matiz = família, não trilha

A cor deixa de dizer *qual trilha* e passa a dizer *que tipo de matemática*. Cinco
famílias cabem exatamente nas cinco vagas disponíveis: três matizes livres, o reuso
legítimo das cores de operação, e um neutro.

| Família | Trilhas | Matiz | Origem da vaga |
|---|---|---|---|
| **Quantidade** | N1, N2, N7 | 316° magenta | faixa livre |
| **Operação** | N3, N4 | herda as travadas | N3 é adição/subtração, N4 é multiplicação/divisão — reuso exato, grátis e já testado |
| **Parte** | N5, N6 | 246° índigo | faixa livre estreita |
| **Espaço** | GE, GM | 79° oliva | faixa livre |
| **Raciocínio** | AL, PE | 30° grafite quente | neutro deliberado |

Dentro da família, as trilhas se distinguem por **claridade**, não por matiz. Isso é
ordenado (N1 → N2 → N7 aprofunda), sobrevive a qualquer daltonismo, e a escada de
claridade é a mesma informação que o currículo já carrega.

Duas escolhas semânticas que a restrição tornou possíveis:

- **Operação herdar as cores travadas** faz a cor da trilha e a cor do símbolo
  coincidirem. Uma criança que aprendeu que `+` é azul encontra a trilha de adição
  azul. Não é economia de matiz — é coerência.
- **AL e PE como neutro** porque padrão e incerteza não são trilhas irmãs das outras:
  são modos de pensar sobre número. Neutro diz isso.

## 3. A paleta

Todas ≥ 4,5:1 sobre branco. Mínimo observado 4,91:1.

| Trilha | Família | Hex | Contraste no branco |
|---|---|---|---|
| N1 | Quantidade | `#C4319D` | 4,91:1 |
| N2 | Quantidade | `#9F287F` | 6,81:1 |
| N7 | Quantidade | `#7A1F62` | 9,55:1 |
| N3 | Operação | `#2563EB` | 5,17:1 — travada |
| N4 | Operação | `#7E22CE` | 6,98:1 — travada |
| N5 | Parte | `#292079` | 13,32:1 |
| N6 | Parte | `#1D1655` | 16,18:1 |
| GE | Espaço | `#597B0F` | 4,92:1 |
| GM | Espaço | `#3B520A` | 8,76:1 |
| AL | Raciocínio | `#7B6E60` | 4,95:1 |
| PE | Raciocínio | `#61574C` | 7,06:1 |

Elimina as 4 colisões e a cor solta `#2E8B57` do GM.

## 4. O limite honesto

Simulando deuteranopia e protanopia, o pior par entre **famílias** fica em 1,24:1.
Entre as **11 trilhas** o colapso é total.

**Onze trilhas mutuamente distinguíveis sob daltonismo é impossível** — não com estes
matizes, não com nenhum outro. Com daltonismo em cerca de 1 menino em 12, isto não é
detalhe.

Portanto vale para trilha exatamente a regra que §1 já travou para operação:

> A cor nunca carrega o significado sozinha. O nome e o ícone da trilha são a
> informação; a cor é o reforço que chega mais rápido.

Isso deve ser protegido por teste, no mesmo formato de `coresDeOperacao.test.ts`:
contraste mínimo, ausência de colisão com operação e feedback, e nenhuma trilha
identificada apenas por cor na interface.

## 5. As outras duas decisões de §4

**Dois pretos.** Ficar com `#1e293b` — 351 usos contra 49, custo de migração sete
vezes menor, e o tom ardósia combina com as superfícies frias já em uso. `#111827`
sai.

**Tipografia.** `Nunito` no texto deve ficar: altura-x grande, aberturas abertas e
terminais arredondados ajudam reconhecimento de letra por leitor iniciante — é
escolha técnica, não estética. `Fredoka` no display é a que envelhece mal: é a face
que vai parecer infantil para os 11 anos. Recomendação: manter Nunito, reavaliar
apenas o display quando a faixa superior for testada. Nenhuma pressa — as duas já
estão hospedadas localmente e travadas.
