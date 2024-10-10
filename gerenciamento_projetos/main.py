import md_funcoes as md

while True:
    try:
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
        try:
            escolha = int(input('Digite o número da opção desejada: '))
        except ValueError:
            print('Por favor digite um número da opção desejada (ex: 1)...')
            continue
        print('='*30)
        match(escolha):
            case 1:
                md.cadastrar_projeto()
            case 2:
                md.atualizar_status()
            case 3:
                for projeto, horas in md.calcular_horas_projetos().items():
                    print(f'O projeto {projeto} tem {horas} horas trabalhadas')
            case 4:
                for membro, horas in md.calcular_horas_equipe().items():
                    print(f'O membro {membro} trabalhou {horas} horas.')
                
            case 5:
                maior_orcamento: dict = md.maior_orcamento()
                maior_quantidade_horas: dict = md.maior_quantidade_horas()
                print(f'O projeto com maior orçamento é {maior_orcamento["nome"]}. Com R$ {maior_orcamento["orcamento"]}')
                print(f'O projeto com a maior quantidade de horas é {list(maior_quantidade_horas.keys())[0]}. Com',
                    list(maior_quantidade_horas.values())[0], 'horas')
                print(f'Os memmbros que trabalharam em mais de um projeto foram: {md.trabalhou_multiplos_projetos()}')
            case 6:
                break
            case _:
                print('Escolha inválida! Por favor tente novamente...')
    except KeyboardInterrupt:
        break
