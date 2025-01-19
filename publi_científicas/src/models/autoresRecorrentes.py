from src.classes.ClasseArtigo import Artigo, Autor

def autoresRecorrentes() -> list[str]:
    resultado = list()
    contagem_autores = dict()
    artigo: Artigo
    autor: Autor

    for artigo in Artigo.lista_artigos:
        for autor in artigo.autores:
            if autor.nome not in contagem_autores.keys():
                contagem_autores[autor.nome] = 1
            else:
                contagem_autores[autor.nome] += 1


    for autor in contagem_autores.keys():
        if len(resultado) == 0:
            resultado.append(autor)
            continue

        if contagem_autores[autor] >= contagem_autores[resultado[0]]:
            if contagem_autores[autor] > contagem_autores[resultado[0]]:
                resultado.clear()

            resultado.append(autor)

    return resultado
         
        