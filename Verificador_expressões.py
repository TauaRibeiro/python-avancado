# A terminar

def balanceada(expressao):
    pilha = list()

    for elemento in expressao:
        if elemento in '()[]{}':
            pilha.append(elemento)

    print(pilha)


balanceada('(2*3)')