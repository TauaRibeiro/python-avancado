# a ser melhorado

import time

def tempo_expirar(tempo= 60):
    def cache_expiravel(funcao):
        tempo_expiracao = time.time() + tempo
        cache = None

        def funcao_decorada(*args, **kwargs):
            nonlocal tempo_expiracao, cache

            if cache == None or time.time() > tempo_expiracao:    
                
                cache = funcao(*args, **kwargs)

                if time.time() > tempo_expiracao:
                    tempo_expiracao = time.time() + tempo
            
            return cache
        return funcao_decorada
    return cache_expiravel            
            
@tempo_expirar(5)
def fatorial(numero):
    if numero == 0:
        print("Executando...")
        return 1
    
    return numero*fatorial(numero-1)


print(fatorial(3))
time.sleep(3)

print(fatorial(3))
time.sleep(3)

print(fatorial(3))
time.sleep(3)

