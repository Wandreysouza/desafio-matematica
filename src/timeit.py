import time


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        kw = method(*args, **kw)
        te = time.time()
        name = ' '.join(kw['name'].split('_'))

        header = 'BENCHMARK'
        metodo = f'METODO: {name.capitalize()}'
        t = f'{tt:.3f}s' if (tt := te - ts) > 1 else f'{tt*1000:.3f}ms'
        tempo = f'TEMPO: {t}'
        sucessos = f'    - PASSED: {kw["sucess"]}'
        falhas = f'    - FAILED: {kw["fail"]}'
        inputs_falhados = f'INPUTS QUE FALHARAM: {", ".join(map(str, kw["fails"]))}' if kw[
            'fail'] else ''

        texto = [metodo, tempo, sucessos, falhas] + \
            ([inputs_falhados] if inputs_falhados else [])
        i = max(map(len, texto)) + 20

        txt = f'{header:=^{i}}\n'
        txt += '\n'.join(f'||  {t:<{i-6}}' + '||' for t in texto)
        txt += f'\n{"":=^{i}}'

        print(txt)

        return kw
    return timed
