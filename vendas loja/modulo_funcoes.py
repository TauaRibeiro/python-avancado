import csv, datetime, re
from collections import OrderedDict as od

def leitura_dados():
    dados = list()

    with open('vendas loja/informações vendas.csv', 'r', encoding= 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            dados.append(linha)

    return dados


def intervalo_datas(analise, inicio, fim):
    analise = formatar_data(analise)
    inicio = formatar_data(inicio)
    fim = formatar_data(fim)

    analise = datetime.date(analise[2], analise[1], analise[0])
    inicio = datetime.date(inicio[2], inicio[1], inicio[0])
    fim = datetime.date(fim[2], fim[1], fim[0])

    
    return analise >= inicio and analise <= fim


def formatar_data(data):

    padrao = r'(\d+)/(\d+)/(\d+)'

    nova_data = re.split(padrao, data)

    nova_data.pop()
    nova_data.pop(0)

    for i in range(0,3):
        nova_data[i] = int(nova_data[i])
    
    return nova_data


def maior_volume(dados, data_inicio, data_fim):
    vendedor_vendas = dict()

    resultado = dict()
    for venda in dados:
        vendedor = venda['Vendedor']
        quantidade = venda['Quantidade']

        data_comparacao = venda['Data_Venda']
        
        if intervalo_datas(data_comparacao, data_inicio, data_fim):
            if not vendedor in vendedor_vendas.keys():
                vendedor_vendas[vendedor] = quantidade
            else:
                vendedor_vendas[vendedor] += quantidade

    for vendedor, quantidade in vendedor_vendas.items():
        quantidades = list(resultado.keys())

        if len(resultado) == 0:
            resultado[vendedor] = quantidade
        elif quantidade >= vendedor_vendas[quantidades[0]]:
            if quantidade > vendedor_vendas[quantidades[0]]:
                resultado.clear()
            resultado[vendedor] = quantidade
    
    return resultado if len(resultado) > 0 else None
    

def receita_total(dados, data_inicio, data_fim):
    data_inicio = formatar_data(data_inicio)
    data_fim = formatar_data(data_fim)

    receita = dict()

    for venda in dados:
        vendedor = venda['Vendedor']
        valor_venda = float(venda['Quantidade'])*float(venda['Preço_Unitário'])

        if not vendedor in receita.keys():
            receita[vendedor] = valor_venda
        else:
            receita[vendedor] += valor_venda
    
    return receita if len(receita) > 0 else None


def mais_vendido(dados, data_inicio, data_fim):
    data_inicio = formatar_data(data_inicio)
    data_fim = formatar_data(data_fim)

    numero_vendas = dict()
    resultado = dict()

    for venda in dados:
        produto = venda['Produto']
        quantidade = venda['Quantidade']

        if produto in numero_vendas.keys():
            numero_vendas[produto] += quantidade
        else:
            numero_vendas[produto] = quantidade

    for produto, quantidade in numero_vendas.items():
        chaveReferencia = list(resultado.keys())

        if len(resultado) == 0:
            resultado[produto] = quantidade
        elif quantidade >= numero_vendas[chaveReferencia[0]] and not produto in resultado:
            if quantidade > numero_vendas[chaveReferencia[0]]:
                resultado.clear()
            
            resultado[produto] = quantidade

    return resultado if len(resultado) > 0 else None         


def Validar_Data(data):
    data = re.match(r'(\d+)/(\d+)/(\d+)', data)

    try:
        dia = int(data.group(1))
        mes = int(data.group(2))
        ano = int(data.group(3))
    except AttributeError:
        return False

    if  mes < 1 and mes > 12:
        return False
    
    if ano > datetime.date.today().year:
        return False
    
    if dia < 1:
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

