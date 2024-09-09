def sequencia_infinita(numero):
    status = 'continuar'
    incrementador = None
    while True:
        entrada = yield numero
        
        print(entrada)
        if entrada == None:
            # terminar essa parte
            if status == 'pular' or status == 'reset':
                status = ('pular', incrementador)

            entrada = status

        if entrada == 'continuar':
            numero += 1 if status == entrada else 0

            status = 'continuar'

        elif entrada == 'pausar':
            status = 'pausar'

        elif entrada[0] == 'pular':
            incrementador = entrada[1]
            numero += incrementador
            status = 'pular'

        elif entrada[] == 'reset':


            


gerador = sequencia_infinita(10)

print(next(gerador))
print(next(gerador))

gerador.send(('pular', 3))
print(next(gerador))
print(next(gerador))