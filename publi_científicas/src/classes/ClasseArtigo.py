from datetime import date
from .ClasseAutor import Autor


class Artigo:
    _GERADOR_ID = 1
    _lista_artigos = list()

    def __str__(self) -> str:
        autores = []

        for autor in self._autores:
            autores.append(Autor.mostrarAutores(autor))

        return f'Título artigo: {self._titulo}\nAutores:\n{"".join(autores)}\nAno publicação: {self._ano_publicacao}\nPalavras chave: {self._palavras_chave}\n\n'

    def __init__(self, titulo: str= None, autores: list = [], ano_publicacao: int= None, palavras_chave: list[str]= []) -> None:

        self._titulo = titulo
        self._autores = autores
        self._ano_publicacao = ano_publicacao
        self._palavras_chave = palavras_chave

        
        valido = False
        while not valido:
            valido = True
            for artigo in Artigo._lista_artigos:
                if Artigo._GERADOR_ID == artigo._id:
                    valido = False
                    break
            
            if valido:
                self._id = Artigo._GERADOR_ID

            Artigo._GERADOR_ID += 1

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo: str) -> None:
        if len(titulo) < 3:
            raise ValueError('O nome do título não pode ser menor que 3 caracteres...')

        self._titulo = titulo

    @property
    def autores(self) -> list[Autor]:
        return self._autores
    
    @autores.setter
    def autores(self, lista_autores: list[Autor]) -> None:
        if len(lista_autores) == 0:
            raise ValueError('Não é possível cadastrar um artigo sem autores...')
        
        self._autores = lista_autores[:]
        
    @property
    def ano_publicacao(self) -> int:
        return self._ano_publicacao
    
    @ano_publicacao.setter
    def ano_publicacao(self, ano: int) -> None:
        if ano > date.today().year:
            raise ValueError('Não é possível publicar um artigo de um ano que ainda não existe.')
        if ano < 0:
            raise ValueError('Não é possível cadastrar um ano negativo.')

        self._ano_publicacao = ano

    @property
    def palavras_chave(self) -> list[str]:
        return self._palavras_chave
    
    @palavras_chave.setter
    def palavras_chave(self, lista_palavras: list[str]) -> None:
        if len(lista_palavras) == 0:
            raise ValueError('O artigo deve ter no mínimo uma palavra chave')
        
        self._palavras_chave = lista_palavras[:]    

    @property
    def lista_artigos(self) -> list:
        return Artigo._lista_artigos
    
    @lista_artigos.setter
    def lista_artigos(lista_artigos: list) -> None:
        Artigo._lista_artigos = lista_artigos

    @staticmethod
    def cadastrarArtigo(artigo) -> bool:
        Artigo._lista_artigos.append(artigo)

    @staticmethod
    def mostrarArtigos() -> str:
        if len(Artigo._lista_artigos) == 0:
            return 'Não há artigos cadastrados...'
        
        resultado = []
        for artigo in Artigo._lista_artigos:
            resultado.append(f'{str(artigo)}\n')

        return ''.join(resultado)

    @staticmethod
    def estavazio() -> bool:
        return True if len(Artigo._lista_artigos) == 0 else False 

    
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