from pathlib import Path

# Aqui o resultado será "True" porque o arquivo está sendo executado na mesma pasta em que a primeiraPasta se encontra - caminho relativo

print(Path("primeiraPasta").exists())

# Indica o "Current Working Directory"

print(Path.cwd())