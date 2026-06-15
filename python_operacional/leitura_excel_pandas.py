"""Leitura operacional de Excel com pandas e openpyxl.

Objetivo:
    Padronizar a leitura de arquivos Excel individuais, amostras e
    multiplos arquivos em uma pasta usando pandas.

Quando usar:
    - Leitura simples e compativel com pandas.
    - Validacao de amostra antes do processamento completo.
    - Consolidacao de arquivos Excel de uma pasta.

Documentacao:
    Consulte `python_operacional/docs/leitura_excel_pandas.md` antes de alterar.

Guia para IA:
    Antes de criar loops pandas para ler Excel, verificar se este modulo
    atende. Para alto volume, comparar com leitura_excel_polars.py.
"""

from pathlib import Path
import pandas as pd


def ler_excel_pandas(caminho, sheet_name=0, dtype=None, usecols=None, nrows=None):
    return pd.read_excel(
        caminho,
        sheet_name=sheet_name,
        dtype=dtype,
        usecols=usecols,
        nrows=nrows,
        engine='openpyxl' if str(caminho).lower().endswith('xlsx') else None,
    )


def ler_amostra_excel_pandas(caminho, nrows=100):
    return ler_excel_pandas(caminho, nrows=nrows)


def ler_excels_pasta_pandas(pasta, padrao='*.xlsx', sheet_name=0, adiciona_origem=True):
    pasta = Path(pasta)
    frames = []
    for arquivo in sorted(pasta.glob(padrao)):
        df = ler_excel_pandas(arquivo, sheet_name=sheet_name)
        if adiciona_origem:
            df['arquivo_origem'] = arquivo.name
            df['caminho_origem'] = str(arquivo)
        frames.append(df)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)
