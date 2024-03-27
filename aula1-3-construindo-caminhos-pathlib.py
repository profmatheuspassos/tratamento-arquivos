from pathlib import Path

# A utilização de "Path" faz com que o script identifique o sistema operacional e faça a conversão para o tipo de barra (normal ou invertida - Windows)

caminho = Path("primeiraPasta/segundaPasta")

# Poderia ser também caminho = Path("primeiraPasta") / caminho = Path("segundaPasta")

# Caminho relativo

for nome in ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]:
    caminhoArquivo = caminho/nome
    print(caminhoArquivo)

# Caminho absoluto
    
caminho = Path("/Users/matheuspassossilva/Library/CloudStorage/Dropbox/GitHub/tratamento-arquivos/")

for nome in ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]:
    caminhoArquivo = caminho/nome
    print(caminhoArquivo)

print(Path.home())