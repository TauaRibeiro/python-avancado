from src.classes.ClasseAutor import Autor

def runTesteAutor():
    while True:
        print('='*30)
        print('1- Cadastrar',
                '\n2- Mostrar',
                '\n3- Editar',
                '\n4- Excluir',
                '\n5- Finalizar')
        print('-'*30)
        decisao = int(input('Digite a decisão: '))
        print('='*30)

        match(decisao):
            case 1:
                novo_autor = Autor(None, None)
                    
                while novo_autor.nome == None or novo_autor.instituicao == None:
                    if novo_autor.nome == None:
                        try:
                            print('-'*30)
                            novo_autor.nome = input('Digite o nome do autor: ')
                        except ValueError:
                            print('Nome inválido!! Deve ter no mínimo 3 caracteres.')
                            print('Por favor, tente novamente...')
                            
                            continue
                    
                    try:
                        print('-'*30)
                        novo_autor.instituicao = input('Digite o nome da instituição: ')
                    except ValueError:
                        print('Nome inválido!! Deve ter no mínimo 3 caracteres.')
                        print('Por favor, tente novamente...')
                        

                Autor.cadastrarAutor(novo_autor)

            case 2:
                print(Autor.mostrarAutores())
            
            case 3:
                if Autor.estaVazia():
                    print('Não há autores cadastrados...')
                    continue
                    
                autor_editado = Autor(None, None)
                
                for indice, autor in enumerate(Autor._lista_autores):
                    print(f'{indice+1}- {autor.nome}')

                print('-'*30)
                decisao = int(input('Digite o número da opção desejada: '))-1
                
                while True:
                    print('='*30)
                    print('1- Nome',
                        '\n2- Instituição')
                    print('-'*30)
                    editar = input('Digite o(os) número(os) do(os) campo(os) que deseja editar (ex: 1; 1,2): ')
                    print('='*30)
                    
                    if not '1' in editar and not '2' in editar:
                        print('Escolha inválida!! Por favor tente novamente')
                        continue
                    
                    break
                    
                while True:
                    if '1' in editar and autor_editado.nome == None:
                        try:
                            print('-'*30)
                            autor_editado.nome = input('Digite o novo nome do autor: ')
                        except ValueError:
                            print('Nome inválido! Por favor tente novamente...')
                            
                            continue
                    
                    if '2' in editar:
                        try:
                            print('-'*30)
                            autor_editado.instituicao = input('Digite a nova instituição do autor: ')
                        except ValueError:
                            print('Institução inválida!! Por favor tente novamente...')
                            
                            continue

                    break
                Autor.editarAutor(decisao, autor_editado)                                   
            
            case 4:
                if Autor.estaVazia():
                    print('Não há autores cadastrados...')

                    continue

                for indice, autor in enumerate(Autor._lista_autores):
                    print(f'{indice+1}- {autor.nome}')
                print('-'*30)
                indice = int(input('Digite o indice do autor a ser excluido: '))-1

                Autor.excluirAutor(indice)

            case 5:
                break
            
            case _:
                ...
