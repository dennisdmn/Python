import numpy as np
import pandas as pd


def conciliar_saldos(saldo_a, saldo_b, chaves, col_a='SALDO_A', col_b='SALDO_B'):
    base = pd.merge(saldo_a, saldo_b, on=chaves, how='outer')
    base[col_a] = base[col_a].fillna(0).round(2)
    base[col_b] = base[col_b].fillna(0).round(2)
    base['DIFERENCA'] = (base[col_b] - base[col_a]).round(2)
    base['STATUS'] = np.where(base['DIFERENCA'].abs() < 0.01, 'OK', 'DIVERGENTE')
    base['ORIGEM'] = np.select(
        [
            (base[col_b] == 0) & (base[col_a] != 0),
            (base[col_a] == 0) & (base[col_b] != 0),
        ],
        ['APENAS_A', 'APENAS_B'],
        default='AMBOS',
    )
    return base
