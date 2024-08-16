from bibliotecas import dados

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return f'({self.x}, {self.y})'


    def __add__(self, other):
        return Ponto(self.x + other.x, self.y + other.y)
    

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False


ponto1 = Ponto(dados.ler_real('Digite a coordenada x do ponto 1: '), dados.ler_real('Digite a coordenada y do ponto 1: '))
ponto2 = Ponto(dados.ler_real('Digite a coordenada x do ponto 2: '), dados.ler_real('Digite a coordenada y do ponto 2: '))

print('='*30)
print(f'Ponto 1 - {ponto1}\nPonto 2 - {ponto2}')

print('-'*30)
print(f'A soma desses dois pontos irá gerar {ponto1 + ponto2}')

print('-'*30)
print(f'Os dois pontos são {"iguais" if ponto1 == ponto2 else "diferentes"}')
print('='*30)
