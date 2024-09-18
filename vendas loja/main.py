import modulo_funcoes as md
import re

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
    print('='*40)

    match(decisao):
        case 1:
            while True:
                data_inicio = input('Digite a data de inicio no formata (dd/mm/aaaa): ')
                data_fim = input('Digite a data final no formato (dd/mm/aaaa): ')

                if re.search(r'(\d+)/(\d+)/(\d+)', data_inicio) != None and re.search(r'(\d+)/(\d+)/(\d+)', data_fim) != None:
                    break
                
                print('Data de início e/ou fim inválidas, por favor tente novamente...')
                print('-'*40)

            resultado = md.maior_volume(dados, data_inicio, data_fim)
            if resultado == None:
                print('Não foi encontrado nenhuma correspondência....')
            else:
                print('='*40)

                print(f'Foi encontrado {len(resultado.keys())} {'correspondências' if len(resultado.keys()) != 1 else 'correspondência'}')

                for vendedor, quantidade in resultado.items():
                    print('-'*40)
                    print(f'VENDEDOR: {vendedor}',
                          f'\nQUANTIDADE: {quantidade}')
                    
        case 2: 
            while True:
                data_inicio = input('Digite a data de inicio no formata (dd/mm/aaaa): ')
                data_fim = input('Digite a data final no formato (dd/mm/aaaa): ')

                if re.search(r'(\d+)/(\d+)/(\d+)', data_inicio) != None and re.search(r'(\d+)/(\d+)/(\d+)', data_fim) != None:
                    break
                
                print('Data de início e/ou fim inválidas, por favor tente novamente...')
                print('-'*40)

            resultado = md.receita_total(dados, data_inicio, data_fim)

            if resultado == None:
                print('Não foi encontrado nenhuma correspondência....')
            else:
                print('='*40)

                for vendedor, receita in resultado.items():
                    print('-'*40)
                    print(f'VENDEDOR: {vendedor}',
                          f'\nRECEITA TOTAL: R$ {receita:.2f}')
        case 3:
            while True:
                data_inicio = input('Digite a data de inicio no formata (dd/mm/aaaa): ')
                data_fim = input('Digite a data final no formato (dd/mm/aaaa): ')

                if re.search(r'(\d+)/(\d+)/(\d+)', data_inicio) != None and re.search(r'(\d+)/(\d+)/(\d+)', data_fim) != None:
                    break
                
                print('Data de início e/ou fim inválidas, por favor tente novamente...')
                print('-'*40)

            resultado = md.mais_vendido(dados, data_inicio, data_fim)
            if resultado == None:
                print('Não foi encontrado nenhuma correspondência....')
            else:
                print('='*40)

                print(f'Foi encontrado {len(resultado.keys())} {'correspondências' if len(resultado.keys()) != 1 else 'correspondência'}')

                for vendedor, quantidade in resultado.items():
                    print('-'*40)
                    print(f'PRODUTO: {vendedor}',
                          f'\nQUANTIDADE: {quantidade}')
        case 4:
            print()
        case 5:
            break
        case _:
            print('Opção inválida...')
        
