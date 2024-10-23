from datetime import date

'''
Voltar a mexer aqui após ter terminado a classe Autor.
'''
class Artigo:
    _GERADOR_ID = 1
    _lista_artigos = list()


    def __init__(self, titulo: str, autores: list, ano_publicacao: int, palavras_chave: list[str]) -> None:

        self._titulo = titulo
        self._autores = autores
        self._ano_publicacao = ano_publicacao
        self._palavras_chave = palavras_chave

        
        valido = False
        while not valido:
            valido = True
            for artigo in Artigo.lista_artigos:
                if Artigo._GERADOR_ID == artigo.id:
                    valido = False
                    break
            
            if valido:
                self._id = Artigo._GERADOR_ID

            Artigo._GERADOR_ID += 1


    def __repr__(self):
        return f'Id: {self._id},Titulo: {self._titulo}, Autores: {self._autores}, Ano_publicação: {self._ano_publicacao}, palavras chaves: {self._palavras_chaves}'

    # A substituir o campo do autor para suportar o objeto em si
    def __str__(self):
        texto_artigo = []

        texto_artigo.append(f'TÍTULO: {self._titulo}\n{"AUTOR" if len(self._autores) == 1 else "AUTORES"}:\n')
        
        for autor in self._autores:
            texto_artigo.append(f'\tNOME: {autor[0]}\n\tINSTITUIÇÃO: {autor[1]}\n\n')

        texto_artigo.append(f'ANO PUBLICAÇÃO: {self._ano_publicacao}\n{"PALAVRA" if len(self._palavras_chave) == 1 else "PALAVRAS"} CHAVE:')
        
        for palavra_chave in self._palavras_chave:
            texto_artigo.append(f'{palavra_chave}')

            if palavra_chave != self._palavras_chave[-1]:
                texto_artigo.append(', ')

        return ''.join(texto_artigo)


    def setTitulo(self, titulo: str) -> bool:
        if len(titulo) >= 4:
            self._titulo = titulo
            return True

        return False
    
    # A substituir o campo do autor para suportar o objeto em si
    def setAutores(self, autores: list) -> bool:
        if len(autores) == 0:
            return False

        for autor in autores:
            if len(autor[0]) < 3 or len(autor[1]) < 3:
                return False

        self._autores = autores[:]
        return True
    

    def setAnoPublicacao(self, ano: int) -> bool:
        if ano > date.today().year:
            return False
        
        self._ano_publicacao = ano
        return True


    def setPalavrasChave(self, palavras_chave: list[str]) -> bool:
        if len(palavras_chave) == 0:
            return False
        
        for palavra in palavras_chave:
            if len(palavra) < 4:
                return False
            
        self._palavras_chave = palavras_chave[:]
    

    def getTitulo(self) -> str:
        return self._titulo
    
    # A substituir o campo do autor para suportar o objeto em si
    def getAutores(self) -> list:
        return self._autores[:]
    

    def getAnoPublicacao(self) -> int:
        return self._ano_publicacao
    

    def getPalavrasChave(self) -> list[str]:
        return self._palavras_chaves[:]


    @staticmethod
    def cadastrarArtigo(artigo) -> bool:
        if len(artigo._titulo) < 4 or len(artigo._autores) == len(artigo._palavras_chaves) == len(artigo._palavras_chave) == 0:
            return False
        
        for autor in artigo._autores:
            if len(autor[0]) < 3 or len(autor[1]) < 3:
                return False
            
        for palavra_chave in artigo._palavras_chave:
            if len(palavra_chave) < 4:
                return False
        
        Artigo._lista_artigos.append(artigo)

        return True


    @staticmethod
    def mostrarArtigos() -> str:
        if len(Artigo._lista_artigos) == 0:
            return 'Não há artigos cadastrados...'
        
        resultado = []
        for artigo in Artigo._lista_artigos:
            resultado.append(f'{artigo.__str__}\n')

        return ''.join(resultado)

    
    @staticmethod
    def atualizarArtigo(id_artigo_desatualizado: int, artigo_atualizado) -> bool:
        if len(Artigo._lista_artigos) == 0:
            raise RuntimeError('Não há artigos cadastrados...')
        
        if len(artigo_atualizado._titulo) < 4 or len(artigo_atualizado._autores) == len(artigo_atualizado._palavras_chaves) == len(artigo_atualizado._palavras_chave) == 0:
            return False
        
        for autor in artigo_atualizado._autores:
            if len(autor[0]) < 3 or len(autor[1]) < 3:
                return False
            
        for palavra_chave in artigo_atualizado._palavras_chave:
            if len(palavra_chave) < 4:
                return False 
        
        for indice, artigo in enumerate(Artigo._lista_artigos):
            if id_artigo_desatualizado == artigo._id:
                Artigo._lista_artigos[indice] = artigo

                return True
            
        return False




if __name__ == '__main__':
    artigo1 = Artigo("olá mundo", ["Teste 1", "Teste 2"], 2024, ["olá", "mundo"])
    artigo2 = Artigo("olá mundo", ["Teste 1", "Teste 2"], 2024, ["olá", "mundo"])
    artigo3 = Artigo("olá mundo", ["Teste 1", "Teste 2"], 2024, ["olá", "mundo"])

    print(artigo1.__repr__)
    print(artigo2.__repr__)
    print(artigo3.__repr__)
    print(artigo3.__repr__)
