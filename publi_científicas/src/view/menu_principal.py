from src.util.menu import Menu

def irMenuAutor():
    pass

def irMenuArtigo():
    pass

def runMenuPrincipal():
    tela_principal = Menu(["Seção de autores", "Seção de artigos"], 
                          [irMenuAutor, irMenuArtigo], "Digite o número da opção desejada: ",
                        "MENU PRINCIPAL", loop= True)
    
    tela_principal.exibir_menu()
    tela_principal.executar_acao()