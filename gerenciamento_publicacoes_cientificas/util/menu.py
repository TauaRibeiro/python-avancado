class menu:
    def _init_(self, campos: list[str], acoes: list, titulo: str= "MENU", 
                 borda_principal: str= "=", borda_secundaria: str= "-", tamanho_borda: int= 30, alinhamento_titulo: str= "^") -> None:
        self.campos = campos[:]
        self.acoes = acoes[:]
        self.titulo = titulo
        self.config_titulo = borda_principal+alinhamento_titulo+str(tamanho_borda)
        self.config_principal = borda_principal+'*'+str(tamanho_borda)
        self.config_secundario = borda_secundaria+'*'+str(tamanho_borda)
        self.input = None
    
    def exibir_menu(self, mensagem: str) -> None:
        print(f'{self.titulo:{self.config_titulo}}')

        for indice, campo in enumerate(self.campos):
            print(f'{indice}- {campo};')

        print(self.config_secundario)

        try:
            entrada = input(mensagem)
        except ValueError:
            print('Por favor digite um número válido...')
            self.exibir_menu()
        except KeyboardInterrupt:
            exit(0)

        entrada.strip().split(',')
        if self.acoes[entrada]:
            self.input = entrada
        else:
            print('Opção inválida!')
            self.exibir_menu()      

    def executar_acao(self):
        ...
        

if __name__ == "__main__":
    print('      1, 2, 3, 4'.replace(' ', '').split(','))