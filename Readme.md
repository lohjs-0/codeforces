# Desafio Codeforces

> Repositório criado como parte do desafio da mentoria: escolher problemas do Codeforces, resolvê-los com apoio de IA e documentar a jornada de aprendizado.

---

## Problemas Escolhidos

| # | Código | Nome | Dificuldade | Link |
|---|--------|------|-------------|------|
| 1 | 2203B | Beautiful Numbers | 900 | [Acessar](https://codeforces.com/problemset/problem/2203/B) |
| 2 | 2210B | Simply Sitting on Chairs | 1000 | [Acessar](https://codeforces.com/problemset/problem/2210/B) |
| 3 | 2218D | The 67th OEIS Problem | 1100 | [Acessar](https://codeforces.com/problemset/problem/2218/D) |

---

## 🔍 Descrição dos Problemas

### 1. 2203B — Beautiful Numbers

Dado um número inteiro `x`, definimos `F(x)` como a **soma dos dígitos** de `x`. Um número é considerado **bonito** se `F(F(x)) == F(x)`.

Em um movimento, podemos trocar qualquer dígito do número por outro (sem criar zeros à esquerda). O objetivo é encontrar o **mínimo de movimentos** para tornar `x` bonito.

**Exemplo:** `x = 19` → `F(19) = 10`, `F(10) = 1`. Como `F(F(19)) = 1 ≠ 10 = F(19)`, não é bonito. Trocando o `9` por `0`, temos `10` → `F(10) = 1`, que é bonito. Resposta: **1 movimento**.

---

### 2. 2210B — Simply Sitting on Chairs

Temos `n` cadeiras em fila, todas desmarcadas. Recebemos uma permutação `p[1..n]`.

Percorremos as cadeiras da primeira à última:
- Se a cadeira `i` **está marcada**: o jogo termina imediatamente.
- Se **não está marcada**: podemos sentar ou pular.
  - **Sentar**: após sentar, marcamos a cadeira `p[i]` e avançamos.
  - **Pular**: apenas avançamos.

O objetivo é **maximizar o número de cadeiras** em que sentamos.

**Exemplo:** Com `p = [2, 1, 3]`, a melhor estratégia resulta em sentar em 2 cadeiras.

---

### 3. 2218D — The 67th OEIS Problem

Dado `n`, construir um array de `n` inteiros positivos **distintos** `a[1], a[2], ..., a[n]` tal que, para cada `i`, `a[i]` divida a soma `a[1] + a[2] + ... + a[i]`.

**Exemplo:** Para `n = 4`, uma resposta válida é `[2, 1, 3, 6]`:
- `2 | 2` ✓
- `1 | 3` ✓
- `3 | 6` ✓
- `6 | 12` ✓

---

## Estratégia de Resolução

### 2203B — Beautiful Numbers

**Observação chave:** `F(F(x)) == F(x)` significa que `F(x)` é um "ponto fixo" de `F`. Isso só ocorre quando `F(x)` tem **um único dígito** (entre 1 e 9), pois para qualquer número com dois ou mais dígitos, a soma dos dígitos é estritamente menor que ele mesmo.

Portanto, `x` é bonito se e somente se a **soma dos seus dígitos está entre 1 e 9**.

**Estratégia greedy:** Se a soma `S > 9`, precisamos reduzir `S` trocando dígitos por `0` (ou `1` para o primeiro dígito). Para minimizar o número de trocas, ordenamos os dígitos em **ordem decrescente** e aplicamos cada troca enquanto `S > 9`.

### 2210B — Simply Sitting on Chairs

**Observação chave (do editorial oficial):** Para um jogo que termina na cadeira `k`, o máximo de cadeiras em que podemos sentar é:

```
|{ i : 1 ≤ i < k  E  (p[i] ≤ i  OU  p[i] ≥ k) }|
```

- `p[i] ≤ i`: sentar marca cadeira já visitada → sem risco.
- `p[i] ≥ k`: sentar marca cadeira após o fim → sem risco.
- `i < p[i] < k`: sentar poderia impedir o avanço → pular.

**Estratégia:** Iterar `k` de `1` a `n+1`, mantendo dois contadores incrementais (`left_count` e `right_count`) em tempo `O(n)`.

### 2218D — The 67th OEIS Problem

**Observação chave:** `a[i] | S[i]` equivale a `a[i] | S[i-1]` (já que `a[i] | a[i]` sempre). Portanto, cada novo elemento deve **dividir a soma acumulada anterior**.

**Construção elegante:**
- `a[1] = 2`, `a[2] = 1` (casos base).
- Para `i ≥ 3`: `a[i] = S[i-1]` (o próximo elemento é a soma anterior).
  - Isso garante `S[i] = 2 × S[i-1]` e `a[i] | S[i]` ✓.
  - Todos os termos são distintos pois a sequência cresce.

Sequência resultante: `2, 1, 3, 6, 12, 24, 48, ...`

---

## Linguagem Utilizada

**Python 3**

Escolhi Python por:
- **Legibilidade**: código mais próximo do raciocínio matemático.
- **Facilidade de teste**: prototipagem rápida sem compilação.
- **Suporte nativo a big integers**: importante para o problema 2203B, onde `x` pode chegar a `10^18`.
- **Familiaridade**: é a linguagem que tenho mais prática no momento, além do C# e Node.js.

---

## IA Utilizada e Como Ajudou

**IA utilizada: Claude (Anthropic)**

A IA foi essencial em cada etapa, mas sempre como **ferramenta de aprendizado**, não de cópia:

- **Entendimento dos problemas**: me ajudou a traduzir e interpretar os enunciados em inglês, identificando o que cada problema realmente pedia.
- **Identificação de padrões**: para o problema 2203B, a IA apontou que `F(F(x)) == F(x)` implica `F(x)` ser de um único dígito, uma observação que eu poderia ter demorado bastante para perceber.
- **Depuração**: quando minha solução retornava resultados errados (como o bug no 2210B onde `right_count` ficava negativo), a IA me ajudou a rastrear o problema e entender por que a condição devia ser `pos_of[k] < k` e não `<= k`.
- **Verificação de construção**: no 2218D, a IA testou diferentes construções e validou qual sequência satisfazia todas as condições, ajudando a encontrar a solução elegante `[2, 1, 3, 6, 12, ...]`.
- **Revisão do raciocínio**: sempre que eu tinha uma ideia, a IA ajudava a verificar se ela era matematicamente correta antes de implementar.

---

## Dificuldades Encontradas

- **2203B:** Inicialmente errei a verificação de "bonito" — confundi `F(F(S)) == F(S)` (que é sempre verdade!) com `1 ≤ F(x) ≤ 9`. Precisei debugar para perceber que estava verificando uma camada a mais.

- **2210B:** O bug mais sutil: ao atualizar `right_count`, usei `pos_of[k] <= k` quando o correto é `pos_of[k] < k`. O elemento `i = k` recém-adicionado nunca esteve no `right_count` antes, então não pode ser removido no mesmo passo.

- **2218D:** A construção inicial "pegar o menor divisor de S não usado" falhava logo no segundo elemento (após `a[1]=1`, `S=1`, o único divisor `1` já estava ocupado). Demorei para perceber que precisava de uma construção mais inteligente com termos base.

- **Leitura dos enunciados em inglês:** Alguns termos técnicos de competição (como "permutation", "marked", "game ends") exigiram atenção para não interpretar errado.

---

## O Que Aprendi

- **Soma de dígitos como invariante**: propriedades matemáticas simples como "a soma dos dígitos é um ponto fixo de F se e somente se é um único dígito" são poderosas em problemas de teoria dos números.

- **Construções incrementais**: no problema das cadeiras, o truque de fixar o "ponto de término" `k` e calcular o melhor resultado para cada `k` em tempo linear foi uma lição sobre como transformar um problema de otimização em uma varredura eficiente.

- **Algoritmos construtivos**: aprender a construir uma sequência válida passo a passo, garantindo invariantes a cada elemento adicionado, é uma habilidade muito útil para problemas de nível 1100+.

- **Testar casos manualmente**: verificar os exemplos à mão antes de codificar ajudou a pegar bugs cedo.

- **Debugging sistemático**: aprender a rastrear o estado das variáveis (`left_count`, `right_count`) a cada iteração revelou bugs que passariam despercebidos.

---

## Experiência Geral

Foi uma experiência muito mais intensa (e divertida!) do que eu esperava. A competição em programação tem uma lógica própria, os problemas parecem simples, mas escondem pegadinhas matemáticas elegantes.

**O que mais gostei:** O momento "aha!" quando a observação chave se revela. No 2203B, perceber que "bonito" se reduz a "soma dos dígitos é um único dígito" foi satisfatório. No 2218D, descobrir a construção `[2, 1, S, 2S, 4S...]` foi quase artístico.

**O que foi mais difícil:** O debugging dos casos de borda. No 2210B, o bug de `<=` vs `<` era microscópico mas causava resultados completamente errados. Aprendi que em programação competitiva, os detalhes importam muito.

**Sobre usar IA:** A experiência foi de colaboração genuína. A IA não resolveu por mim, ela questionou meu raciocínio, apontou onde eu estava errado e me ajudou a entender o *porquê* das soluções, não apenas o *como*. Isso fez toda a diferença para o aprendizado.

---

## Estrutura do Repositório

```
📦 codeforces-challenge
 ┣ 📜 2203B-beautiful-numbers.py
 ┣ 📜 2210B-simply-sitting-on-chairs.py
 ┣ 📜 2218D-67th-oeis-problem.py
 ┗ 📜 README.md
```

---
