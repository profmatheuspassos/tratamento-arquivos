"""
VERSÃO ORIGINAL

from pathlib import Path

pastaAtual = Path(__file__).parent

htmlSemEspacos = []

html = []

indicesARemover = []

indice = 0

with open(pastaAtual / "view_lista.html") as original:
    for linha in original:
        htmlSemEspacos.append(linha.strip())
    try:
        indice = htmlSemEspacos.index("Passear com cachorro")
    except:
        print("O item não está na lista.")

with open(pastaAtual / "view_lista.html") as original:
    html = original.readlines()

indicesARemover = [indice]

if indice + 1 < len(html):
    indicesARemover.append(indice + 1)
if indice - 1 >= 0:
    indicesARemover.append(indice - 1)
if indice - 2 >= 0:
    indicesARemover.append(indice - 2)

indicesARemover.sort(reverse=True)

for i in indicesARemover:
    del html[i]

with open(pastaAtual / "view_lista_atualizada.html", mode = "w") as htmlAtualizado:
    htmlAtualizado.writelines(html)
"""



from pathlib import Path

pastaAtual = Path(__file__).parent
caminhoArquivo = pastaAtual / "view_lista.html"
caminhoArquivoAtualizado = pastaAtual / "view_lista_atualizada.html"

try:
    with open(caminhoArquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    textoAlvo = "Passear com cachorro"
    indiceAlvo = None
    for i, linha in enumerate(linhas):
        if textoAlvo in linha:
            indiceAlvo = i
            break

    if indiceAlvo is not None:
        indicesARemover = {indiceAlvo}

        if indiceAlvo + 1 < len(linhas):
            indicesARemover.add(indiceAlvo + 1)
        if indiceAlvo - 1 >= 0:
            indicesARemover.add(indiceAlvo - 1)
        if indiceAlvo - 2 >= 0:
            indicesARemover.add(indiceAlvo - 2)

        linhasAtualizadas = []
        for i, linha in enumerate(linhas):
            if i not in indicesARemover:
                linhasAtualizadas.append(linha)

        with open(caminhoArquivoAtualizado, 'w', encoding='utf-8') as arquivoAtualizado:
            arquivoAtualizado.writelines(linhasAtualizadas)
    else:
        print("O item não está na lista.")
except IOError as erro:
    print(f"Erro ao abrir o arquivo: {erro}")