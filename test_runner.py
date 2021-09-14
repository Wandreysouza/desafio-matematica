from timeit import timeit
from terno_pitagorico import funcs

inputs = [12, 90, 108, 840, 1000, 1001, 30000]
outputs = [funcs[-1](i) for i in inputs]


@timeit
def run_tests(func, **kw):
    sucess = 0
    fails = []
    for in_, out in zip(inputs, outputs):
        try:
            sucess += (flag := sorted(out) == sorted(func(in_)))
            assert flag
        except Exception:
            fails.append(in_)
    kw['sucess'] = sucess
    kw['fail'] = len(fails)
    kw['fails'] = fails.copy()
    return kw


if __name__ == '__main__':
    print('=' * 25)
    txt = f'|| TOTAL DE TESTES: {len(inputs)}'
    print(f'{txt:^20}  ||')
    print('=' * 25 + '\n\n')

    [run_tests(func, name=func.__name__) for func in funcs]
    
