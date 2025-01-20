from src.classes.ClasseArtigo import Artigo

def palavrasChavesRecorrentes() -> list[str]:
    resultado = list()
    contagem_palavras = dict()
    artigo: Artigo

    for artigo in Artigo.getListaArtigos():
        for palavra_chave in artigo.palavras_chave:
            if palavra_chave not in contagem_palavras.keys():
                contagem_palavras[palavra_chave] = 1
            else:
                contagem_palavras[palavra_chave] += 1


    for palavra_chave in contagem_palavras.keys():
        if len(resultado) == 0:
            resultado.append(palavra_chave)
            continue

        if contagem_palavras[palavra_chave] >= contagem_palavras[resultado[0]]:
            if contagem_palavras[palavra_chave] > contagem_palavras[resultado[0]]:
                resultado.clear()

            resultado.append(palavra_chave)

    return resultado
         