import re


class Projeto:
    def __init__(self, id_projeto, nome, equipe, data_inicio,
                 data_fim= 'null') -> None:
        self.id = id_projeto
        self.nome = nome
        self.equipe = equipe[:]
        self.status = 'Em andamento'
        self.inicio = data_inicio
        self.fim = data_fim

    def getId() -> int:
        return self.id

        
    def getNome() -> str:
        return self.nome


    def getStatus() -> str:
        return self.status


    def getDataInicio() -> str:
        return self.inicio


    def getDataFim() -> str:
        return self.fim

    
    def setStatus(status) -> None:
        if status:
            self.status = 'Concluído'
        elif not status:
            self.status = 'Em andamento'

        raise(ValueError)

        
    def setNome(nome) -> None:
        self.nome = nome

    def setDataInicio(data, inicio = True) -> None:
        padrao = r'(\d+)/(\d+)/(\d+)'
        # Precisa criar a validação de data
        if re.fullmatch(padrao, data) == None:
            raise(ValueError)

        
        if inicio:
            self.inicio = data
        else:
            self.fim = data
        
        

class Funcionarios:
    def __init__(self, nome, cargo, horas_trabalhadas) -> None:
        self.nome = nome
        self.cargo = cargo
        self.horas = horas_trabalhadas
    pass

