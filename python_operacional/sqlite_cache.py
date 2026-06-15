from pathlib import Path
import sqlite3
import pandas as pd


def conectar_sqlite(caminho):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(caminho)


def gravar_dataframe_sqlite(df: pd.DataFrame, caminho_db, tabela, if_exists='replace'):
    with conectar_sqlite(caminho_db) as con:
        df.to_sql(tabela, con, if_exists=if_exists, index=False)


def ler_tabela_sqlite(caminho_db, tabela):
    with conectar_sqlite(caminho_db) as con:
        return pd.read_sql_query(f'SELECT * FROM {tabela}', con)


def executar_sql(caminho_db, sql, params=None):
    with conectar_sqlite(caminho_db) as con:
        return pd.read_sql_query(sql, con, params=params)


def criar_indice(caminho_db, tabela, colunas, nome_indice=None):
    nome_indice = nome_indice or 'idx_' + tabela + '_' + '_'.join(colunas)
    cols = ', '.join(colunas)
    sql = f'CREATE INDEX IF NOT EXISTS {nome_indice} ON {tabela} ({cols})'
    with conectar_sqlite(caminho_db) as con:
        con.execute(sql)
        con.commit()
