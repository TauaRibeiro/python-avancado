import csv
import pandas as pd
import numpy as np

def leitura_arquivo():
    dados = []

    with open('vendas loja/informações vendas.csv', mode= 'r', encoding= 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            dados.append(linha)
    
    return dados

def gravacao_arquivo(dados):
    with open('vendas loja/informações vendas.csv', mode= 'w', encoding= 'utf-8') as arquivo:
        gravador = csv.DictWriter(arquivo)

        gravador.writeheader()
        gravador.writerow()
    
dados = leitura_arquivo()

tabela = pd.DataFrame(data= dados)
tabela.sort_values(by= 'idade', ascending= False, inplace= True)
print(tabela)
print()
