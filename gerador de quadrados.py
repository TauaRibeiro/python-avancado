def quadrados(limite):
    numero = 1

    while numero <= limite:
        yield numero**2
        numero += 1

gerador = quadrados(5)

for numero in gerador:
    print(numero)