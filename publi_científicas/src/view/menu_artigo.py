from src.util.menu import Menu
from src.classes.ClasseArtigo import Artigo
from src.classes.ClasseAutor import Autor

def CadastrarArtigo(novo_artigo: Artigo):
    if Autor.estaVazia():
        print("Não há autores cadastrados...")
        return
    
    if novo_artigo.titulo is None:
        try:
            print("-"*30)
            novo_artigo.titulo = input("Digite o título do artigo: ")
        except ValueError as ve:
            print(ve.args)
            CadastrarArtigo(novo_artigo)

    if novo_artigo.ano_publicacao is None:
        try:
            print("-"*30)
            novo_artigo.ano_publicacao = int(input("Digite o ano de publicação do artigo"))
        except ValueError as ve:
            print(ve.args)
            CadastrarArtigo(novo_artigo)

    if novo_artigo.autores is None:
        menu_autores = Menu([Autor.obterAutores(i) for i in Autor.lista_autores], [], 
                            "Digite os números das opções desejadas ex(1; 1,2,3): ", "",
                            "-", ".",
                            multiplos_argumento= True)
        try:
            novo_artigo.autores = Autor.obterAutores([int(i)-1 for i in menu_autores.input()])
        except ValueError as ve:
            print(ve.args)
            CadastrarArtigo(novo_artigo)

    try:
        print("-"*30)
        novo_artigo.palavras_chave = input("Digite as palavras chaves para o artigo ex(computação, engenharia): ")
    except ValueError as ve:
        print(ve.args)
        CadastrarArtigo(novo_artigo)
    
    Artigo.cadastrarArtigo(novo_artigo)

def ExibirArtigos():
    Artigo.mostrarArtigos()

def PesquisarArtigos():
    if Artigo.estavazio():
        print("Não há artigos cadastrados...")
        return
    
    palavra_chave_pesquisa = input("Digite a palavra chave para a pesquisa: ").lower().strip()
    print("-"*30)

    resultado = list()

    for artigo in Artigo.lista_artigos():
        for palavra_chave in artigo.palavras_chave:
            if palavra_chave is palavra_chave_pesquisa:
                resultado.append(str(artigo))
                break
    
    resultado = ''.join(resultado) if len(resultado) != 0 else "Artigo não encontrado..."

    print(resultado)

def GerarRelatorio():
    pass

def runMenuArtigo():
    menu_artigo = Menu(["Cadastrar artigo", "Exibir artigos", "Pesquisar artigos", "Gerar relatório final"],
                        [CadastrarArtigo, ExibirArtigos, PesquisarArtigos, GerarRelatorio],
                        "Digite o número da opção desejada: ", "MENU DE ARTIGOS", loop= True)

    menu_artigo.exibir_menu()
    menu_artigo.executar_acao()
    pass