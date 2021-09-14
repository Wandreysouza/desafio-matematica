# [Problema](https://exercism.org/tracks/python/exercises/pythagorean-triplet)

O exercício proposto pede uma solução em que se ache todos os tripleto pitagórico {a, b, c} que seguem a regra: `a + b + c = N`. Neste trabalho irei apresentar formas de resolver este problemas e explicar alguns conceitos computacionais que explicam a importância de uma função quadrática para resolve-lo.

### Problema proposto(tradução)

> Um tripleto pitágorico é um conjunto de três números naturais {a, b, c} em que: `a**2 + b**2 = c**2`, tal qual `a < b < c`. Por exemplo: `3^2 + 4^2 = 9 + 16 = 25 = 5^2`
> Dado um número N, encontre todos os tripletos que seguem a seguinte lei: `a + b + c = N`. Por exemplo, com N = 1000, há exatamente um terno pitagórico que satisfaça tal lei: `a + b + c = 1000`: `{200, 375, 425}`

# Definições

## [Terno Pitagórico](https://pt.wikipedia.org/wiki/Terno_pitag%C3%B3rico)

Em matemática, nomeadamente em [teoria dos números](https://pt.wikipedia.org/wiki/Teoria_dos_n%C3%BAmeros), um **terno pitagórico** é formado por três números naturais _a_, _b_ e _c_ tais que *a*²+*b*²=*c*². O nome vem do teorema de Pitágoras que afirma que se as medidas dos lados de um triângulo rectângulo são números inteiros, então são um terno pitagórico. Se (_a_,_b_,_c_) é um terno pitagórico, então (_ka_,_kb_,_kc_) também é um terno pitagórico, para qualquer número natural k. Um **terno pitagórico primitivo** é um terno pitagórico em que os três números são primos entre si. Os primeiros ternos pitagóricos primitivos são (3, 4, 5), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41), (11, 60, 61), (12, 35, 37), (13, 84, 85), (16, 63, 65), (20, 21, 29)...

Os ternos pitagóricos apareceram em problemas na Matemática Babilônia na tabela [Plimpton 322](https://pt.wikipedia.org/wiki/Plimpton_322), escrita no Século XVIII a.C. e, posteriormente, foram estudadas no período grego pelos pitagóricos e por Platão e aparecem de forma explícita na obra de Euclides e nos estudos de Diofanto. Também foi estudada por alguns matemáticos islâmicos e, nesse caso, estavam relacionadas com o Problema dos Números Congruentes, um antigo problema que remonta à época do matemático italiano Leonardo Fibonacci.

O Teorema de Pitágoras (e, portanto, os ternos pitagóricos) é a mais bela jóia da tradição pitagórica. Como lembrança inesquecível da época escolar, ele pertence à base cultural comum da humanidade. O seu estudo introduziu uma radical inflexão intelectual entre a prática empírica e indutiva e a argumentação lógico-dedutiva, tanto no aspecto histórico cultural matemático como no âmbito escolar.

### Algumas regras de definição

O primeiro terno pitagórico é formado pelos números 3, 4 e 5. Estes desempenham um papel importante em todos os ternos pitagóricos. Pois pode-se provar que pela definição ou pela fórmula de Euclides, que num termo pitágorico primitivo:

- exatamente um dos números **a** ou **b** é múltiplo de 3
- exatamente um dos números **a** ou **b** é múltiplo de 4
- exatamente um dos números **a** ou **b** ou **c** é múltiplo de 5

### [Formulas para gerar ternos pitagóricos](https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples)

Há várias formas de se gerar tripletos pitagóricos, tais quais: fórmula de Euclides, metódo fibonacci, progressões de números inteiros e fracionados, método de dickson, através de equações quadráticas, matrizes e transformações lineares, entre outros.
Para este problema em específico usaremos a própria definição de pitágoras(`a² + b² = c²`) e a fórmula fornecida pelo problema(`a + b + c = N`), o que nos levará à uma função quadrática.

#### Fórmula de Euclides

Euclides, em seu livro Elementos, demonstrou que existe uma infinidade de ternos pitagóricos primitivos. Além disso, encontrou uma fórmula que gera todos os ternos pitagóricos primitivos. Dados dois números naturais _m_ > _n_, o terno (_a_,_b_,_c_), onde:

- _a = m² - n²_
- _b = 2mn_
- _c = m² + n²_
  E este terno será primitivo se e só somente se _m_ e _n_ são primos entre si. Ou seja o MDC(_m_, _n_) = 1.

#### Função Quadrática

Este método acrescenta uma varíavel _x_ em _m_ e _n_ de forma em que o par será tratado como uma constante, enquanto o valor de _x_ é variado criará pares que são "descendentes" do par f(0) de _m_ e _n_, desta forma iremos "pular" os ternos e obter apenas aqueles que são originários de f(0). Como exemplo:

- Com _m_ = 5 e _n_ = 2, façamos que _m1_ = _4x + m_, e _n1_ = _x + n_.
- Em seguida substituindo na fórmula original teremos:
  - lado _A = m1² - n²_ = (_4x_ + 5)² - (_x_ + 2)² = **15x² + 36x + 21**
  - lado _B = 2m1n1_ = 2(_4x_ + 5)(_x_ + 2) = **8x² + 26x + 20**
  - lado _C = m² + n²_ = (_4x_ + 5)² + (_x_ + 2)² = **17x² + 44x + 29**

Teremos a seguinte relação para f(x):

| x   | a   | b   | c   | m   | n   |
| --- | --- | --- | --- | --- | --- |
| 0   | 20  | 21  | 29  | 5   | 2   |
| 1   | 54  | 72  | 90  | 9   | 3   |
| 2   | 104 | 153 | 185 | 13  | 4   |
| 3   | 170 | 264 | 314 | 17  | 5   |
| 4   | 252 | 405 | 477 | 21  | 6   |

## [Complexidade de Tempo em Algorítmos](https://pt.wikipedia.org/wiki/Complexidade_de_tempo#:~:text=Em%20ci%C3%AAncia%20da%20computa%C3%A7%C3%A3o%2C%20a,tamanho%20da%20entrada%20do%20problema.&text=A%20quantidade%20de%20tempo%20tomada,m%C3%A1ximo%20de%20um%20fator%20constante.)

Em ciência da computação, a complexidade de tempo de um algoritmo quantifica a porção de tempo tomada por um algoritmo para rodar em função da entrada do problema. A complexidade de tempo de um algoritmo é comumente expressada usando a notação _big O_, que suprime constantes multiplicativas e outros termos de menor ordem. A quantidade de tempo tomada e o número de operações elementares realizadas pelo algoitmo diferem no máximo de um fator constante.

### Tipos de complexidade de tempo comum

- Tempo constante: _O(1)_
- log-logarítmico: _O(log log n)_
- Tempo logarítmico: _O(log n)_
- Tempo linear: _O(n)_
- Tempo quadrático: _O(n²)_
- Tempo cúbico: _O(n³)_

### Tempo linear

Um algoritmo é classificado como O(n) quando seu tempo de execução aumenta de forma linear com o tamanho da entrada. Por exemplo um procdimento que adiciona todos os elementos em uma lista requere tempo proporcional ao tamanho da lista.
Tempo linear é comumente visto como um atributo desejável para um algoritmo. Muitas pesquisas foram investidas na criação de algoritmos exibindo tempos lineares ou melhores.

### Tempo polinomial

Um algoritmo é dito tempo polinomial se o tempo de execução dele é limitado superiormente por uma expressão polinomial do tamanho da entrada pra o algoritmo, _T(n) = O(n^k)_ para algumas constantes _k_. Alguns exemplos de algoritmos em tempo polinomial:

- O algoritmo de ordenação quicksort em n inteiros executa, no máximo, An² operações para algumas constantes A. Assim, é executado em tempo O (n2) e é um algoritmo de tempo polinomial.
- Todas as operações aritméticas básicas (adição, subtração, multiplicação, divisão e comparação) pode ser feito em tempo polinomial.
- Emparelhamento máximo em grafos podem ser encontrados em tempo polinomial.

# Solução

## Definindo uma regra geral para ternos pitagóricos

```python
def is_triplet(a, b, c):
    return a**2 + b **2 == c**2 and a < b < c
```

## Algoritmo em Tempo Cúbico

Este algoritmo irá forçadamente encontrar o valor dos triplos pitagóricos através de uma busca e testagem para cada {a, b, c} satisfazem a condição de _`a + b + c = N`_ e também _`a² + b² = c²`_, esta não é uma forma adequada de resolver este problema visto que haverá muito gasto de recursos de processamento para iterar várias vezes.

```python
def is_triplet(a, b, c): ...
def terno_pitagorico_com_soma(perimetro):
    """este método usará um algoritmo em tempo O(n³) para resolver o problema proposto.

    :param perimetro: int valor da soma dos lados de um triângulo.
    :return: list[list] lista com todos os ternos pitagórico que tem como soma o perimetro designado.

    >>> terno_pitagorico_com_soma(1000)
    [[200, 375, 425]]
    >>> terno_pitagorico_com_soma(90)
    [[9, 40, 41], [15, 36, 39]]
    >>> terno_pitagorico_com_soma(100)
    []
    """

    res = []
    return [[a, b, c] # tempo: O(1)
            for c in range(1, perimetro) # tempo: O(f(n)) = O(n)
            for b in range(1, c) # tempo: O(f(n) * g(n)) = O(n²)
            for a in range(1, b) # tempo: O(f(n) * g(n) * h(n)) = O(n³)
            if is_triplet(a, b, c)
            and a + b + c == perimetro]
```

Este algorítmo será em tempo cúbico pois a equação para _T(n) = n³ + n² + n + 1_.

## Algoritmo em Tempo Quadrático

Este algoritmo irá forçadamente encontrar o valor dos triplos pitagóricos através de uma busca e testagem para cada {a, b, c} que satisfazem o problema, então teremos uma iteração de 5(do primeiro terno pitagórico) até _N_, e uma segunda iteração que irá de 4 até o valor do laço anterior.

```python
def is_triplet(a, b, c): ...
def terno_pitagorico_com_soma(N):
    """este método usará um algoritmo em tempo O(n²) com algumas melhorias no algoritmo para resolver
    o problema proposto.

    :param N: int valor da soma dos lados de um triângulo, também conhecido como perímetro.
    :return: list[list] lista com todos os ternos pitagórico que tem como perímetro valor N

    >>> terno_pitagorico_com_soma(1000)
    [[200, 375, 425]]
    >>> terno_pitagorico_com_soma(90)
    [[9, 40, 41], [15, 36, 39]]
    >>> terno_pitagorico_com_soma(100)
    []
    """
    return [[a, b, c] # tempo: O(1)
            for c in range(5, perimetro//2) # tempo: O(f(n)) = O(n)
            for b in range(4, c) # tempo: O(f(n) * g(n)) = O(n²)
            if (a := perimetro - b - c) + b + c == perimetro
            and is_triplet(a, b, c)]
```

Este será um algoritmo em tempo quadrático pois _T(n) = n² + n + 1_. Este algoritmo tem melhorias em perfomance, pelos seguintes fatores:

- Ele irá iterar baseado na inequação em que _c < perimetro / 2_, sendo _c_ a maior parte do triangulo, este não pode ser maior que sua metade, já que o mesmo será divido em três partes.
- Os valores começam a iterar baseado no primeiro terno pitagórico: {3, 4, 5}, isso nos economiza aproximadamente _2n_ laços necessários para o resultado final.
- Não precisamos iterar uma terceira vez para achar o valor de _a_, já que podemos achar através da fórmula _a = N - b - c_.

## Algoritmo em Tempo Linear

Este por sua vez é o algoritmo final em que aplicaremos uma função quadrática que nos dará um resultado mais rápido e que terá uma perfomance significativa para números grandes.
Primeiramente devemos definir fórmulas para valores de _a_, _b_ e regras para o valor de _c_.

Aplicaremos as seguintes fórmulas:

- _`a² + b² = c²`_
- _`a + b + c = N`_
  Sendo [_{a, b, c}_ ∈ Z*], desenvolvendo estas fórmulas teremos:

### Valores para o lado A

Já que _a_ é a menor parte do triângulo, este deverá ser menor que a terça parte de N, assim poderemos ter 3 valores distintos para os lados de forma que _`a < b < c`_. O valor mínimo de _a_ será dado pela raiz de N, esse valor ainda não tenho uma ideia exata de como chegar à ele, porém creio que esteja relacionado à área de um quadrado, de forma que _a_ não possa ter mesmo valor de _b_, a definição não é clara, porém a aplicação é correta. Portanto:

- _a_ será real se e somente se: _`sqrt(N) < a < N/3`_

### Valores para o lado B

1. Isolando o valor de _c_, teremos: _`c = N - a - b`_
2. Substituindo o valor de _c_ na primeira fórmula, teremos: _`a ² + b² = (N - a - b)²`_
3. Aplicando a distributiva de _`(N - a - b)²`_, teremos: _`a² + b² = N² + a² + b² + 2ab - 2aN - 2bN`_
4. Isolando _b_ e simplificando a fórmula, teremos: _`b = (N² + 2aN) / (2N- 2a)`_
   Portanto iremos calcular valores para o lado B, baseados na fórmula acima.

### Valores para o lado C

Tendo os valores para o lado A e B, achar o valor do lado C será fácil, basta isolarmos o valor de _c_ na fórmula do perímetro, e nós ja a temos na primeira parte do cálculo do lado B. Portanto para calcular _c_, teremos: _`c = N - a - b`_

Com os valores definidos vamos ao algoritmo que irá desempenhar um **tempo linear _O(n)_**

```python
def calcula_b(a, N): return (N**2 + 2*a*N) / (2*n - 2*a)
def calcula_c(a, b, N): return N - a - b

def terno_pitagorico_com_soma(perimetro):
    return [[a, b, c]
            for a in range(int(sqrt(N)), N//3)
            if is_triplet(a, b := calcula_b(a, perimetro), c := calcula_c(a, b, perimetro))]
```

## Resultados para os testes

Rótulos:

1. _n_ é o valor do inserido na função, também conhecido como _input_;
2. _t(n)_ tempo em segundos necessário para rodar a função.

### Tempo Cúbico

| _n_   | t(n)     | Qtd. de Laços |
| ----- | -------- | ------------- |
| 12    | 0,000    | 220           |
| 90    | 0,102    | 117.480       |
| 108   | 0,206    | 204.156       |
| 840   | 92,738   | 98.431.480    |
| 1000  | 157,741  | 166.167.000   |
| 1001  | 161,428  | 166.666.500   |
| 30000 | _indef._ | _indef._      |

### Tempo Quadrático

| _n_   | t(n)    | Qtd. de Laços |
| ----- | ------- | ------------- |
| 12    | 0,000   | 1             |
| 90    | 0,001   | 820           |
| 108   | 0,002   | 108           |
| 840   | 0,093   | 86.320        |
| 1000  | 0,128   | 122.760       |
| 1001  | 0,128   | 122.760       |
| 30000 | 131,955 | 112.432.510   |

### Tempo Linear

| _n_   | t(n)  | Qtd. de Laços |
| ----- | ----- | ------------- |
| 12    | 0,000 | 1             |
| 90    | 0,000 | 21            |
| 108   | 0,000 | 26            |
| 840   | 0,000 | 252           |
| 1000  | 0,000 | 302           |
| 1001  | 0,000 | 302           |
| 30000 | 0,018 | 9827          |

# Referencias

> Todos os links utilizados para desenvolver este projeto estão hyperlinkados à este texto.
