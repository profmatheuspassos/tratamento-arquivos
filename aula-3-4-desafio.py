from pathlib import Path
import pandas as pd

pastaAtual = Path(__file__).parent

"""
MANEIRA INDICADA PELO PROFESSOR

tabelaClientesDict = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = None)

for nomeAba, tabela in tabelaClientesDict.items():
    tabela.to_excel(pastaAtual / "planilhas" / "planilhas-Separadas" / f"{nomeAba}.xlsx", index = False)

with pd.ExcelWriter(pastaAtual / "planilhas" / "planilha-Consolidada" / "clientes.xlsx") as consolidada:
    for arquivo in Path(pastaAtual / "planilhas" / "planilhas-Separadas").glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name = arquivo.stem, index = False)
"""

planilhaRS = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "RS")

planilhaSC = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SC")

planilhaPR = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "PR")

planilhaSP = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SP")

caminhoPastaDestinoSeparadas = pastaAtual / "planilhas" / "planilhasSeparadas"

caminhoPastaDestinoConsolidadas = pastaAtual / "planilhas" / "planilhasConsolidadas"

caminhoPastaDestinoSeparadas.mkdir(exist_ok = True)

caminhoPastaDestinoConsolidadas.mkdir(exist_ok = True)

with pd.ExcelWriter(caminhoPastaDestinoConsolidadas / "clientesConsolidada.xlsx") as novaPlanilha:
    planilhaRS.to_excel(novaPlanilha, sheet_name = "RS", index = False)
    planilhaSC.to_excel(novaPlanilha, sheet_name = "SC", index = False)
    planilhaPR.to_excel(novaPlanilha, sheet_name = "PR", index = False)
    planilhaSP.to_excel(novaPlanilha, sheet_name = "SP", index = False)

with pd.ExcelWriter(caminhoPastaDestinoSeparadas / "clientes-RS.xlsx") as novaPlanilhaRS:
    planilhaRS.to_excel(novaPlanilhaRS, sheet_name = "RS", index = False)
with pd.ExcelWriter(caminhoPastaDestinoSeparadas / "clientes-SC.xlsx") as novaPlanilhaSC:
    planilhaSC.to_excel(novaPlanilhaSC, sheet_name = "SC", index = False)
with pd.ExcelWriter(caminhoPastaDestinoSeparadas / "clientes-PR.xlsx") as novaPlanilhaPR:
    planilhaPR.to_excel(novaPlanilhaPR, sheet_name = "PR", index = False)
with pd.ExcelWriter(caminhoPastaDestinoSeparadas / "clientes-SP.xlsx") as novaPlanilhaSP:
    planilhaSP.to_excel(novaPlanilhaSP, sheet_name = "SP", index = False)