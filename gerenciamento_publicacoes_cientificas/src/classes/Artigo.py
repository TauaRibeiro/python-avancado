class Artigo:
    _GERADOR_ID = 1
    lista_artigos = list()
    def __init__(self, titulo, autores, ano_publicacao, palavras_chaves):

        self._titulo = titulo
        self._autores = autores
        self._ano_publicacao = ano_publicacao
        self._palavras_chaves = palavras_chaves

        
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
    

if __name__ == '__main__':
    artigo1 = Artigo("olá mundo", ["Teste 1", "Teste 2"], 2024, ["olá", "mundo"])
    artigo2 = Artigo("olá mundo", ["Teste 1", "Teste 2"], 2024, ["olá", "mundo"])
    artigo3 = Artigo("olá mundo", ["Teste 1", "Teste 2"], 2024, ["olá", "mundo"])

    print(artigo1.__repr__)
    print(artigo2.__repr__)
    print(artigo3.__repr__)