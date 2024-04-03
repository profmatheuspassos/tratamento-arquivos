import pickle
from pathlib import Path

pastaAtual = Path(__file__).parent


"""# Salvando arquivos pickle
minhaLista = [0, 1, 2]
meuDict = {"a": 1, "b": 2}
pastaAtual = Path(__file__).parent

with open(pastaAtual / "pickles" / "minhaLista.pickle", "wb") as arquivo:
    pickle.dump(minhaLista, arquivo)

with open(pastaAtual / "pickles" / "meuDict.pickle", "wb") as arquivo:
    pickle.dump(meuDict, arquivo)

# Lendo arquivos pickle
with open(pastaAtual / "pickles" / "minhaLista.pickle", "rb") as arquivo:
    minhaListaLida = pickle.load(arquivo)

with open(pastaAtual / "pickles" / "meuDict.pickle", "rb") as arquivo:
    meuDictLido = pickle.load(arquivo)

print(type(minhaListaLida))
print(minhaListaLida)

print(type(meuDictLido))
print(meuDictLido)
"""

# Salvando a instância de uma classe com pickle
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def quemSouEu(self):
        print(f"Eu sou {self.nome} e tenho {self.idade} anos.")

joao = Pessoa("João", 31)

joao.quemSouEu()

with open(pastaAtual / "pickles" / "joao.pickle", "wb") as arquivo:
    pickle.dump(joao, arquivo)

# Lendo a mesma instância
with open(pastaAtual / "pickles" / "joao.pickle", "rb") as arquivo:
    joaoLido = pickle.load(arquivo)

joaoLido.quemSouEu()