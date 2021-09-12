from timeit import timeit
from terno_pitagorico import funcs

inputs = [12, 108, 1000, 1001, 90, 840, 30000]

@timeit
def run_tests(func, **kw):
    [func(input) for input in inputs]


if __name__ == '__main__':
    [run_tests(func, name=func.__name__) for func in funcs]
