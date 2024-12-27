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
        print(f'{self.titulo:{self.config_titulo}}')

        for indice, campo in enumerate(self.campos):
            print(f'{indice}- {campo};')

        print('X- Sair;')
        print(self.config_secundario)
        
        try:
            entrada = input(mensagem_input)
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
                return
            else:
                for i in entrada:
                    try:
                        i = int(i)
                    except ValueError:
                        print('Por favor digite um número válido...')
                        self.input = None
                        self.exibir_menu(mensagem_input)
                        return

                    if i < 0:
                        print('Por favor digite um número positivo...')
                        self.input = None
                        self.exibir_menu(mensagem_input)
                        return
                    
                    try:
                        self.acoes[i]
                    except IndexError:
                        print('Opção inválida!! Por favor tente novamente...')
                        self.input = None
                        self.exibir_menu(mensagem_input)
                        return 

                self.input = entrada 
        

    def executar_acao(self):
        if self.input != 'x':
            for i in self.input:
                self.acoes[int(i)]()

        self.input = None
    