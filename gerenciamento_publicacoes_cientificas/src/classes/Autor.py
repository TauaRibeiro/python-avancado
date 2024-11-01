class Autor:
    _lista_autores = list()

    def __init__(self, nome: str= None, instituicao: str= None) -> None:
        self._nome = nome
        self._instituicao = instituicao


    def __str__(self) -> str:
        return f'\tNOME: {self._nome}\n\tINSTITUIÇÃO: {self._instituicao}\n\n'

    @property
    def lista_autores() -> list:
        return Autor._lista_autores
    
    @lista_autores.setter
    def lista_autores(lista: list) -> None:
        Autor._lista_autores = lista[:]

    @property
    def nome(self) -> str:
        return self._nome


    @property
    def instituicao(self) -> str:
        return self._instituicao


    @nome.setter
    def nome(self, nome: str) -> None:
        if len(nome) >= 3:
            self._nome = nome
        else:
            raise ValueError('Nome possui menos de 3 caracteres')


    @instituicao.setter
    def instituicao(self, instituicao: str) -> None:
        if len(instituicao) >= 3:
            self._instituicao = instituicao
        else:
            raise ValueError('Nome da instituição possui menos de 3 caracteres')


    @staticmethod
    def cadastrarAutor(autor) -> None:
        Autor._lista_autores.append(autor)


    @staticmethod
    def mostrarAutores(autor_procurado= None) -> str:
        if Autor.estaVazia():
            return 'Não há autores cadastrados'
        
        resultado = []

        for autor in Autor._lista_autores:
            if autor_procurado is None or autor is autor_procurado:
                resultado.append(str(autor))
        
        return ''.join(resultado)


    @staticmethod
    def editarAutor(indice_autor: int, autor_editado) -> None:
        if autor_editado._nome == None:
            autor_editado._nome = Autor._lista_autores[indice_autor]._nome

        if autor_editado._instituicao == None:
            autor_editado._instituicao = Autor._lista_autores[indice_autor]._instituicao

        
        Autor._lista_autores[indice_autor] = autor_editado


    @staticmethod
    def excluirAutor(indice_autor) -> None:
        Autor._lista_autores.pop(indice_autor)


    @staticmethod
    def estaVazia() -> bool:
        if len(Autor._lista_autores) == 0:
            return True
        return False
        
        
    @staticmethod
    def obterAutores(indices_autores: list[int]) -> list:
        resultado = []

        for indice in indices_autores:
            if not Autor._lista_autores[indice] in resultado:
                try:
                    resultado.append(Autor._lista_autores[indice])
                except IndexError:
                    continue
        
        return resultado
            
                

        
# Parte para testes da classe Autor, simulando a interação de um usuário. Além de ajudar na construção da interface principal.
if __name__ == '__main__':
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
