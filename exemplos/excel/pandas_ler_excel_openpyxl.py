from pathlib import Path

import pandas as pd


arquivo_excel = Path(r"C:\Python\Projeto_Conciliacao_Contabil\_Bases_Razoes\exemplo.xlsx")
aba = "Exportação SAPUI5"
colunas = ["Conta do Razão", "Mont.moeda empresa"]

# Leitura simples de uma aba do Excel usando pandas com openpyxl.
df = pd.read_excel(
    arquivo_excel,
    sheet_name=aba,
    usecols=colunas,
    engine="openpyxl",
)

print(df.head())
print(f"Linhas carregadas: {len(df)}")
