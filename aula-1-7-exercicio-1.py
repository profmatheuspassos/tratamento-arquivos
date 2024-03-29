# Desenvolva um script para encontrar um arquivo dentro da pasta home do usuário

from pathlib import Path

caminho = Path.home()

print(caminho)

for arquivo in caminho.glob("**/*"):
    if arquivo.is_file():
        if arquivo.name == "2023-1a-PARTE-LGPD.pptx":
            print("arquivo.name")
            print(arquivo)
            print("Fim")
        if arquivo.stem == "2023-1a-PARTE-LGPD":
            print("arquivo.stem")
            print(arquivo)
            print("Fim")