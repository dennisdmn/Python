"""Utilidades operacionais para escolha e normalizacao de colunas.

Objetivo:
    Centralizar operacoes recorrentes de selecao, reducao e normalizacao
    de colunas em DataFrames pandas.

Quando usar:
    - Bases com muitas colunas.
    - Preparacao de evidencias.
    - Reducao de memoria antes de joins e conciliacoes.
    - Padronizacao de campos antes de validar layouts.

Documentacao:
    Consulte `python_operacional/docs/colunas.md` antes de alterar este modulo.

Guia para IA:
    Antes de escrever selecoes manuais como `df[[...]]` em scripts
    operacionais, verificar se `escolher_colunas` atende ao caso.
"""

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
