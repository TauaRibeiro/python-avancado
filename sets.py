def dif_intersecao(conjuntos):
    novo_conjunto = set()

    for analise in conjuntos:
        adicionar = True

        for conjunto in novo_conjunto:
            if len(analise & conjunto) == 0 or analise.issubset(conjunto):

                adicionar = False

                break
        
        if adicionar:
            novo_conjunto.add(analise)
    
    return novo_conjunto


grupo_conjuntos = set()
conjunto = set()

while True:
    entrada = input('Digite os números que de seja inserir em um conjunto separados por vírgula (ex: 1,2,3,4): ')

    for i in entrada.split(','):
        conjunto.add(int(i))

    grupo_conjuntos.add(frozenset(conjunto.copy()))

    conjunto.clear()

    while True:
        decisao = (input('Deseja continuar? [Sim/Não]: ')).lower()

        if decisao in ['sim', 'não', 'nao', 's', 'n']:
            break

        print('Opção inválida!! Por favor tente novamente...')
    
    if decisao in ['não', 'nao', 'n']:
        break

for i in dif_intersecao(grupo_conjuntos):
    print(i)
    