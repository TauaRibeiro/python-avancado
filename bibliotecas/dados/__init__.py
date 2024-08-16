def ler_inteiro(mensagem = ''):
    while True:
        try:
            entrada = input(mensagem)
        except KeyboardInterrupt:
            print('\nERRO!! Nada foi digitado, por favor digite um número...')
        else:
            
            if entrada.isnumeric():
                return int(entrada)
        
        print('ERRO!! Valor inválido, tente novamente...')

def ler_real(mensagem = ''):
    while True:
        try:
            entrada = input(mensagem)
        except KeyboardInterrupt:
            print('\nERRO!! Nada foi digitado, por favor tente novamente...')
        else:
            entrada = entrada.replace(',', '.')

            valido = True

            for digito in entrada:
                if not digito.isnumeric() and digito != '.':
                    valido = False
                
            if valido:
                return float(entrada)
            
            print('ERRO!! Valor inválido, tente novamente...')
