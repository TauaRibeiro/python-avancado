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
    try:
        decisao = int(input('Digite o número da opção desejada: '))
    except(ValueError):
        print('Por favor digite um número válido da opção desejada (ex: 1,2,3).')

        continue
    except(KeyboardInterrupt):
        break

    print('='*40)

    match(decisao):
        case 1:
            while True:
                data_inicio = input('Digite a data de inicio no formata (dd/mm/aaaa): ')
                data_fim = input('Digite a data final no formato (dd/mm/aaaa): ')

                if md.Validar_Data(data_inicio) and md.Validar_Data(data_fim):
                    break
                
                print('Data de início e/ou fim inválidas, por favor tente novamente...')
                print('-'*40)

            resultado = md.maior_volume(dados, data_inicio, data_fim)
            if resultado == None:
                print('Não foi encontrado nenhuma correspondência....')
            else:
                print('='*40)

                print(f'Foi encontrado {len(resultado.keys())} {"correspondências" if len(resultado.keys()) != 1 else "correspondência"}')

                for vendedor, quantidade in resultado.items():
                    print('-'*40)
                    print(f'VENDEDOR: {vendedor}',
                          f'\nQUANTIDADE: {quantidade}')
                    
        case 2: 
            while True:
                data_inicio = input('Digite a data de inicio no formata (dd/mm/aaaa): ')
                data_fim = input('Digite a data final no formato (dd/mm/aaaa): ')

                if md.Validar_Data(data_inicio) and md.Validar_Data(data_fim):
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

                if md.Validar_Data(data_inicio) and md.Validar_Data(data_fim):
                    break
                
                print('Data de início e/ou fim inválidas, por favor tente novamente...')
                print('-'*40)

            resultado = md.mais_vendido(dados, data_inicio, data_fim)
            if resultado == None:
                print('Não foi encontrado nenhuma correspondência....')
            else:
                print('='*40)

                print(f'Foi encontrado {len(resultado.keys())} {"correspondências" if len(resultado.keys()) != 1 else "correspondência"}')

                for vendedor, quantidade in resultado.items():
                    print('-'*40)
                    print(f'PRODUTO: {vendedor}',
                          f'\nQUANTIDADE: {quantidade}')
        
        case 4:
            while True:
                data_inicio = input('Digite a data de inicio no formata (dd/mm/aaaa): ')
                data_fim = input('Digite a data final no formato (dd/mm/aaaa): ')
                print('-'*40)

                if md.Validar_Data(data_inicio) and md.Validar_Data(data_fim):
                    break
                
                print('Data de início e/ou fim inválidas, por favor tente novamente...')
                print('-'*40)

            maiorVolume = md.maior_volume(dados, data_inicio, data_fim)
            maiorReceita = md.receita_total(dados, data_inicio, data_fim)
            maisVendido = md.mais_vendido(dados, data_inicio, data_fim)

            if maiorVolume != None:
                print(f'{"O vendedor" if len(maiorVolume) == 1 else "Os vendedores"} com maior volume de vendas ',
                    f'{"foi" if len(maiorVolume) == 1 else "foram"}: {list(maiorVolume.keys())}.',
                    f'Que {"vendeu" if len(maiorVolume) == 1 else "venderam"} {list(maiorVolume.values())[0]}',
                    f'{"unidade" if list(maiorVolume.values())[0] == 1 else "unidades"}.')
            else:
                print('Nenhuma correspondência encontrada...')
            print('-'*40)
            if maiorReceita != None:
                print(f'{"O vendedor" if len(maiorReceita) == 1 else "Os vendedores"} com a maior receita ',
                    f'{"foi" if len(maiorReceita) == 1 else "foram"}: {list(maiorReceita.keys())}.',
                    f'Que {"faturou" if len(maiorReceita) == 1 else "faturaram"} R$ {list(maiorReceita.values())[0]:.2f}')
            else:
                print('Nenhuma correspondência...')
            print('-'*40)
            if maisVendido != None:
                print(f'{"O produto mais vendido" if len(maisVendido) == 1 else "Os produtos mais vendidos"}',
                    f'{"foi" if len(maisVendido) == 1 else "foram"}: {list(maisVendido.keys())}.',
                    f'Que {"vendeu" if len(maisVendido) == 1 else "venderam"} {list(maisVendido.values())[0]}',
                    f'{"unidade" if list(maisVendido.values())[0] == 1 else "unidades"}.')
            else:
                print('Nenhuma correspondência encontrada...')
        
        case 5:
            break
        
        case _:
            print('Opção inválida...')
        
