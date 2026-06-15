import pandas as pd


def escolher_colunas(df: pd.DataFrame, colunas, obrigatorias=None):
    obrigatorias = obrigatorias or []
    faltantes = [c for c in obrigatorias if c not in df.columns]
    if faltantes:
        raise ValueError('Colunas obrigatorias ausentes: ' + str(faltantes))
    existentes = [c for c in colunas if c in df.columns]
    return df.loc[:, existentes].copy()


def normalizar_nomes_colunas(df: pd.DataFrame):
    novo = df.copy()
    novo.columns = [str(c).strip() for c in novo.columns]
    return novo


def colunas_por_texto(df: pd.DataFrame, termos):
    termos = [t.lower() for t in termos]
    cols = [c for c in df.columns if any(t in str(c).lower() for t in termos)]
    return df.loc[:, cols].copy()
