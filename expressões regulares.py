import re

texto = 'O número de telefone é 1234-5678'
padrao = r'\d{4}-\d{4}' # Padrão para um número de telefone

numero = re.search(padrao, texto)
print(numero.group()) # Output: 1234-5678