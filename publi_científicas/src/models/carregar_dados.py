import xml.etree.ElementTree as ET
from src.classes.ClasseArtigo import Artigo, Autor

def carregarDados() -> None:
    conferencia = ET.Element("conferencia")

    for ar in Artigo.getListaArtigos():
        ar: Artigo
        artigo = ET.SubElement(conferencia, "artigo", id= str(ar._id))

        ET.SubElement(artigo, "titulo").text = str(ar.titulo)

        ETautores = ET.SubElement(artigo, "autores")
        for au in ar.autores:
            au: Autor
            autor = ET.SubElement(ETautores, "autor")
            ET.SubElement(autor, "nome").text = str(au.nome)
            ET.SubElement(autor, "instituicao").text = str(au.instituicao)
        
        ET.SubElement(artigo, "ano_publicacao").text = str(ar.ano_publicacao)
        
        ETpalavras_chave = ET.SubElement(artigo, "palavras_chave")
        for pc in ar.palavras_chave:
            ET.SubElement(ETpalavras_chave, "palavra").text = str(pc)
    
    arvore = ET.ElementTree(conferencia)
    with open('public/artigos_publicados.xml', mode= 'wb') as arquivo:
        arvore.write(arquivo, encoding= 'UTF-8')
