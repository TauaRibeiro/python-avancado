import csv

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

def maior_volume(dados):
    vendedor_vendas = dict()

    # A ser feito

dados = [
    {'ID_VENDA': 0, 'Produto': 'Macarrão', 'Quantidade': 10, 'Preço_Unitário': 7.99, 'Data_Venda': '10/05/2003', 'Vendedor': 'Natan'},
    {'ID_VENDA': 1, 'Produto': 'Sabão', 'Quantidade': 6, 'Preço_Unitário': 3.50, 'Data_Venda': '08/04/2005', 'Vendedor': 'João'},
    {'ID_VENDA': 2, 'Produto': 'Óleo', 'Quantidade': 5, 'Preço_Unitário': 8, 'Data_Venda': '10/07/2023', 'Vendedor': 'Marcos'},
    {'ID_VENDA': 3, 'Produto': 'Biscoito', 'Quantidade': 15, 'Preço_Unitário': 7.50, 'Data_Venda': '10/06/2005', 'Vendedor': 'Natan'}
]

gravador_dados(dados)

print(leitura_dados())