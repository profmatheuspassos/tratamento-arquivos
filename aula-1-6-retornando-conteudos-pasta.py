from pathlib import Path
import os

os.system("clear")

# Listando arquivos de uma pasta
print("os.listdir(Path.cwd())")
print(os.listdir(Path.cwd()))
print("\nPath.cwd().glob(\"*\")")
print(Path.cwd().glob("*"))
print("\nlist(Path.cwd().glob(\"*\"))")
print(list(Path.cwd().glob("*")))

# Listando arquivos de uma determinada extensão
print("\nlist(Path.cwd().glob(\"*.py\"))")
print(list(Path.cwd().glob("*.py")))

# Listar tudo dentro de uma pasta
print("\nlist(Path.cwd().glob(\"**/*\"))")
print(list(Path.cwd().glob("**/*")))
print("\nlist(Path.cwd().glob(\"**/*.txt\"))")
print(list(Path.cwd().glob("**/*.txt")))

# Validando caminhos
print("\nNão existe")
naoExiste = Path.home() / "naoExiste"
print(naoExiste.exists())

# Verificando se é arquivo ou pasta
print("\nVerificando se é arquivo ou pasta")
print(Path(__file__))
print(Path(__file__).is_file())
print(Path(__file__).parent)
print(Path(__file__).parent.is_file())
print(Path(__file__).parent)
print(Path(__file__).parent.is_dir())
print("\nTESTE")
caminhoArquivo = Path(__file__)
print(Path(__file__).name)
print(Path(__file__).stem)
print(Path(__file__).suffix)
print(caminhoArquivo.name)
print(caminhoArquivo.stem)
print(caminhoArquivo.suffix)