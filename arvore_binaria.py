class No():
    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.esquerda = None
        self.direita = None


class Arvore():
    def __init__(self):
        self.raiz = None


    def inserir(self, valor: int) -> None:
        if self.raiz == None:
            self.raiz = No(valor)
            
            return
        
        self._inserirRecursivo(self.raiz, valor)

    def _inserirRecursivo(self, no: No, valor: int) -> None:
        if no == None:
            return
        
        if valor < no.valor:
            if no.esquerda == None:
                no.esquerda = No(valor)
                
                return
            else:
                self._inserirRecursivo(no.esquerda, valor)

        else: 
            if no.direita == None:
                no.direita = No(valor)
                
                return
            else:
                self._inserirRecursivo(no.direita, valor)

            
    
    def emOrdem(self) -> None:
        if self.raiz == None:
            print('Árvore vazia...')
            
            return
        
        self._emOrdem(self.raiz)

    def _emOrdem(self, no:No) -> None:
        if no == None:
            return
        
        self._emOrdem(no.esquerda)
        print(no.valor)
        self._emOrdem(no.direita)

    
    def excluir(self, valor) -> None:
        if self.raiz is None:
            print('Árvore vazia...')

        self._excluirRecursivo(valor, self.raiz, None)
    
    def _excluirRecursivo(self, valor, no_atual: No, no_anterior: No):
        if no_atual is None:
            return
        
        if valor > no_atual.valor:
            self._excluirRecursivo(valor, no_atual.esquerda, no_atual)
        elif valor < no_atual.valor:
            self._excluirRecursivo(valor, no_atual.direita, no_atual)

        elif no_atual.direita is None and no_atual.esquerda is None:
            if no_anterior.esquerda is no_atual:
                no_anterior.esquerda = None
            else:
                no_anterior.direita = None

        elif not no_atual.direita is None and not no_atual.esquerda is None:
            no_sucessor = no_atual.direita

            print(f'no atual -> {no_atual.valor}\ndireita -> {no_atual.direita.valor}\nesquerda -> {no_atual.esquerda.valor}')

            print(no_sucessor.valor)
            while not no_sucessor.esquerda is None:
                no_sucessor = no_sucessor.esquerda
                print(no_sucessor.valor)
            
            no_sucessor.direita = no_atual.direita if not no_atual.direita is no_sucessor else None
            no_sucessor.esquerda = no_atual.esquerda if not no_atual.esquerda is no_sucessor else None

            if no_anterior.direita is no_atual:
                no_anterior.direita = no_sucessor
            else:
                no_anterior.esquerda = no_sucessor



arvore = Arvore()

arvore.emOrdem()

arvore.inserir(500)
arvore.inserir(0)
arvore.inserir(1000)
arvore.inserir(-100)
arvore.inserir(100)
arvore.inserir(900)
arvore.inserir(1100)
arvore.inserir(-50)
arvore.inserir(-200)
arvore.inserir(50)
arvore.inserir(200)
arvore.inserir(750)
arvore.inserir(950)
arvore.inserir(1050)
arvore.inserir(1150)

arvore.emOrdem()
print('-'*30)
arvore.excluir(0)

# arvore.emOrdem()
