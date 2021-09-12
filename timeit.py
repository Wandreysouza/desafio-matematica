import time

#Esta função servirá como decorator que irá nos fornecer o tempo decorrido para cada teste!
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        name = ' '.join(kw['name'].split('_'))

        aplicacao = '//    FORMA: {}   //'.format(name.capitalize())
        i = len(aplicacao)

        print('{:=^{i}}'.format('RELATORIO', i=i))
        print(aplicacao)
        print('//    TEMPO: {:<{i}}   //'.format('%.3fms' % (te - ts), i=i-18))
        print('='*i)
        
        print('\n')
        return result
    return timed