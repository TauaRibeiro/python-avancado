import re, datetime, json

'''
TODO
- Calcule as horas totais trabalhadas por toda a equipe em cada projeto e o total de horas trabalhadas por cada membro individualmente.

- Encontre o projeto com o maior orçamento e o projeto com a maior quantidade de horas totais trabalhadas.

- Gere um relatório final com as seguintes informações:
    O nome do projeto com o maior orçamento.
    O nome do projeto com o maior número de horas totais trabalhadas.
    A lista de membros que trabalharam em mais de um projeto e a quantidade total de horas trabalhadas por eles.
'''
def validar_data(data) -> bool:
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


def carregar_dados(dados) -> None:
    with open('gerenciamento_projetos/informações projetos.json', 'w', encoding= 'UTF-8') as arquivo:
        json.dump(dados, arquivo, indent= 4)


def atualizar_status(dados) -> dict:
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
                break
            case 2:
                projeto["status"] = 'Concluído'
                break
            case 3:
                projeto["status"] = 'Cancelado'
                break
            case _:
                print('Opção inválida!! Por favor tente novamente...')
    
    return dados


def calcular_horas_projetos(dados) -> dict:
    resultado = dict()

    for projeto in dados["projetos"]:
        resultado[projeto["id"]] = 0

        for membro in projeto["equipe"]:
            resultado[projeto["id"]] += membro["horas_trabalhadas"]
    
    return resultado


def calcular_horas_equipe(dados) -> dict:
    resultado = dict()

    for projeto in dados["projetos"]:
        for membro in projeto["equipe"]:
            if membro["nome"] in resultado.keys():
                resultado[membro["nome"]] += membro["horas_trabalhadas"]
            else:
                resultado[membro["nome"]] = membro["horas_trabalhadas"]
    
    return resultado


dados = ler_dados()

print(calcular_horas_equipe(dados))
