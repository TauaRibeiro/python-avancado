from datetime import date
from Autor import Autor # Passar a nomear os arquivos de classes como classe_<nome classe>

'''
Voltar a mexer aqui após ter terminado a classe Autor.
'''
class Artigo:
    _GERADOR_ID = 1
    _lista_artigos = list()

    def __str__(self) -> str:
        autores = []

        for autor in self._autores:
            autores.append(Autor.mostrarAutores(autor))

        return f'Título artigo: {self._titulo}\nAutores:\n{''.join(autores)}\nAno publicação: {self._ano_publicacao}\nPalavras chave: {self._palavras_chave}\n\n'

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
    autor1 = Autor('Autor 1', 'Instituição 1')
    autor2 = Autor('Autor 2', 'Instituição 2')
    autor3 = Autor('Autor 3', 'Instituição 3')
    autor4 = Autor('Autor 4', 'Instituição 4')

    Autor.cadastrarAutor(autor1)
    Autor.cadastrarAutor(autor2)
    Autor.cadastrarAutor(autor3)
    Autor.cadastrarAutor(autor4)
    while True:

        print('='*30)
        print('1- Cadastrar',
              '\n2- Mostrar artigos',
              '\n3- Atualizar artigos',
              '\n4- Excluir artigo',
              '\n5- Finalizar')
        print('-'*30)
        decisao = int(input('Digite o número da opção desejada: '))
        print('='*30)

        match(decisao):
            case 1:
                novo_artigo = Artigo()
                
                while True:
                    if novo_artigo.titulo is None:
                        try:
                            print('-'*30)
                            novo_artigo.titulo = input('Digite o título do artigo: ')
                        except:
                            print('Título inválido! O título deve conter no mínimo 3 caracteres...')
                            continue
                    
                    if len(novo_artigo._autores) == 0:
                        print('-'*30)
                        for indice, autor in enumerate(Autor._lista_autores):
                            print(f'{indice+1}- {autor.nome}')

                        print('-'*30)
                        decisao = input('Digite os números das opções desejadas ex(1; 1,2,3): ').replace(' ', '').split(',')
                        try:
                            decisao = [int(x)-1 for x in decisao]
                        except Exception as erro:
                            print(f'O erro foi -> {erro.__class__}')
                            continue
                        
                        print(decisao)
                        if len(decisao) == 0:
                            print('O artigo deve ter no mínimo 1 autor!')
                            continue

                        novo_artigo.autores = Autor.obterAutores(decisao)
                    
                    if novo_artigo.ano_publicacao is None:
                        print('-'*30)
                        try:
                            novo_artigo.ano_publicacao = int(input('Digite o ano de publicação do artigo: '))
                        except ValueError as erro:
                            print(erro.__cause__)
                            continue

                    print('-'*30)
                    palavras = input('Digite as palavras chaves para o artigo ex(computação, engenharia, bioquímica): ').replace(' ', '').split(',')
                    
                    if len(palavras) == 0:
                        print('O artigo deve ter no mínimo uma palavra chave.')
                        continue
                    
                    novo_artigo.palavras_chave = palavras
                    break

                Artigo.cadastrarArtigo(novo_artigo) 
            case 2:
                print(Artigo.mostrarArtigos())
            case 3:
                ...
            case 4:
                ...
            case 5:
                break
            case _:
                ...
