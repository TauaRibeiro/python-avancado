def contador_personalizado(numero_incrementador=0):
    numero_inicial = contador = 0

    def incrementador(inicial, reset=False):
        nonlocal numero_inicial, contador, numero_incrementador

        if reset:
            numero_incrementador = inicial
            numero_inicial = contador = 0
        
        if inicial != numero_inicial:
            numero_inicial = inicial
            contador = 0

        if contador != 0:
            contador += numero_incrementador
        else:
            contador = numero_incrementador + numero_inicial

        return contador

    return incrementador

