import re

texto  =  'Contato: email1@dominio.com, email2@outrodominio.com. Pagamentos: R$ 1.200,50, R$ 350,00. Datas: 23/08/2024, 12/05/2023.'


emails = re.findall(r'\w+@\w+\.\w{3}', texto)
pagamentos = re.findall(r'R\$\s?((?:\d{1,3}\.)*\d{1,3}),(\d{2})', texto)
datas = re.findall(r'(\d{2})/(\d{2})/(\d{4})',texto)

datas_novas = list()
pagamentos_novos = list()

for i in datas:
    datas_novas.append(f'{i[2]}-{i[1]}-{i[0]}')

for i in pagamentos:
    inteiros = i[0]
    decimal = i[1]

    inteiros = inteiros.replace('.', '')

    pagamentos_novos.append(float((inteiros+'.'+decimal)))


print(f'emails = {emails}')
print(f'datas = {datas_novas}')
print(f'valores = {pagamentos_novos}')
