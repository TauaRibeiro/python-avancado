class Menu:
    def __init__(self, campos: list[str], acoes: list, titulo: str= "MENU", 
                 borda_principal: str= "=", borda_secundaria: str= "-", tamanho_borda: int= 30, alinhamento_titulo: str= "^", 
                 multiplos_argumento= False, loop= False) -> None:
        self.campos = campos[:]
        self.acoes = acoes[:]
        self.titulo = titulo
        self.config_titulo = borda_principal+alinhamento_titulo+str(tamanho_borda)
        self.config_principal = borda_principal*tamanho_borda
        self.config_secundario = borda_secundaria*tamanho_borda
        self.input = None
        self.mult_argumentos = multiplos_argumento
        self.loop = loop

    def exibir_menu(self, mensagem_input: str) -> None:
        self.config_principal = borda_principal+'*'+str(tamanho_borda)
        self.config_secundario = borda_secundaria+'*'+str(tamanho_borda)
        self.input = None
    
    def exibir_menu(self, mensagem: str) -> None:
        print(f'{self.titulo:{self.config_titulo}}')

        for indice, campo in enumerate(self.campos):
            print(f'{indice}- {campo};')

        print('X- Sair;')
        print(self.config_secundario)
        
        try:
            entrada = input(mensagem_input)
        except ValueError:
            print('Por favor digite um número válido...')
            self.exibir_menu()
        except KeyboardInterrupt:
            exit(0)

        if entrada.lower().strip() == 'x':
            self.input = 'x'
            self.loop = False
        else:  
            entrada = entrada.replace(' ', '').split(',')
            print(self.config_principal)
            
            if not self.mult_argumentos and len(entrada) > 1:
                print("Por favor escolha apenas uma das opções dadas...")
                entrada = None
                self.exibir_menu(mensagem_input)
            else:
                for i in entrada:
                    i = int(i)
                    if i < 0:
                        i *= -1
                    try:
                        self.acoes[i]
                    except IndexError:
                        print('Opção inválida!! Por favor tente novamente...')
                        self.input = None
                        self.exibir_menu(mensagem_input) 

                self.input = entrada 
        

    def executar_acao(self):
        if self.input != 'x':
            for i in self.input:
                self.acoes[int(i)]()

        self.input = None
    
        
def acao1():
    print("Executando acao 1")

def acao2():
    print("Executando acao 2")

def acao3():
    print("Executando acao 3")

def acao4():
    print("Executando acao 4")    

if __name__ == "__main__":
    tela_teste = Menu(["Campo 1", "Campo 2", "Campo 3", "Campo 4"], [acao1, acao2, acao3, acao4], titulo= "Menu de teste", loop= True)

    while tela_teste.loop:
        tela_teste.exibir_menu("Digite o número do campo: ")
        tela_teste.executar_acao()
