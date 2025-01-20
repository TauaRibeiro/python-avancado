from src.util.menu import Menu
from src.classes.ClasseAutor import Autor
from src.models.carregar_dados import carregarDados

def EditarNome(autor_editado: Autor):
    try:
        print('-'*30)
        autor_editado.nome = input('Digite o novo nome do autor: ')
    except ValueError:
        print('Nome inválido! Por favor tente novamente...')
        EditarInstituicao(autor_editado)

def EditarInstituicao(autor_editado: Autor):
    try:
        print('-'*30)
        autor_editado.instituicao = input('Digite a nova instituição do autor: ')
    except ValueError:
        print('Institução inválida!! Por favor tente novamente...')
        EditarInstituicao(autor_editado)

def runMenuEdicaoAutor(decisao: int, autor_editado: Autor):
    menu_edicao = Menu(["Nome", "Instituição"], [EditarNome, EditarInstituicao],
                       "Digite os números das opções desejadas: ", "",
                       multiplos_argumento= True)
    
    menu_edicao.exibir_menu()
    menu_edicao.executar_acao(autor_editado)
    
    Autor.editarAutor(decisao, autor_editado)
  