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
            resultado.append(autor.__str__)

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
        


if __name__ == '__main__':
    while True:
        print('='*30)
        print('1- Cadastrar',
              '\n2- Mostrar',
              '\n3- Editar',
              '\n4- Excluir',
              '\n5- Finalizar')
        decisao = int(input('Digite a decisão: '))
        print('='*30)

        match(decisao):
            case 1:
                nome_autor = input('Digite o nome do autor')
                instituicao_autor = input('Digite a instituicao do autor')

                novo_autor = Autor(nome_autor, instituicao_autor)
                # CORRIGIR
                
                # while True:
                #     if (novo_autor.nome = nome_autor): 
                    
                #     if novo_autor.nome == nome_autor:
                #         print('ERRO, Nome inválido!! Por favor tente novamente...')
                #     if Autor.cadastrarAutor(novo_autor):
                #         break

            case 2:
                ...
            case 3:
                ...
            case 4:
                ...
            case 5:
                ...
            case _:
                ...