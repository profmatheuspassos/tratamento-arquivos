from pathlib import Path

pastaAtual = Path(__file__).parent

# Lendo arquivo forma não recomendada
print("\nLendo arquivo forma não recomendada - open")
listaCompras1 = open(pastaAtual / "listaCompras.txt")

print(listaCompras1.read())

listaCompras1.close()

# Lendo arquivo forma recomendada
print("\nLendo arquivo forma recomendada - with open")
with open(pastaAtual / "listaCompras.txt") as listaCompras2:
    print(listaCompras2.read())

"""
Modo default de abertura: mode = r (read)

Principais modos:

r = modo de leitura padrão
r+ = modo de leitura e escrita mas apenas em arquivos já existentes
w = modo de escrita, reescreve por cima se arquivo já existir
a = acrescenta conteúdo no arquivo existente sem reescrever por cima
rb = lê arquivo em binário

Ver outros modos na apostila

"""

# Lendo linha a linha
print("\nLendo linha a linha - readline()")
with open(pastaAtual / "listaCompras.txt") as listaCompras3:
    linha = listaCompras3.readline()
    print(linha)

print("\nLendo linha a linha e incluindo a próxima linha - readline()")
with open(pastaAtual / "listaCompras.txt") as listaCompras31:
    while linha != "":
        linha = listaCompras31.readline()
        print(linha, end = "")

# Lendo todas as linhas
print("\n\nLendo todas as linhas - readlines()")
with open(pastaAtual / "listaCompras.txt") as listaCompras4:
    linha = listaCompras4.readlines()
    print(linha)

# Escrevendo arquivo
print("\nEscrevendo arquivo - método write() - itens já comprados e lista atualizada em listaComprasAtualizada1.txt")

itensComprados1 = ["farinha", "fermento", "água"]

with open(pastaAtual / "listaCompras.txt") as listaCompras5:
    itensLista1 = listaCompras5.readlines()

with open(pastaAtual / "listaComprasAtualizada1.txt", mode = "w") as listaAtualizada1:
    for item in itensLista1:
        if not item.replace("\n", "") in itensComprados1:
            listaAtualizada1.write(item)

# Escrevendo linha a linha
print("\nscrevendo linha a linha - método writelines() - itens já comprados e lista atualizada em listaComprasAtualizada2.txt")
itensComprados2 = ["farinha", "fermento", "água"]

with open(pastaAtual / "listaCompras.txt") as listaCompras6:
    itensLista2 = listaCompras6.readlines()

itensListaAtualizada = []

for item in itensLista2:
    if not item.replace("\n", "") in itensComprados2:
        itensListaAtualizada.append(item)

with open("listaComprasAtualizada2.txt", mode = "w") as listaAtualizada2:
    listaAtualizada2.writelines(itensListaAtualizada)

# Acrescentando valores a um arquivo
print("\nAcrescentando valores a um arquivo")

novosItens = ["banana"]

novosItensComQuebra = []

for item in novosItens:
    novosItensComQuebra.append(f"\n{item}")

"""
Outra maneira de se fazer o for acima:

novosItensComQuebra = [f"\n{item}" for item em novosItens]

Maneira mais "pythônica" de se fazer um for
"""

with open(pastaAtual / "listaCompras.txt", mode = "a") as listaCompras7:
    listaCompras7.writelines(novosItensComQuebra)