def transformador(funcao_primaria, lista_funcoes=[]):
    def execucao(numero):
        resultado = funcao_primaria

        for funcao in lista_funcoes:
            resultado = funcao(resultado)

        return resultado(numero)
    return execucao


def adicionar_1(numero):
    return numero+1

def multiplicar_2(func):
    return lambda numero : func(numero)*2

def elevar_quadrado(func):
    return lambda numero : func(numero)**2

nova_funcao = transformador(adicionar_1, [multiplicar_2, elevar_quadrado])
resultado = nova_funcao(3)

print(resultado)
