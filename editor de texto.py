from collections import deque, defaultdict

try:
    texto = deque(input('Digite um texto: '))
except KeyboardInterrupt:
    print('\nPrograma finalizado!!')
    
    finalizar = True
else:
    finalizar = False

acao = dict()
pilha = list()


while not finalizar:
    print('='*30)
    print('O que deseja fazer?')
    print('-'*30)
    print(f'Texto original -> {''.join(texto)}')
    print('-'*30)
    print('1 - Inserir um caracter')
    print('2 - Deletar um caracter')
    print('3 - Desfazer última alteração')
    print('4 - Finalizar')
    print('-'*30)
    try:
        decisao = int(input('Digite o número da opção desejada: '))
    except ValueError:
        print('Por favor digite um número inteiro (Ex: 1, 2, 3, 4)')

        continue
    except KeyboardInterrupt:
        print('\nPrograma encerrado!!')
        
        break
    except Exception as erro:
        print(f'O erro foi -> {erro.__class__}')

    print('='*30)

    match(decisao):
        case 1:
            while True:
                try:
                    caracter = input('Digite o caracter a ser inserido: ')
                except KeyboardInterrupt:
                    print('\nPrograma encerrador!!')
                    finalizar = True
                    break
                if len(caracter) == 1:
                    break

                print('Por favor digite apenas um caracter...')

            while not finalizar:
                print('='*30)
                print('Onde deseja inserir o caracter?')
                print('-'*30)
                print('1 - Início')
                print('2 - Fim')
                print('-'*30)
                try:
                    decisao = int(input('Digite o número da opção desejada: '))
                except ValueError:
                    print('Por favor digite um número inteiro!! (Ex: 1, 2)')

                    continue
                except KeyboardInterrupt:
                    print('\nPrograma encerrado!!')
                    
                    finalizar = True
                    break
                print('='*30)

                match(decisao):
                    case 1:
                        texto.appendleft(caracter)
                        acao['inserir'] = 'inicio'

                        pilha.append(acao.copy())
                        acao.clear()
                        
                        break
                    case 2:
                        texto.append(caracter)
                        acao['inserir'] = 'fim'

                        pilha.append(acao.copy())
                        acao.clear()

                        break
                    case _:
                        print('Opção inválida!! Tente novamente...')
                
                print('Caracter inserido com sucesso!!')
        case 2:
            if len(texto) == 0:
                print('Não há caracteres para serem deletados')
            else:
                while True:
                    print('='*30)
                    print('Onde deseja deletart caracter?')
                    print('-'*30)
                    print('1 - Início')
                    print('2 - Fim')
                    print('-'*30)
                    try:
                        decisao = int(input('Digite o número da opção desejada: '))
                    except ValueError:
                        print('Por favor digite um número inteiro!! (Ex: 1, 2)')

                        continue
                    except KeyboardInterrupt:
                        print('\nPrograma encerrado!!')
                        
                        finalizar = True
                        break
                    print('='*30)

                    match(decisao):
                        case 1:
                            acao['deletar'] = ['inicio', texto.popleft()]

                            pilha.append(acao.copy())
                            acao.clear()
                            
                            break
                        case 2:
                            acao['deletar'] = ['fim', texto.pop()]

                            pilha.append(acao.copy())
                            acao.clear()

                            break
                        case _:
                            print('Opção inválida!! Tente novamente...')
                    
                    print('Caracter deletado com sucesso!!')
        case 3:
            if len(pilha) == 0:
                print('O texto não possui nenhuma alteração...')
            else:
                acao = pilha.pop()
                
                for chave, item in acao.items():
                    if chave == 'inserir':
                        if item == 'fim':
                            texto.pop()
                        else:
                            texto.popleft()
                    else:
                        if item[0] == 'fim':
                            texto.append(item[1])
                        else:
                            texto.appendleft(item[1])
            print('Alteração desfeita com sucesso!!')
        case 4:
            break
        case _:
            print('Opção inválida! Por favor tente novamente...')
