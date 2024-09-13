import csv, datetime, re

def leitura_dados():
    dados = list()

    with open('vendas loja/informações vendas.csv', 'r', encoding= 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            dados.append(linha)

    return dados

def gravador_dados(dados):
    with open('vendas loja/informações vendas.csv', 'w', encoding= 'utf-8', newline= '') as arquivo:
        campos = list(dados[0].keys())

        gravador = csv.DictWriter(arquivo, campos)

        gravador.writeheader()
        gravador.writerows(dados)

def intervalo_datas(analise, inicio, fim):
    analise = formatar_data(analise)
    inicio = formatar_data(inicio)
    fim = formatar_data(fim)

    analise = datetime.date(analise[2], analise[1], analise[0])
    inicio = datetime.date(inicio[2], inicio[1], inicio[0])
    fim = datetime.date(fim[2], fim[1], fim[0])

    
    return analise >= inicio and analise <= fim

def formatar_data(data):

    padrao = r'(\d{2})/(\d{2})/(\d{4})'

    nova_data = re.split(padrao, data)

    nova_data.pop()
    nova_data.pop(0)

    for i in range(0,3):
        nova_data[i] = int(nova_data[i])
    
    return nova_data

def maior_volume(dados, data_inicio, data_fim):
    vendedor_vendas = dict()

    maior = list()
    for venda in dados:
        vendedor = venda['Vendedor']
        quantidade = venda['Quantidade']

        data_comparacao = venda['Data_Venda']
        
        if intervalo_datas(data_comparacao, data_inicio, data_fim):
            if not vendedor in vendedor_vendas.keys():
                if len(vendedor_vendas.keys()) == 0:
                    maior.append(vendedor)
                vendedor_vendas[vendedor] = quantidade
            else:
                vendedor_vendas[vendedor] += quantidade

            if vendedor_vendas[vendedor] > vendedor_vendas[maior[0]]:
                maior.clear()
                maior.append(vendedor)
            elif vendedor_vendas[vendedor] == vendedor_vendas[maior[0]] and not vendedor in maior:
                maior.append(vendedor)
    
    return maior if len(maior) > 0 else None

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
    
    return receita

def mais_vendido(dados, data_inicio, data_fim):
    data_inicio = formatar_data(data_inicio)
    data_fim = formatar_data(data_fim)

    produto_mais_vendido = list()

    for venda in dados:
        produto = venda['Produto']
        valor_venda = float(venda['Quantidade'])*float(venda['Preço_Unitário'])

        if len(produto_mais_vendido) == 0:
            produto_mais_vendido.append([produto, valor_venda])
        elif valor_venda > produto_mais_vendido[1]:
            produto_mais_vendido.clear()
            produto_mais_vendido.append([produto, valor_venda])
        else:
            for i in produto_mais_vendido:
                print()
                # A fazer
                # if not produto in i and :

    return produto_mais_vendido

dados = [
    {'ID_VENDA': 0, 'Produto': 'Macarrão', 'Quantidade': 10, 'Preço_Unitário': 7.99, 'Data_Venda': '10/05/2003', 'Vendedor': 'Natan'},
    {'ID_VENDA': 1, 'Produto': 'Sabão', 'Quantidade': 6, 'Preço_Unitário': 3.50, 'Data_Venda': '08/04/2005', 'Vendedor': 'João'},
    {'ID_VENDA': 2, 'Produto': 'Óleo', 'Quantidade': 5, 'Preço_Unitário': 8, 'Data_Venda': '10/07/2023', 'Vendedor': 'Marcos'},
    {'ID_VENDA': 3, 'Produto': 'Biscoito', 'Quantidade': 5, 'Preço_Unitário': 7.50, 'Data_Venda': '10/06/2005', 'Vendedor': 'Natan'}
]

print(receita_total(dados, '10/05/2003', '13/09/2024'))
