def balanceada(expressao):
    pilha = list()
    cont_parenteses = cont_colchetes = cont_chaves = 0

    for elemento in expressao:
        if elemento in '()[]{}':
            pilha.append(elemento)

    for i in range(0,len(pilha)):
        elemento = pilha.pop()
        
        if elemento in '()':
            if elemento == '(' and cont_parenteses == 0:
                return False
            elif elemento == ')':
                cont_parenteses += 1
            else:
                cont_parenteses -= 1

        if elemento in '[]':
            if elemento == '[' and cont_colchetes == 0:
                return False
            elif elemento == ']':
                cont_colchetes += 1
            else:
                cont_colchetes -= 1

        if elemento in '{}':
            if elemento == '{' and cont_chaves == 0:
                return False
            elif elemento == '}':
                cont_chaves += 1
            else:
                cont_chaves -= 1
        
    if cont_parenteses == cont_colchetes == cont_chaves == 0:
        return True
    else:
        return False

try:
    print(balanceada(input('Digite uma expressão: (ex: {[(2+3)*4]/3}*5): ')))
except KeyboardInterrupt:
    print('\nNenhuma expressão foi digitada...')
except Exception.__class__ as erro:
    print('O erro foi -> '+erro)
