import pandas as pd


def escolher_colunas(df: pd.DataFrame, colunas_desejadas: list[str], obrigatorias: list[str] | None = None) -> pd.DataFrame:
    obrigatorias = obrigatorias or []
    faltantes_obrigatorias = [col for col in obrigatorias if col not in df.columns]
    if faltantes_obrigatorias:
        raise ValueError(f'Colunas obrigatorias ausentes: {faltantes_obrigatorias}')

    colunas_existentes = [col for col in colunas_desejadas if col in df.columns]
    return df.loc[:, colunas_existentes].copy()


def escolher_colunas_por_prefixo(df: pd.DataFrame, prefixos: list[str]) -> pd.DataFrame:
    colunas = [col for col in df.columns if any(str(col).startswith(prefixo) for prefixo in prefixos)]
    return df.loc[:, colunas].copy()


def escolher_colunas_por_contem(df: pd.DataFrame, termos: list[str]) -> pd.DataFrame:
    termos_norm = [termo.lower() for termo in termos]
    colunas = [col for col in df.columns if any(termo in str(col).lower() for termo in termos_norm)]
    return df.loc[:, colunas].copy()
