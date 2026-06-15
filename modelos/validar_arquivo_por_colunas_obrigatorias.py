import pandas as pd


def validar_colunas(df: pd.DataFrame, colunas_obrigatorias: set[str]) -> dict:
    faltantes = sorted(colunas_obrigatorias - set(df.columns))
    return {
        'valido': len(faltantes) == 0,
        'colunas_faltantes': faltantes,
    }
