import md_funcoes as md

while True:
    print('='*30)
    print(f'{"MENU":^30}')
    print('-'*30)
    print('1- Adicionar novo projeto',
            '\n2- Ataulizar status',
            '\n3- Horas totais dos projetos',
            '\n4- Horas totais dos membros',
            '\n5- Relatório final',
            '\n6- Sair')
    print('-'*30)
    escolha = int(input('Digite o número da opção desejada: '))
    print('='*30)
    match(escolha):
        case 1:
            md.cadastrar_projeto()
        case 2:
            md.atualizar_status()
        case 3:
            md.calcular_horas_projetos()
        case 4:
            md.calcular_horas_equipe()
        case 5:
            maior_orcamento: dict = md.maior_orcamento()
            maior_quantidade_horas: dict = md.maior_quantidade_horas()
            print(f'O projeto com maior orçamento é {maior_orcamento["nome"]}. Com R$ {maior_orcamento["orcamento"]}')
            print(f'O projeto com a maior quantidade de horas é {list(maior_quantidade_horas.keys())[0]}. Com',
                  list(maior_quantidade_horas.values())[0])
            # A TERMINAR
            print(f'')
            ...
        case 6:
            break
        case _:
            print('Escolha inválida! Por favor tente novamente...')
