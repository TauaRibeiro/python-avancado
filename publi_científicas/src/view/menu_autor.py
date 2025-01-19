from src.view.menu_edicao_autor import runMenuEdicaoAutor
from src.util.menu import Menu
from src.classes.ClasseAutor import Autor

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

def ListarAutores():
    print(Autor.mostrarAutores())

def EditarAutor():
    if Autor.estaVazia():
        print('Não há autores cadastrados...')
        return
        
    autor_editado = Autor(None, None)
    
    for indice, autor in enumerate(Autor._lista_autores):
        print(f'{indice+1}- {autor.nome}')

    print('-'*30)
    decisao = int(input('Digite o número da opção desejada: '))-1
    
    runMenuEdicaoAutor(decisao, autor_editado)      

def runMenuAutor():
    menu_autor = Menu(["Cadastrar autor", "Listar autores", "Editar autor"],
                      [CadastrarAutor, ListarAutores, EditarAutor], 
                      "Digite o número da opção desejada: ","MENU AUTOR", loop= True)
    
    menu_autor.exibir_menu()
    menu_autor.executar_acao()