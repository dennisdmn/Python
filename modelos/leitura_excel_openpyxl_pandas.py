from pathlib import Path

import pandas as pd


PASTA_BASES = Path(r"C:\Python\Projeto_Conciliacao_Contabil\_Bases_Razoes")
ABA = "Exportação SAPUI5"
COLUNAS = ["Conta do Razão", "Mont.moeda empresa"]

arquivos = sorted(PASTA_BASES.glob("*.xlsx"))
dataframes = []

for arquivo in arquivos:
    print(f"Lendo: {arquivo.name}")

    df = pd.read_excel(
        arquivo,
        sheet_name=ABA,
        usecols=COLUNAS,
        engine="openpyxl",
    )

    df["arquivo_origem"] = arquivo.name
    dataframes.append(df)

if dataframes:
    df_final = pd.concat(dataframes, ignore_index=True)
else:
    df_final = pd.DataFrame(columns=COLUNAS + ["arquivo_origem"])

print(f"Arquivos lidos: {len(arquivos)}")
print(f"Linhas carregadas: {len(df_final)}")

print(df_final.head())
