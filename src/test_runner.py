import time
from terno_pitagorico import funcs

inputs = [12, 90, 108, 840, 1000, 1001, 30000]
outputs = [funcs[-1](i) for i in inputs]


def timeit(method, *args, **kwargs):
    ts = time.time()
    method(*args)
    return time.time() - ts


def __get_table(**kw):
    name = ' '.join(kw['NOME'].split('_'))
    header = 'BENCHMARK'
    metodo = f'METODO: {name.title()}'
    t = f'{kw["TEMPO"]:.3f}s' if kw['TEMPO'] > 1 else f'{kw["TEMPO"]*1000:.3f}ms'
    tempo = f'TEMPO: {t}'
    sucessos = f'    - PASSED: {kw["SUCESSO"]}'
    inputs_falhados = f'INPUTS QUE FALHARAM: {", ".join(map(str, kw["ERROS"]))}' if kw[
        'FALHA'] else ''
    inputs_falhados = ('{%s}' % inputs_falhados) if inputs_falhados else ''
    falhas = f'    - FAILED: {kw["FALHA"]}{inputs_falhados}'

    texto = [metodo, tempo, sucessos, falhas] + \
        ([inputs_falhados] if inputs_falhados else [])
    i = max(map(len, texto)) + 20

    txt = f'{header:=^{i}}\n'
    txt += '\n'.join(f'||  {t:<{i-6}}' + '||' for t in texto)
    txt += f'\n{"":=^{i}}'

    print(txt)


def run_test(func):
    sucesso = 0
    fails = []
    tempo_total = 0
    for i, o in zip(inputs, outputs):
        tempo_total += timeit(func, i)
        flag = sorted(func(i)) == sorted(o)
        sucesso += flag
        if not flag:
            fails.append(i)
    return __get_table(NOME=func.__name__, TEMPO=tempo_total, SUCESSO=sucesso, FALHA=len(inputs)-sucesso, ERROS=fails)


if __name__ == '__main__':
    print('=' * 25)
    txt = f'|| TOTAL DE TESTES: {len(inputs)}'
    print(f'{txt:^20}  ||')
    print('=' * 25 + '\n\n')

    [run_test(func) for func in funcs]
