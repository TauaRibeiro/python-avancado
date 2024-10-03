import md_funcoes as md

dados_projeto = md.ler_dados()

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
            ...
        case 2:
            ...
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case 6:
            ...
        case _:
            print('Escolha inválida! Por favor tente novamente...')
