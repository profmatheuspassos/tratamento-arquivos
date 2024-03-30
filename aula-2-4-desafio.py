# Organiza arquivos por formato
from pathlib import Path
import shutil
import datetime

pastaAtual = Path(__file__).parent
pastaAOrganizar = pastaAtual / "arquivos_desafio"
pastaOrganizada = pastaAtual / "organizada"
pastaBackups = pastaAtual / "backups"

if pastaOrganizada.exists():
    shutil.rmtree(pastaOrganizada)

pastaOrganizada.mkdir()

if not pastaBackups.exists():
    pastaBackups.mkdir()

for arquivo in pastaAOrganizar.glob("**/*"):
    if arquivo.is_file():
        pastaOrganizadaComExtensao = pastaOrganizada / arquivo.suffix().replace(".", "")
        if not pastaOrganizadaComExtensao.exists():
            pastaOrganizadaComExtensao.mkdir()
        shutil.copy(arquivo, pastaOrganizadaComExtensao)

nomeBackup = datetime.datetime.now().strftime("%Y-%m-%d")
shutil.make_archive(pastaBackups / nomeBackup, "zip", pastaOrganizada)