from pathlib import Path
import shutil

# Criando pasta
pastaAtual = Path(__file__).parent
caminhoPastaDestino = pastaAtual / "destino4"
caminhoPastaDestino.mkdir(exist_ok = True)

""" Executado uma vez, pasta destino4 criada """

# Criando pasta com todas as pastas anteriores necessárias
pastaAtual = Path(__file__).parent
caminhoPastaDestino = pastaAtual / "destino5" / "destino5-1"
# caminhoPastaDestino.mkdir(parents = True)

""" Executado uma vez, pastas destino5 e destino5-1 criada - linha comentada para evitar erros """

# Copiando pastas
pastaAtual = Path(__file__).parent
# shutil.copytree(pastaAtual / "destino5", pastaAtual / "destino1" / "destino5")

""" Executado uma vez, pastas destino5 e destino5-1 copiadas - linha comentada para evitar erros """

# Deletando pastas vazias
pastaAtual = Path(__file__).parent
pastaRemover = pastaAtual / "destino5" / "destino5-1"
# pastaRemover.rmdir() # Método só apaga pastas vazias

""" Executado uma vez, pasta destino5-1 excluída - linha comentada para evitar erros """

# Deletando pastas com conteúdo
pastaAtual = Path(__file__).parent
pastaRemover = pastaAtual / "destino1"
shutil.rmtree(pastaRemover) # Remove pastas com conteúdo

""" Executado uma vez, pasta destino1 excluída - linha comentada para evitar erros """