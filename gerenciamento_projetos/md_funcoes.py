import re, datetime, json

'''
TODO
- Gere um relatório final com as seguintes informações:
    O nome do projeto com o maior orçamento.
    O nome do projeto com o maior número de horas totais trabalhadas.
    A lista de membros que trabalharam em mais de um projeto e a quantidade total de horas trabalhadas por eles.
'''
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


def calcular_horas_projetos(dados: list[dict]) -> dict:
    resultado = dict()

    for projeto in dados["projetos"]:
        resultado[projeto["nome"]] = 0

        for membro in projeto["equipe"]:
            resultado[projeto["nome"]] += membro["horas_trabalhadas"]
    
    return resultado


def calcular_horas_equipe(dados: list[dict]) -> dict:
    resultado = dict()

    for projeto in dados["projetos"]:
        for membro in projeto["equipe"]:
            if membro["nome"] in resultado.keys():
                resultado[membro["nome"]] += membro["horas_trabalhadas"]
            else:
                resultado[membro["nome"]] = membro["horas_trabalhadas"]
    
    return resultado


def maior_orcamento(dados: list[dict]) -> dict:
    maior: dict = None
    for projeto in dados["projetos"]:
        if maior == None or projeto["orcamento"] > maior["orcamento"]:
            maior = projeto.copy()

    return maior    


def maior_quantidade_horas(dados: list[dict]) -> dict:
    maior = dict()

    dados = calcular_horas_projetos(dados)

    for projeto, horas in dados.items():
        if len(maior) == 0 or horas > list(maior.values())[0]:
            maior.clear()
            maior[projeto] = horas
    
    return maior 


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


def cadastrar_projeto() -> bool:
    novo_projeto = dict()
    
    novo_projeto["id"] = int(input('Digite o id do projeto: '))
    novo_projeto["nome"] = input('Digite o nome do projeto: ')
    novo_projeto["equipe"] = list()

    integrante = dict()
    num_integrantes = int(input('Digite o número de integrantes do projeto: '))
    for n in range(1, num_integrantes+1):
        # A continuar
        integrante["nome"] = input(f'Digite o nome do {n}° funcionario: ')
        integrante["cargo"] = input(f'Digite o cargo de \'{integrante["nome"]}\': ')
        integrante["horas_trabalhadas"] = int(input(f'Digite as horas trabalhadas por \'{integrante["nome"]}\': '))
        print('-'*30)

    while(True):
        print('Escolha o status do projeto:')
        print('1- Em andamento',
                '\n2- Concluído',
                '\n3- Cancelado')
        print('-'*30)
        escolha = input('Digite o número da opção desejada: ')
        

if __name__ == '__main__':
    dados = ler_dados()

    print(trabalhou_multiplos_projetos(dados))
