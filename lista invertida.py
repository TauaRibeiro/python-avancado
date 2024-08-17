class ListaInvertida:
    def __init__(self, lista):
        self.lista = lista[::]

    def __repr__(self):
        return f'{self.lista}'


    def __getitem__(self, index):
        return self.lista[len(self.lista)-index-1]

    def __len__(self):
        return len(self.lista)

