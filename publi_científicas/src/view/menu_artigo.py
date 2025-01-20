from src.util.menu import Menu
from src.classes.ClasseArtigo import Artigo, Autor
from src.models.autoresRecorrentes import autoresRecorrentes
from src.models.palavrasChavesRecorrentes import palavrasChavesRecorrentes
from src.models import carregarDados

def CadastrarArtigo(novo_artigo: Artigo|None= None):
    if Autor.estaVazia():
        print("Não há autores cadastrados...")
        return

    if novo_artigo is None:
        novo_artigo = Artigo()

    if novo_artigo.titulo is None:
        try:
            print("-"*30)
            novo_artigo.titulo = input("Digite o título do artigo: ")
        except ValueError as ve:
            print(ve.args)
            CadastrarArtigo(novo_artigo)
            return

    if novo_artigo.ano_publicacao is None:
        try:
            print("-"*30)
            novo_artigo.ano_publicacao = int(input("Digite o ano de publicação do artigo: "))
        except ValueError as ve:
            print(ve.args)
            CadastrarArtigo(novo_artigo)
            return

    if len(novo_artigo.autores) == 0:
        menu_autores = Menu([i.nome for i in Autor.getListaAutores()], [], 
                            "Digite os números das opções desejadas ex(1; 1,2,3): ", "",
                            "~", ".",
                            multiplos_argumento= True)
        menu_autores.exibir_menu()

        try:
            novo_artigo.autores = Autor.obterAutores([int(i)-1 for i in menu_autores.input])
        except ValueError as ve:
            print(ve.args)
            CadastrarArtigo(novo_artigo)
            return

    try:
        print("-"*30)
        novo_artigo.palavras_chave = input("Digite as palavras chaves para o artigo "
        + "ex(computação, engenharia): ").lower().strip().replace(', ', ',').split(',')
    except ValueError as ve:
        print(ve.args)
        CadastrarArtigo(novo_artigo)
        return
    
    Artigo.cadastrarArtigo(novo_artigo)
    carregarDados()

def ExibirArtigos():
    print(Artigo.mostrarArtigos())

def PesquisarArtigos():
    if Artigo.estavazio():
        print("Não há artigos cadastrados...")
        return
    
    palavra_chave_pesquisa = input("Digite a palavra chave para a pesquisa: ").lower().strip()
    print("-"*30)

    resultado = list()
    artigo: Artigo
    for artigo in Artigo.getListaArtigos():

        for palavra_chave in artigo.palavras_chave:
            print(f"Palavra chave: {palavra_chave}")
            if palavra_chave.lower() == palavra_chave_pesquisa:
                resultado.append(str(artigo))
                break
    
    resultado = ''.join(resultado) if len(resultado) != 0 else "Artigo não encontrado..."

    print(resultado)

def GerarRelatorio():
    autores_recorrentes = autoresRecorrentes()
    palavras_recorrentes = palavrasChavesRecorrentes()

    print(f"{'Foi publicado' if len(Artigo.getListaArtigos()) == 1 else 'Foram publicados'}",
          f"{len(Artigo.getListaArtigos())} {'artigo' if len(Artigo.getListaArtigos()) == 1 else 'artigos'}.")
    print(f"{'O autor mais recorrente' if len(autores_recorrentes) == 1 else 'Os autores mais recorrentes'}",
          f"{'foi' if len(autores_recorrentes) == 1 else 'foram'} {autores_recorrentes}")
    print(f"{'A palavra chave mais recorrente' if len(palavras_recorrentes) == 1 else 'As  palavras chave mais recorrentes'}",
          f"{'foi' if len(palavras_recorrentes) == 1 else 'foram'} {palavras_recorrentes}")
    

def runMenuArtigo():
    menu_artigo = Menu(["Cadastrar artigo", "Exibir artigos", "Pesquisar artigos", "Gerar relatório final"],
                        [CadastrarArtigo, ExibirArtigos, PesquisarArtigos, GerarRelatorio],
                        "Digite o número da opção desejada: ", "MENU DE ARTIGOS", loop= True)

    menu_artigo.exibir_menu()
    menu_artigo.executar_acao()
    