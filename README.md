## [Terno Pitagórico](https://pt.wikipedia.org/wiki/Terno_pitag%C3%B3rico)

### Introdução

Na matemática um terno pitagórico é formado por três números naturais _a_, _b_ e _c_ tais que ² + b² = c² sendo < b < c O nome vem do teorema de Pitágoras que se as medidas de um triângulo retângulo são números inteiros, então são um **terno pitagórico**.

### Pré-requisitos e definições

Há mais de 2.000 anos atrás, Euclides estabeleceu que os ternos pitagóricos podem ser gerados pela seguintes leis:

Sendo _m_ e _n_ números inteiros positivos onde m > n > 0.

- a = m² - n²

- b = 2mn
- c = m² + n²

Os inteiros _a_, _b_, _c_ formam um terno pitagórico, pode-se provar que: (m²-n²)² + (2mn)² = (m² + n²)² expandindo ambos os lados. Existe outras fórmulas para [gerar trios](https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples) porém usaremos uma abordagem de equações quadráticas. Dependendo dos valores para _m_ e _n_, os valores podem ser trocados entre _a_ e _b_ pois < b.

### [Problema](https://exercism.org/tracks/python/exercises/pythagorean-triplet)

Um tripleto pitagórico é um conjunto de três números naturais {a, b, c} em que:

- a² + b² = c²

- a < b < c

Por exemplo: 3² + 4² = 9 + 16 = 25 = 5². Dado um número N, encontre todos os tripletos que seguem a regra: a + b + c = N.

Com = 1000, há exatamente um terno pitagórico que satisfaça tal lei: + b + c = 1000, e este terno é 200, 375, 425}

### Resolvendo o problema

Para a resolução, as fórmulas aplicadas serão:

- a² + b² = c²
- a + b + c = N

Sendo a, b, c ∈ Z, desenvolvendo estas fórmulas teremos:

1.  c = N - a - b

2.  a ² + b² = (N - a - c) ²

3.  a² + b² = N² + a² + b² + 2ab - 2aN - 2bN

4.  2bN - 2ab = N² + 2aN

5.  b(2N - 2a) = N² + 2aN

6.  b = (N² + 2aN) / (2N - 2a)

Portanto para calcular os lados do triângulo teremos:

- sqrt(N) < a < N/3
- b = (N² + 2aN) / (2N - 2a)
- c = N - a - c

Com os valores e leis montados podemos seguir para a parte prática, criar um programa que resolva nosso problema de forma genérica e com poucos gastos de recursos.

_Nota: a aplicação deste material será feito em um anexo juntamente de um arquivo que mostrará comparativos entre duas formas de resolver o mesmo problema. Caso queira inspecionar o código antes de rodar, _

### Referencias:

- Codigo e texto traduzido e adaptado de: [https://www.geeksforgeeks.org/pythagorean-triplet-with-given-sum-using-single-loop/](https://www.mathblog.dk/pythagorean-triplets/)
- Problema adaptado de: [https://projecteuler.net/problem=9](https://projecteuler.net/problem=9)
