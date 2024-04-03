import xml.dom.minidom
from pathlib import Path

# Lendo arquivo xml
pastaAtual = Path(__file__).parent
domTree = xml.dom.minidom.parse(str(pastaAtual / "xmls" / "livros.xml"))

group = domTree.documentElement

livros = group.getElementsByTagName("livro")

# print(type(domTree))

# print(type(livros))

# print(domTree)

# print(len(livros))

# Interando por elementos e retornando valores
for livro in livros:
    titulo = livro.getElementsByTagName("titulo")[0].childNodes[0].nodeValue
    autor = livro.getElementsByTagName("autor")[0].childNodes[0].nodeValue
    print(f"Título: {titulo} | Autor: {autor}")

# Salvando um arquivo xml
livros[0].getElementsByTagName("autor")[0].childNodes[0].nodeValue = "Soares, Adriano"

with open(pastaAtual / "xmls" / "livrosCopia.xml", "w") as arquivo:
    domTree.writexml(arquivo)