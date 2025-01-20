from src.view.menu_edicao_autor import runMenuEdicaoAutor
from src.util.menu import Menu
from src.classes.ClasseAutor import Autor
from src.models import carregarDados

def CadastrarAutor():
    novo_autor = Autor()
    
    while novo_autor.nome is None or novo_autor.instituicao is None:
        if novo_autor.nome == None:
            try:
                print("-"*30)
                novo_autor.nome = input("Digite o nome do autor: ")
            except ValueError:
                print('Nome inválido!! Deve ter no mínimo 3 caracteres.')
                print('Por favor, tente novamente...')
                
                continue
        
        try:
            print("-"*30)
            novo_autor.instituicao = input("Digite a instituição do autor: ")
        except ValueError:
            print('Nome inválido!! Deve ter no mínimo 3 caracteres.')
            print('Por favor, tente novamente...')

        Autor.cadastrarAutor(novo_autor)
        carregarDados()

def ListarAutores():
    print(Autor.mostrarAutores())

def EditarAutor():
    if Autor.estaVazia():
        print('Não há autores cadastrados...')
        return
        
    
    menu_autores = Menu([a.nome for a in Autor.getListaAutores()],[],
                        "Digite o número da opção desejada: ", "",
                        borda_principal= '~', borda_secundaria= '.',)
    menu_autores.exibir_menu()
    
    indice_autor = int(menu_autores.input[0])-1

    runMenuEdicaoAutor(indice_autor, Autor.obterAutores([indice_autor])[0])
    carregarDados()

def runMenuAutor():
    menu_autor = Menu(["Cadastrar autor", "Listar autores", "Editar autor"],
                      [CadastrarAutor, ListarAutores, EditarAutor], 
                      "Digite o número da opção desejada: ","MENU AUTOR", loop= True)
    
    menu_autor.exibir_menu()
    menu_autor.executar_acao()