from src.classes.ClasseArtigo import Artigo
from src.classes.ClasseAutor import Autor

def runTesteArtigo():
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
                            print(f"{erro.args}")
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
