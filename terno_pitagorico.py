"""# [Problema](https://exercism.org/tracks/python/exercises/pythagorean-triplet):
Um tripleto pitágorico é um conjunto de três números naturaisl, {a, b, c} em que:
`a**2 + b**2 = c**2`, tal qual `a < b < c`. Por exemplo: `3^2 + 4^2 = 9 + 16 = 25 = 5^2`

Dado um número N, encontre todos os tripletos que seguem a seguinte lei: `a + b + c = N`

Por exemplo, com N = 1000, há exatamente um terno pitagórico que satisfaça tal lei:
`a + b + c = 1000`: `{200, 375, 425}`
"""

__author__ = 'Emanuel Luis'
__date__ = "12/09/2021"

from math import sqrt


def is_triplet(a: int, b: int, c: int) -> bool:
    """aplica a regra básica de um terno pitagórico:
    > a² + b² = c²
    > a < b < c
    """
    return a**2 + b**2 == c**2 and a < b < c


def convencional(perimetro: int) -> list[list[int]]:
    """Resolução que irá procurar pelo terno pitagórico através de verificações brutas em todos os
    possíveis casos

    ### Como o código funciona?
    O programa irá percorrer todos os valores até N e irá criar combinações de vários triângulos diferentes
    e retornará apenas aqueles que satisfazer as seguintes condições:
    - a² + b² = c²
    - a + b + c = N
    - a < b < c

    Esta função tem algumas melhorias para a perfomance tais qual `perimetro//2` o que diminuirá a quantidade
    de iterações no FOR e a criação da variável `a` a partir da fórmula do perímetro. Porém ainda não é totalmente
    eficaz já que ele fará N/2 iterações, para números muito grandes ele irá demorar para retornar os resultados."""

    return [[a, b, c] for c in range(perimetro//2)
            for b in range(c)
            if (a := perimetro - b - c) + b + c == perimetro
            and is_triplet(a, b, c)]


def funcao_quadratica(N: int) -> list[list[int]]:
    """Esta função seguirá as leis explicadas em `readme.md`.

    O código irá procurar as trincas pitagóricas de forma rápida e que demandará menos processamento que a resolução bruta.
    Para esta resolução seguiremos as seguintes leis:
    - a² + b² = c²
    - a + b + c = N
    Usaremos: a² + b² = (a + b)² - 2ab

    => c = N - b - a ::: da equação 2
    => a² + b² = (N - b - a)² ::: substituindo na equação 1
    => b = (N² - 2Na) / (2N - 2Na) ::: depois de expandir e simplificar toda a equação acima, teremos:
    Sendo sqrt(N) < a < N//3.
    
    A partir disto conseguimos juntar as equação com alguns dos conceitos do `readme.md`
    """
    def calc_b(a): return (N ** 2 - 2 * N * a) // (2 * N - 2 * a)

    return [[a, b, c] for a in range(int(sqrt(N/2)), N//3)
            if is_triplet(a, b := calc_b(a), c := N - a - b)]


funcs = convencional, funcao_quadratica
