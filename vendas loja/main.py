import modulo_funcoes as md

dados = md.leitura_dados()

while True:
    print('='*40)
    print(f'{"MENU":^40}')
    print('-'*40)
    print('1- Vendedor com maior volume de vendas',
          '\n2- Receita total de cada vendedor',
          '\n3- Produto mais vendido',
          '\n4- Relatório final',
          '\n5- Sair')
    print('-'*40)
    decisao = int(input('Digite o número da opção desejada: '))

    match(decisao):
        case 1:
            # A terminar
            data_inicio = input('Digite a data no formata')
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()
        case 5:
            break
        case _:
            print('Opção inválida...')
        
