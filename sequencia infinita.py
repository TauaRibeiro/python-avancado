def sequencia_infinita(numero):
    status = 'continuar'
    numero_alteracao = None
    while True:
        entrada = yield numero

        if entrada == None:
            if status == 'pular' or status == 'reset':
                status = (status, numero_alteracao)
            
            entrada = status

        if entrada == 'continuar':
            numero += 1 if status == entrada else 0

            status = 'continuar'

        elif entrada == 'pausar':
            status = 'pausar'

        elif entrada[0] == 'pular':
            if not numero_alteracao in entrada:
                numero_alteracao = entrada[1]
                numero += numero_alteracao
                status = 'pular'
            else:
                status = 'continuar'
        elif entrada[0] == 'reset':
            if numero != numero_alteracao:
                numero_alteracao = entrada[1]
                numero = numero_alteracao
                status = 'reset'
            else:
                status = 'continuar'
