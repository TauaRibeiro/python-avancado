from time import sleep

def processar(tarefas):
    fila = []
    buffer = []

    for elemento in tarefas:
        buffer.append(elemento['prioridade'])
        buffer.append(elemento['tarefa'])

        if len(fila) == 0:
            fila.append(buffer[:])
        else:
            adicionar = True
            
            for index, ordem in enumerate(fila):
                if elemento['prioridade'] < ordem[0]:
                    fila.insert(index, buffer[:])

                    adicionar = False
                    break
                elif elemento['prioridade'] == ordem[0]:
                    ordem.append(elemento['tarefa'])

                    adicionar = False
                    break
            if adicionar:
                fila.append(buffer[:])

        buffer.clear()

    for elemento in fila:
        print('REALIZANDO TAREFAS DE PRIORIDADE ' + str(elemento[0]))
        for x in range(len(elemento), 1, -1):
            print('Executando '+ elemento.pop(1), flush= True)

            sleep(1)
        print('-'*30)
        sleep(2)

entrada = dict()
tarefas = list()

while True:
    entrada['tarefa'] = input('Digite a tarefa a ser realizada: ')
    entrada['prioridade'] = int(input('Digite a prioridade da tarefa: '))

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
