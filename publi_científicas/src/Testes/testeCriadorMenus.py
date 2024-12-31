from src.util.menu import Menu

def runTesteCriadorMenus():
    def acao1():
        print("Executando acao 1")

    def acao2():
        print("Executando acao 2")

    def acao3():
        print("Executando acao 3")

    def acao4():
        print("Executando acao 4") 

    tela_teste = Menu(["Campo 1", "Campo 2", "Campo 3", "Campo 4"], [acao1, acao2, acao3, acao4],  
                      "Digite o número do campo: ", titulo= "Menu de teste", loop= True)

    tela_teste.exibir_menu()
    tela_teste.executar_acao()
