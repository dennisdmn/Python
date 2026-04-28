from pathlib import Path

import polars as pl


arquivo_excel = Path(r"C:\Python\Projeto_Conciliacao_Contabil\_Bases_Razoes\exemplo.xlsx")
aba = "Exportação SAPUI5"
colunas = ["Conta do Razão", "Mont.moeda empresa"]

# Leitura simples de uma aba do Excel usando Polars com calamine.
df = pl.read_excel(
    arquivo_excel,
    sheet_name=aba,
    columns=colunas,
    engine="calamine",
)

print(df.head())
print(f"Linhas carregadas: {df.height}")
