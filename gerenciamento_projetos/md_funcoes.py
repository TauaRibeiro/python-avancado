import re, datetime, json

'''
TODO
- Finalizar a função de atualizar status
- Criar uma função para procurar um determinado projeto baseado no nome ou id, talvez usar decorador para isso já que vou aplicar em funções.
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
    with open('gerenciamento_projetos/informações projetos.json', 'w', encoding= 'utf-8') as arquivo:
        json.dump(dados, arquivo, indent= 4)


def atualizar_status(dados) -> dict:
    print('='*30)
    print('Para qual status deseja atualizar ?')
    print('-'*30)
    print('1- Em andamento\n',
          '2- Concluído\n',
          '3- Cancelado')
    print('='*30)
    decisao = int(input('Digite o número da opção desejada'))

    match(decisao):
        case 1:
            print()


dados = ler_dados()