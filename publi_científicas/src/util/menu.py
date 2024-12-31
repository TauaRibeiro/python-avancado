class Menu:
    """
    Menu(self, campos: list[str], acoes: list[func],  mensagem_input: str, titulo: str= "MENU", borda_principal: str= "=",
    borda_secundaria: str= "-", tamanho_borda: int= 30, alinhamento_titulo: str= "^", multiplos_argumento= False, loop= False)
    - Classe que gera um menu personalizavel no qual o usuário pode interagir digitando o número da opção desejada;
    - Caso a repetição (loop) seja True, o menu continuará a ser exibido até que o usuário selecione a opção \"x\";

    ### campos
        - Recebe uma lista de string que se refere ao nome dos campos que serão fornecidos para usuário 
    ### acoes 
        - Recebe um lista de funções que serão executadas conforme a esclha do usuário (Ex: se o usuário escolheu a opção 1, será executado
        a primeira função da lista
    ### mensagem_imput
        - Recebe uma string que será exibida como uma mensagem de input
    ### titulo
        - Recebe uma string que servirá como título para o menu. Padrão é \"MENU\"
    ### borda_principal
        - Recebe uma string que servirá como demarcador para a borda principal. Padrão é \"=\"
    ### borda_secundaria
        - Recebe uma string que servirá como demarcador para a borda secundaria. Padrão é \"-\"
    ### tamanho_borda
        - Recebe um número inteiro que representa o tamanho da borda. Padrão é 30
    ### alinhamento_titulo
        - Recebe uma string que indicará qual será o alinhamento aplicado ao título do menu, o alinhamento segue a regra das
        format strings. Padrão é \"^\"
    ### mutiplos_argumentos
        - Recebe um boolean que indica se o menu irá permitir que o menu aceite mútiplas escolhas do usuário (Ex: 1, 2, 3)
        - As vírgulas \',\' devem ser usadas como separadores. Padrão é False
    ### loop
        - Recebe um boolean que indica se o menu irá ficar se repetido.
        - Caso seja habilitado será fornecido a opção de sair do menu \'x\', e o menu só irá terminar o loop quando o usuario 
        selecionar a devida opção. Padrão é False 
    """
    def __init__(self, campos: list[str], acoes: list, mensagem_input: str, titulo: str= "MENU",
                 borda_principal: str= "=", borda_secundaria: str= "-", tamanho_borda: int= 30, alinhamento_titulo: str= "^", 
                 multiplos_argumento= False, loop= False) -> None:
        self.campos = campos[:]
        self.acoes = acoes[:]
        self.mensagem_input = mensagem_input
        self.titulo = titulo
        self.config_titulo = borda_principal+alinhamento_titulo+str(tamanho_borda)
        self.config_principal = borda_principal*tamanho_borda
        self.config_secundario = borda_secundaria*tamanho_borda
        self.input = None
        self.mult_argumentos = multiplos_argumento
        self.loop = loop

    def exibir_menu(self) -> None:
        """
        - Exibe o menu para o usuário e recebe o input da opção desejada pelo usuário
        """
        print(f'{self.titulo:{self.config_titulo}}')

        for indice, campo in enumerate(self.campos):
            print(f'{indice+1}- {campo};')

        if self.loop:
            print('X- Sair;')
        print(self.config_secundario)
        
        try:
            entrada = input(self.mensagem_input)
        except KeyboardInterrupt:
            exit(0)

        if entrada.lower().strip() == 'x':
            self.input = 'x'
            self.loop = False
        else:  
            entrada = entrada.replace(' ', '').split(',')
            print(self.config_principal)
            
            if not self.loop and input == 'x':
                print('Por favor digite o um dos números fornecidos...')
                self.input = None
                self.exibir_menu()
                return 
            
            if not self.mult_argumentos and len(entrada) > 1:
                print("Por favor escolha apenas uma das opções dadas...")
                entrada = None
                self.exibir_menu()
                return
            
            for i in entrada:
                try:
                    i = int(i)
                except ValueError:
                    print('Por favor digite um número válido...')
                    self.input = None
                    self.exibir_menu()
                    return

                if i <= 0:
                    print('Por favor digite um número maior que zero...')
                    self.input = None
                    self.exibir_menu()
                    return
                
                try:
                    self.acoes[i-1]
                except IndexError:
                    print('Opção inválida!! Por favor tente novamente...')
                    self.input = None
                    self.exibir_menu()
                    return 

            self.input = entrada 
    

    def executar_acao(self):
        """
        - Executa a ação escolhida pelo usuário.        
        """
        if self.input != 'x':
            for i in self.input:
                self.acoes[int(i)-1]()

        self.input = None

        if self.loop:
            self.exibir_menu()
            self.executar_acao()
    