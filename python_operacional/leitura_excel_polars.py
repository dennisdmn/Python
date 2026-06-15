"""Leitura operacional de Excel com Polars e fastexcel.

Objetivo:
    Padronizar leitura performatica de Excel usando Polars com engine
    calamine, suportada pelo pacote fastexcel.

Quando usar:
    - Muitos arquivos Excel.
    - Planilhas grandes.
    - Necessidade de leitura mais rapida que pandas/openpyxl.
    - Etapas intermediarias antes de converter para pandas ou SQLite.

Documentacao:
    Consulte `python_operacional/docs/leitura_excel_polars.md` antes de alterar.

Guia para IA:
    Quando o usuario mencionar lentidao, alto volume ou leitura em lote,
    considerar este modulo antes de sugerir pandas puro.
"""

from pathlib import Path
import polars as pl


def ler_excel_polars(caminho, sheet_name=None, columns=None, schema_overrides=None):
    return pl.read_excel(
        source=caminho,
        sheet_name=sheet_name,
        engine='calamine',
        columns=columns,
        schema_overrides=schema_overrides,
    )


def ler_excels_pasta_polars(pasta, padrao='*.xlsx', sheet_name=None, columns=None):
    pasta = Path(pasta)
    frames = []
    for arquivo in sorted(pasta.glob(padrao)):
        df = ler_excel_polars(arquivo, sheet_name=sheet_name, columns=columns)
        df = df.with_columns([
            pl.lit(arquivo.name).alias('arquivo_origem'),
            pl.lit(str(arquivo)).alias('caminho_origem'),
        ])
        frames.append(df)
    if not frames:
        return pl.DataFrame()
    return pl.concat(frames, how='vertical_relaxed')


def para_pandas(df_polars):
    return df_polars.to_pandas()
