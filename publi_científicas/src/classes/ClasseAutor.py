class Autor:
    _lista_autores = list()

    def __init__(self, nome: str= None, instituicao: str= None) -> None:
        self._nome = nome
        self._instituicao = instituicao


    def __str__(self) -> str:
        return f'\tNOME: {self._nome}\n\tINSTITUIÇÃO: {self._instituicao}\n\n'

    @property
    def lista_autores() -> list:
        return Autor._lista_autores
    
    @lista_autores.setter
    def lista_autores(lista: list) -> None:
        Autor._lista_autores = lista[:]

    @property
    def nome(self) -> str:
        return self._nome


    @property
    def instituicao(self) -> str:
        return self._instituicao


    @nome.setter
    def nome(self, nome: str) -> None:
        if len(nome) >= 3:
            self._nome = nome
        else:
            raise ValueError('Nome possui menos de 3 caracteres')


    @instituicao.setter
    def instituicao(self, instituicao: str) -> None:
        if len(instituicao) >= 3:
            self._instituicao = instituicao
        else:
            raise ValueError('Nome da instituição possui menos de 3 caracteres')


    @staticmethod
    def cadastrarAutor(autor) -> None:
        Autor._lista_autores.append(autor)


    @staticmethod
    def mostrarAutores(autor_procurado= None) -> str:
        if Autor.estaVazia():
            return 'Não há autores cadastrados'
        
        resultado = []

        for autor in Autor._lista_autores:
            if autor_procurado is None or autor is autor_procurado:
                resultado.append(str(autor))
        
        return ''.join(resultado)


    @staticmethod
    def editarAutor(indice_autor: int, autor_editado) -> None:
        if autor_editado._nome == None:
            autor_editado._nome = Autor._lista_autores[indice_autor]._nome

        if autor_editado._instituicao == None:
            autor_editado._instituicao = Autor._lista_autores[indice_autor]._instituicao

        
        Autor._lista_autores[indice_autor] = autor_editado


    @staticmethod
    def estaVazia() -> bool:
        if len(Autor._lista_autores) == 0:
            return True
        return False

    @staticmethod
    def getListaAutores() -> list:
        return Autor._lista_autores    
        
    @staticmethod
    def obterAutores(indices_autores: list[int]) -> list:
        resultado = []

        for indice in indices_autores:
            if not Autor._lista_autores[indice] in resultado:
                try:
                    resultado.append(Autor._lista_autores[indice])
                except IndexError:
                    continue
        
        return resultado