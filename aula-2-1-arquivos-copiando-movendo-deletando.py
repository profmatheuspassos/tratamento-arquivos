from pathlib import Path
import shutil
import os

# Copiando arquivo com copyfile - este método não copia as permissões do arquivo original
"""
pastaAtual = Path(__file__).parent
caminhoArquivo = pastaAtual / "texto.txt"
caminhoArquivoDestino = pastaAtual / "destino1" / "texto.txt"

shutil.copyfile(caminhoArquivo, caminhoArquivoDestino)
"""

""" O script acima foi executado uma vez, arquivo texto.txt criado na pasta destino 2  """

# Copiando arquivo com copy - copia as permissões do arquivo original
"""
pastaAtual = Path(__file__).parent
caminhoArquivo = pastaAtual / "texto.txt"
caminhoPastaDestino = pastaAtual / "destino2"

shutil.copy(caminhoArquivo, caminhoPastaDestino)
"""

""" O script acima foi executado uma vez, arquivo texto.txt criado na pasta destino 2 """

# Copiando arquivo com copy2 - copia as permissões e os metadados do arquivo original
"""
pastaAtual = Path(__file__).parent
caminhoArquivo = pastaAtual / "texto.txt"
caminhoPastaDestino = pastaAtual / "destino3"

shutil.copy2(caminhoArquivo, caminhoPastaDestino)
"""

""" O script acima foi executado uma vez, arquivo texto.txt criado na pasta destino 3 """

# Movendo arquivos
"""
pastaAtual = Path(__file__).parent
caminhoArquivo = pastaAtual / "texto.txt"
caminhoPastaDestino = pastaAtual / "destino1"

shutil.move(caminhoArquivo, caminhoPastaDestino)
"""

""" O script acima foi executado uma vez, arquivo texto.txt criado na pasta destino 1 """

# Deletando arquivos
pastaAtual = Path(__file__).parent
caminhoArquivo = pastaAtual / "texto.txt"
caminhoArquivoDestino = pastaAtual / "destino3" / "texto.txt"

shutil.copyfile(caminhoArquivo, caminhoArquivoDestino)

if caminhoArquivo.exists():
    os.remove(caminhoArquivo)
else:
    print("Arquivo inexistente.")