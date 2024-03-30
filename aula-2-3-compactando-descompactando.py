from pathlib import Path
import shutil

# Compactando arquivos
pastaAtual = Path(__file__).parent
pastaCompactada = pastaAtual
nomeArquivoCompactado = pastaAtual / "compactado"
shutil.make_archive(nomeArquivoCompactado, "zip", pastaCompactada)

# Descompactando arquivos
pastaAtual = Path(__file__).parent
nomeArquivoCompactado = pastaAtual / "compactado.zip"
pastaDescompactada = pastaAtual / "descompactada"
shutil.unpack_archive(nomeArquivoCompactado, pastaDescompactada, "zip")
