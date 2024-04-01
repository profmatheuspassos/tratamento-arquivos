import pandas as pd
from pathlib import Path

pastaAtual = Path(__file__).parent

# Lendo tabelas com DataFrame
print("\nLendo tabelas com DataFrame")
tabelaClientes1 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx")
print(tabelaClientes1.head())

# Lendo aba específica
print("\nLendo aba específica - SC")
tabelaClientes2 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SC")
print(tabelaClientes2.head())

# Modificando header
print("\nModificando header")
tabelaClientes3 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SC", header = 1)
print(tabelaClientes3.head())

# Adicionando coluna de index
print("\nAdicionando coluna de index")
tabelaClientes4 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SC", index_col = 0)
print(tabelaClientes4.head())

# Lendo colunas específicas
print("\nLendo colunas específicas - A:B")
tabelaClientes5 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SC", usecols = "A:B")
print(tabelaClientes5.head())

print("\nLendo colunas específicas - [0, 1]")
tabelaClientes6 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SC", usecols = [0, 1])
print(tabelaClientes6.head())

# Comentários sobre decimals e thousands
print("\nComentários sobre decimals e thousands - decimal = \".\"")
tabelaClientes7 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", decimal = ".")
print(tabelaClientes7.head())

print("\nComentários sobre decimals e thousands - thousands = \".\"")
tabelaClientes8 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", thousands = ".")
print(tabelaClientes8.head())

# Escrevendo planilha
print("\nEscrevendo planilha - apenas primeira aba - planilhas/copiaClientes.xlsx")
tabelaClientes9 = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx")
tabelaClientes9.to_excel(pastaAtual / "planilhas" / "copiaClientes.xlsx")

# Escrevendo diversas abas
print("\nEscrevendo diversas abas - planilhas/copiaClientes-RS-SC.xlsx")
tabelaClientesRS = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "RS")
tabelaClientesSC = pd.read_excel(pastaAtual / "planilhas" / "clientes.xlsx", sheet_name = "SC")
with pd.ExcelWriter(pastaAtual / "planilhas" / "copiaClientes-RS-SC.xlsx") as novaPlanilha:
    tabelaClientesRS.to_excel(novaPlanilha, sheet_name = "RS", index = False)
    tabelaClientesSC.to_excel(novaPlanilha, sheet_name = "SC", index = False)