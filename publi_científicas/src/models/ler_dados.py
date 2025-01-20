import xml.etree.ElementTree as ET
from src.classes.ClasseArtigo import Artigo, Autor

def lerDados() -> None:
    arvore = ET.parse('public/artigos_publicados.xml')
    conferencia = arvore.getroot()
    
    for ar in conferencia.findall("artigo"):
        lista_autores = list()
        lista_palavras = list()
        cadastrar = True
        artigo = Artigo()

        artigo._id = int(ar.attrib['id'])
        artigo.titulo = ar.find('titulo').text

        sb_autores = ar.find('autores')
        for au in sb_autores.findall('autor'):
            autor = Autor()

            autor.nome = au.find('nome').text
            autor.instituicao = au.find('instituicao').text

            lista_autores.append(autor)

            for autor_lista in Autor.getListaAutores():
                autor_lista: Autor
                if autor.nome == autor_lista.nome:
                    cadastrar = False
            
            if cadastrar:
                Autor.cadastrarAutor(autor)
                
        artigo.autores = lista_autores

        artigo.ano_publicacao = int(ar.find('ano_publicacao').text)

        sb_palavras = ar.find('palavras_chave')
        for pc in sb_palavras.findall('palavra'):
            lista_palavras.append(pc.text)
        
        artigo.palavras_chave = lista_palavras

        Artigo.cadastrarArtigo(artigo)

        lista_autores.clear()
        lista_palavras.clear()

