class Vetor:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vetor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vetor(self.x - other.x, self.y + other.y)

    def __mul__(self, other):
        return Vetor(self.x * other.x, self.y + other.y)
    
    def __div__(self, other):
        return Vetor(self.x / other.x, self.y / self.y)

    def __repr__(self):
        return f'x: {self.x}, y: {self.y}'
    
    def __len__(self):
        return 10
    
    def __call__(self):
        print('Me chamou?')

v1 = Vetor(10, 20)
v2 = Vetor(50, 60)
v3 = v1 + v2

print(len(v3))

v3()
