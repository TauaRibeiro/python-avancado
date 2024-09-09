import time

def cache_expiravel(tempo= 60):
    """Decorador que implementa um cache de armazenamento temporário

    Parâmetros:
        tempo (float, opicional): Tempo em segundos que o cache será mantido, após esse tempo ele é deletado. Padrão é 60 segundos (1 minuto).
    """
    def decorador(funcao):
        tempo_expiracao = time.time() + tempo
        cache = dict()

        def funcao_decorada(*args, **kwargs):
            nonlocal tempo_expiracao, cache

            chave = (args, tuple(kwargs.items()))

            if len(cache) == 0 or time.time() > tempo_expiracao:
                cache.clear()    

                cache[chave] = funcao(*args, **kwargs)

                if time.time() > tempo_expiracao:
                    tempo_expiracao = time.time() + tempo

            elif not chave in cache.keys():
                cache[chave] = funcao(*args, **kwargs)
            

            return cache[chave]
        return funcao_decorada
    return decorador          
            
