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
