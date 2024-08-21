import re

texto  =  'Contato: email1@dominio.com, email2@outrodominio.com. Pagamentos: R$ 1.200,50, R$ 350,00. Datas: 23/08/2024, 12/05/2023.'


emails = re.findall(r'\w+@\w+\.\w{3}', texto)
pagamentos = re.findall(r'R\$\s?(?:\d{1,3}\.)*\d{1,3},\d{2}', texto)
data = re.findall(r'(\d{2})/(\d{2})/(\d{4})',texto)

print(emails)
print(pagamentos)
print(data)
