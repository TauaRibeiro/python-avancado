def fibonacci():
    atual = 0
    anterior = 0

    while True:
        if atual == 0:
            yield 0
            atual = 1
        else:
            yield atual+anterior

            temp = atual
            atual += anterior
            anterior = temp

gerador = fibonacci()

for _ in range(0, 10):
    print(next(gerador))