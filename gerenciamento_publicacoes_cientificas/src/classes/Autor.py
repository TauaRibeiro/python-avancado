class Autor:
    lista_autores = list()

    def __init__(self, nome: str, instituicao) -> None:
        self._nome = nome
        self._instituicao = instituicao


    def __str__(self) -> str:
        return f'\tNOME: {self._nome}\n\tINSTITUIÇÃO: {self._instituicao}\n\n'


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
    def cadastrarAutor(autor) -> bool:
        if len(autor._nome) < 3 or len(autor._instituicao) < 3:
            return False
        
        Autor.lista_autores.append(autor)
        return True
    

    @staticmethod
    def mostrarAutores() -> str:
        if len(Autor.lista_autores) == 0:
            return 'Não há autores cadastrados'
        
        resultado = []

        for autor in Autor.lista_autores:
            resultado.append(str(autor))
        
        return ''.join(resultado)
    

    @staticmethod
    def editarAutor(indice_autor: int, autor_editado) -> bool:
        if len(autor_editado._nome) < 3 or len(autor_editado._instituicao) < 3:
            return False
        
        Autor.lista_autores[indice_autor] = autor_editado
        return True
        

    @staticmethod
    def excluirAutor(indice_autor) -> None:
        Autor.lista_autores.remove(indice_autor)
        
    @staticmethod
    def cadastrouAutor() -> bool:
        if len(Autor.lista_autores) == 0:
            return False
        return True
        


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
                
                while True: 
                    novo_autor = Autor('Nome', 'Instituição')
                        
                    while True:
                        if novo_autor.nome == 'Nome':
                            try:
                                novo_autor.nome = input('Digite o nome do autor: ')
                            except ValueError:
                                print('Nome inválido!! Deve ter no mínimo 3 caracteres.')
                                print('Por favor, tente novamente...')
                                
                                continue
                        
                        try:
                            novo_autor.instituicao = input('Digite o nome da instituição: ')
                        except ValueError:
                            print('Nome inválido!! Deve ter no mínimo 3 caracteres.')
                            print('Por favor, tente novamente...')
                            
                            continue
                        
                        break
                    
                    break

                Autor.cadastrarAutor(novo_autor)
    
            case 2:
                print(Autor.mostrarAutores())
            
            case 3:
                if not Autor.cadastrouAutor():
                    print('Não há autores cadastrados...')
                    continue
                    
                autor_editado = Autor('Nome', 'Instituição')
                
                for indice, autor in enumerate(Autor.lista_autores):
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
                    
                    # Alterar o método editar no
                    
                    # while True:
                    #     if novo_autor.nome == 'Nome':
                    #         if '1' in editar:
                    #             try:
                    #                 novo_autor.nome = input('Digite o nome do autor: ')
                    #             except ValueError:
                    #                 print('Nome inválido!! Por favor tente novamente...')
                    #                 continue
                    #         else:
                    #             novo_autor.nome = Autor.lista_autores[indice].nome
                    #     if novo_autor.instituicao == 'Instituição' and '':
                                   
            
            case 4:
                ...
            
            case 5:
                break
            
            case _:
                ...
