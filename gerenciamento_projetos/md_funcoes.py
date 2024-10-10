import re, datetime, json

def arquivo_dinamico(gravacao= False):
    def decorador(funcao):
        def funcao_decorada():
            dados = ler_dados()

            resultado = funcao(dados)

            if gravacao:
                carregar_dados(dados)

            return resultado
        return funcao_decorada
    return decorador


def e_maior(data1: str, data2: str) -> bool:
    if validar_data(data1) and validar_data(data2):
        data1 = re.match(r'(\d+)/(\d+)/(\d+)', data1)
        data2 = re.match(r'(\d+)/(\d+)/(\d+)', data2)

        if int(data1.group(3)) > int(data2.group(3)):
            return True
        elif int(data1.group(3)) == int(data2.group(3)):
            if int(data1.group(2)) > int(data2.group(2)):
                return True
            elif int(data1.group(2)) == int(data2.group(2)):
                if int(data1.group(1)) > int(data2.group(1)):
                    return True
       
        return False
    
    raise ValueError('Data(as) inválidas!!')


def validar_data(data: str) -> bool:
    data = re.match(r'(\d+)/(\d+)/(\d+)', data)

    try:
        dia = int(data.group(1))
        mes = int(data.group(2))
        ano = int(data.group(3))
    except AttributeError:
        return False

    if  1 > mes > 12:
        return False
    
    if ano > datetime.date.today().year:
        return False
    
    if 31 < dia < 1:
        return False
    
    if mes in [1,5,7,8,10,12] and dia <= 31:
        return True
    elif mes in [4,6,9,11] and dia <= 30:
        return True
    else:
        if ano % 400 == 0 and dia <= 29:
            return True
        elif dia <= 28:
            return True
    
    return False


def ler_dados() -> dict:
    try:
        with open('gerenciamento_projetos/informações projetos.json', 'r', encoding= 'utf-8') as arquivo:
            dados = json.load(arquivo)
    except json.JSONDecodeError:
        print('ERRO!! Não foi possível decodificar o arquivo...')

    return dados


def carregar_dados(dados: list[dict]) -> None:
    with open('gerenciamento_projetos/informações projetos.json', 'w', encoding= 'UTF-8') as arquivo:
        json.dump(dados, arquivo, indent= 4)

@arquivo_dinamico(gravacao=True)
def atualizar_status(dados: list[dict]) -> dict:
    while(True):
        print('-'*30)
        achou = False
        id_projeto = int(input('Digite o id do projeto: '))

        for projeto in dados["projetos"]:
            if id_projeto == projeto["id"]:
                achou = True
                break
        
        if achou:
            break

        print('Projeto não encontrado. Por favor tente novamente...')

    while True:
        print('='*30)
        print('Para qual status deseja atualizar ?')
        print('-'*30)
        print('1- Em andamento',
            '\n2- Concluído',
            '\n3- Cancelado')
        print('='*30)
        decisao = int(input('Digite o número da opção desejada: '))

        match(decisao):
            case 1:
                projeto["status"] = 'Em andamento'

                projeto["data_fim"] = None

                break
            case 2:
                projeto["status"] = 'Concluído'

                while True:
                    projeto["data_fim"] = input('Digite a data de termino do projeto (dd/mm/aaaa):')

                    if e_maior(projeto["data_fim"], projeto["data_inicio"]) or projeto["data_fim"] == projeto["data_inicio"]:
                        break
                    
                    print('Data inválida!! Por favor tent novamente...')
                break
            case 3:
                projeto["status"] = 'Cancelado'

                while True:
                    projeto["data_fim"] = input('Digite a data de termino do projeto (dd/mm/aaaa):')

                    if e_maior(projeto["data_fim"], projeto["data_inicio"]) or projeto["data_fim"] == projeto["data_inicio"]:
                        break
                    
                    print('Data inválida!! Por favor tent novamente...')

                break
            case _:
                print('Opção inválida!! Por favor tente novamente...')
    
    print('Status atualizado com sucesso!!')
    return dados

@arquivo_dinamico()
def calcular_horas_projetos(dados: list[dict]) -> dict:
    resultado = dict()

    for projeto in dados["projetos"]:
        resultado[projeto["nome"]] = 0

        for membro in projeto["equipe"]:
            resultado[projeto["nome"]] += membro["horas_trabalhadas"]
    
    return resultado

@arquivo_dinamico()
def calcular_horas_equipe(dados: list[dict]) -> dict:
    resultado = dict()

    for projeto in dados["projetos"]:
        for membro in projeto["equipe"]:
            if membro["nome"] in resultado.keys():
                resultado[membro["nome"]] += membro["horas_trabalhadas"]
            else:
                resultado[membro["nome"]] = membro["horas_trabalhadas"]
    
    return resultado

