def processamento(tarefas):
    fila = ([],[],[])

    for elemento in tarefas:
        fila[elemento['prioridade']-1].append(elemento['tarefa'])

    print(fila)

    for prioridade in fila:
        for x in range(0, len(prioridade)):
            print(prioridade.pop(0))

processamento([{'tarefa':"comer", 'prioridade':1},
               {'tarefa':"jogar", 'prioridade':3},
               {'tarefa':"dormir", 'prioridade':1},
               {'tarefa':"assistir vídeos", 'prioridade':2},
               {'tarefa':"tomar banho", 'prioridade':2},
               {'tarefa':"criar o tigrinho", 'prioridade':3},
               {'tarefa':"alisar o gato", 'prioridade':1}])






