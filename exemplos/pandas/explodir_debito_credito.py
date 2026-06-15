import pandas as pd


def explodir_debito_credito(df):
    deb = df[['EMPRESA', 'DEBITO', 'VALOR']].copy()
    deb.columns = ['EMPRESA', 'CONTA', 'VALOR']
    deb['SINAL'] = 1

    cred = df[['EMPRESA', 'CREDITO', 'VALOR']].copy()
    cred.columns = ['EMPRESA', 'CONTA', 'VALOR']
    cred['SINAL'] = -1

    movs = pd.concat([deb, cred], ignore_index=True)
    movs['VALOR_LIQ'] = movs['VALOR'] * movs['SINAL']
    return movs
