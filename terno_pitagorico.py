"""# [Problema](https://exercism.org/tracks/python/exercises/pythagorean-triplet):
Um tripleto pitágorico é um conjunto de três números naturaisl, {a, b, c} em que:
`a**2 + b**2 = c**2`, tal qual `a < b < c`. Por exemplo: `3^2 + 4^2 = 9 + 16 = 25 = 5^2`

Dado um número N, encontre todos os tripletos que seguem a seguinte lei: `a + b + c = N`

Por exemplo, com N = 1000, há exatamente um terno pitagórico que satisfaça tal lei:
`a + b + c = 1000`: `{200, 375, 425}`
"""

from os import system
from time import sleep
__author__ = 'Emanuel Luis'
__date__ = "14/09/2021"

from math import sqrt


def is_triplet(a: int, b: int, c: int) -> bool:
    """aplica a regra básica de um terno pitagórico:
    > a² + b² = c²
    > a < b < c
    """
    return a**2 + b**2 == c**2 and a < b < c


def tempo_quadratico(N: int) -> list[list[int]]:
    """Resolução que irá procurar pelo terno pitagórico através de verificações brutas em todos os
    possíveis casos

    # Como o código funciona?
    O programa irá percorrer todos os valores até N e irá criar combinações de vários triângulos diferentes
    e retornará apenas aqueles que satisfazer as seguintes condições:
    - a² + b² = c²
    - a + b + c = N
    - a < b < c

    Esta função tem algumas melhorias para a perfomance tais qual `perimetro//2` o que diminuirá a quantidade
    de iterações no FOR e a criação da variável `a` a partir da fórmula do perímetro. Porém ainda não é totalmente
    eficaz já que ele fará N/2 iterações, para números muito grandes ele irá demorar para retornar os resultados."""
    return [[a, b, c] for c in range(5, N//2)
            for b in range(4, c)
            if (a := N - b - c) + b + c == N
            and is_triplet(a, b, c)]


def tempo_linear(N: int) -> list[list[int]]:
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
    def calc_c(a, b): return N - a - b

    return [[a, b, c]
            for a in range(int(sqrt(N)), N//3)
            if is_triplet(a, b := calc_b(a), c := calc_c(a, b))]


def tempo_cubico(N: int) -> list[list[int]]:
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
    if N > 500:
        raise ValueError(
            'Valor fora dos limites calculáveis para esta função.')
    return [[a, b, c]  # tempo: O(1)
            for c in range(1, N)  # tempo: O(f(n)) = O(n)
            for b in range(1, c)  # tempo: O(f(n) * g(n)) = O(n²)
            for a in range(1, b)  # tempo: O(f(n) * g(n) * h(n)) = O(n³)
            if is_triplet(a, b, c)
            and a + b + c == N]

# tempo_cubico não será inserido devido à demora para rodar o algoritmo 
funcs = tempo_quadratico, tempo_linear

if __name__ == '__main__':
    system('cls')
    texto = '\nDigite o perimetro do triângulo, ou digite 0 para sair do programa: '
    while True:
        try:
            N = int(input(texto))
        except Exception:
            system('cls')
            continue

        if N == 0:
            break

        try:
            ternos = tempo_linear(N)
        except ValueError:
            print('O input deve ser um número inteiro positivo ou 0.')
        else:
            if ternos:
                print(f'\nTodos os triângulos possíveis para o perímetro {N}:')
                [print(f'a: {a}\tb: {b}\tc: {c}') for a, b, c in ternos]
            else:
                print('Não há ternos para este perímetro')
        sleep(4)
        system('cls')
