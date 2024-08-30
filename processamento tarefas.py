from time import sleep

def processar(tarefas):
    fila = []
    buffer = []

    for elemento in tarefas:
        buffer.append(elemento['tarefa'])
        buffer.append(elemento['prioridade'])

        if len(fila) == 0:
            fila.append(buffer[:])
        else:
            for index, ordem in enumerate(fila):
                if elemento['prioridade'] < ordem[1]:
                    fila.insert(index, buffer[:])

        buffer.clear()
        
    print(fila)

    for elemento in fila:
        print('REALIZANDO TAREFAS DE PRIORIDADE ' + elemento['prioridade'])
        for x in range(len(elemento), 0):
            print('Executando '+ elemento.pop(), flush= True)

            sleep(2)
    print()


entrada = dict()
tarefas = list()

while True:
    entrada['tarefa'] = input('Digite a tarefa a ser realizada: ')
    entrada['prioridade'] = int(input('Digite a prioridade da tarefa (1 à 3): '))

    tarefas.append(entrada.copy())
    entrada.clear()

    while True:
        parar = input('Deseja continuar? [SIM / NÃO]: ').lower()
        
        if parar in ['sim', 'não', 'nao', 's', 'n']:
            if parar in ['não', 'nao', 'n']:
                parar = True
            else:
                parar = False
            break
        
        else:
            print('Opção inválida!! Por favor tente novamente...')
    
    print('-'*30)

    if parar:
        break
    
processar(tarefas)    