@arquivo_dinamico()
def maior_orcamento(dados: list[dict]) -> dict:
    maior: dict = None
    for projeto in dados["projetos"]:
        if maior == None or projeto["orcamento"] > maior["orcamento"]:
            maior = projeto.copy()

    return maior    

@arquivo_dinamico()
def maior_quantidade_horas(dados: list[dict]) -> dict:
    maior = dict()

    dados = calcular_horas_projetos()

    for projeto, horas in dados.items():
        if len(maior) == 0 or horas > list(maior.values())[0]:
            maior.clear()
            maior[projeto] = horas
    
    return maior 

@arquivo_dinamico()
def trabalhou_multiplos_projetos(dados: list[dict]) -> list:
    resultado = dict()
    resultado_filtrado = list()

    for projeto in dados["projetos"]:
        for funcionario in projeto["equipe"]:
            if not funcionario["nome"] in list(resultado.keys()):
                resultado[funcionario["nome"]] = 1
            else:
                resultado[funcionario["nome"]] += 1
            
                if resultado[funcionario["nome"]] > 1:
                    resultado_filtrado.append(funcionario["nome"])
    
    return resultado_filtrado

@arquivo_dinamico(gravacao=True)
def cadastrar_projeto(dados: list[dict]) -> None:
    novo_projeto = dict()

    
    while True:
        invalido = False

        novo_projeto["id"] = int(input('Digite o id do projeto: '))
        print('-'*30)
        
        for d in dados["projetos"]:
            if novo_projeto["id"] == int(d["id"]):
                invalido = True
                
                break

        if not invalido:
            break

        print('O id já existe no sistema!! Por favor tente novamente...')

    novo_projeto["nome"] = input('Digite o nome do projeto: ')
    print('-'*30)
    novo_projeto["equipe"] = list()

    integrante = dict()
    while True:
        num_integrantes = int(input('Digite o número de integrantes do projeto: '))

        if num_integrantes > 0:
            break

        print('O projeto deve ter no mínimo um integrante.')

    for n in range(1, num_integrantes+1):
        integrante["nome"] = input(f'Digite o nome do {n}° funcionario: ')
        integrante["cargo"] = input(f'Digite o cargo de \'{integrante["nome"]}\': ')
        integrante["horas_trabalhadas"] = int(input(f'Digite as horas trabalhadas por \'{integrante["nome"]}\': '))
        print('-'*30)

        novo_projeto["equipe"].append(integrante.copy())
        integrante.clear()

    while(True):
        try:
            print('Escolha o status do projeto:')
            print('1- Em andamento',
                    '\n2- Concluído',
                    '\n3- Cancelado')
            print('-'*30)
            escolha = int(input('Digite o número da opção desejada: '))
            print('-'*30)
        except ValueError:
            print('Por favor digite o número de uma das opções (ex: 1): ')
            continue

        match(escolha):
            case 1:
                novo_projeto["status"] = "Em andamento"
                break
            case 2:
                novo_projeto["status"] = "Concluído"
                break
            case 3:
                novo_projeto["status"] = "Cancelado"
                break
            case _:
                print('Escolha inválida! Por favor tente novamente')
    while True:
        try:
            novo_projeto["orcamento"] = float(input("Digite o orçamento do projeto: R$ ").replace(',', '.'))
            print('-'*30)
        except ValueError:
            print('Por favor digite o valor do orçamento (ex: 1300)')
        if novo_projeto["orcamento"] >= 0:
            break

        print('Orçamento inválido! Deve ser um valor positivo...')
            

    while True:
        novo_projeto["data_inicio"] = input("Digite a data de início do projeto (dd/mm/aaaa): ")
        
        if validar_data(novo_projeto["data_inicio"]):
            break

        print('Data inválida! Por favor tente novamente...')

    if novo_projeto["status"] == "Concluído" or novo_projeto["status"] == "Cancelado":
        while True:
            novo_projeto["data_fim"] = input('Digite a data de termino do projeto (dd/mm/aaaa):')

            if e_maior(novo_projeto["data_fim"], novo_projeto["data_inicio"]) or novo_projeto["data_fim"] == novo_projeto["data_inicio"]:
                break
            
            print('Data inválida!! Por favor tent novamente...')
    else:
        novo_projeto["data_fim"] = None
        
    dados["projetos"].append(novo_projeto)

    print('Cadastro realizado com sucesso!!')


if __name__ == '__main__':
    dados = ler_dados()

    print(trabalhou_multiplos_projetos(dados))