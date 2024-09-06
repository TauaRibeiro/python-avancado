def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def multiplicacao(num1, num2):
    return num1*num2

def escolher_operacao(operacao, lista_operacoes):    
    for tipo_operacao in lista_operacoes:
        if operacao.lower() == tipo_operacao.__name__:
            return tipo_operacao

def aplicar_operacoe(lista_operacoes, num1, num2):
    resultados = list()

    for operacao in lista_operacoes:
        resultados.append(operacao(num1,num2))

    return resultados    

operacoes = [soma, subtracao, multiplicacao]

somar = escolher_operacao('soma', operacoes)
subtrair = escolher_operacao('subtracao', operacoes)
multiplicar = escolher_operacao('multiplicacao', operacoes)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(somar(num1, num2))
print(subtrair(num1, num2))
print(multiplicar(num1, num2))

print(aplicar_operacoe(operacoes, num1, num2))
