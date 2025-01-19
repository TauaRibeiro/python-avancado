from src.util.menu import Menu
from src.view.menu_autor import runMenuAutor
from src.view.menu_artigo import runMenuArtigo

def runMenuPrincipal():
    tela_principal = Menu(["Seção de autores", "Seção de artigos"], 
                          [runMenuAutor, runMenuArtigo], "Digite o número da opção desejada: ",
                        "MENU PRINCIPAL", loop= True)
    
    tela_principal.exibir_menu()
    tela_principal.executar_acao()