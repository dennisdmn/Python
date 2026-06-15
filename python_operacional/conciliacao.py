"""Funcoes genericas de conciliacao por chaves.

Objetivo:
    Concentrar padroes reutilizaveis para comparar duas bases por
    chaves comuns, calcular diferenca e classificar origem.

Quando usar:
    - Comparacao entre duas origens.
    - Conciliacao de saldos ou quantidades.
    - Diagnostico de registros apenas em uma das bases.

Documentacao:
    Consulte `python_operacional/docs/conciliacao.md` antes de alterar.

Guia para IA:
    Antes de criar um merge de conciliacao do zero, verificar se
    `full_outer_conciliacao` atende ao caso. Regra de negocio deve ficar
    no script operacional, nao neste modulo generico.
"""

import numpy as np
import pandas as pd


def full_outer_conciliacao(base_a, base_b, chaves, valor_a, valor_b, nome_a='A', nome_b='B'):
    df = pd.merge(base_a, base_b, on=chaves, how='outer')
    df[valor_a] = df[valor_a].fillna(0).round(2)
    df[valor_b] = df[valor_b].fillna(0).round(2)
    df['DIFERENCA'] = (df[valor_b] - df[valor_a]).round(2)
    df['STATUS'] = np.where(df['DIFERENCA'].abs() < 0.01, 'OK', 'DIVERGENTE')
    df['ORIGEM'] = np.select(
        [
            (df[valor_a] != 0) & (df[valor_b] == 0),
            (df[valor_a] == 0) & (df[valor_b] != 0),
        ],
        ['APENAS_' + nome_a, 'APENAS_' + nome_b],
        default='AMBOS',
    )
    return df


def agregar_saldo(df, chaves, coluna_valor, nome_saldo):
    return (
        df.groupby(chaves, as_index=False)[coluna_valor]
        .sum()
        .rename(columns={coluna_valor: nome_saldo})
    )
