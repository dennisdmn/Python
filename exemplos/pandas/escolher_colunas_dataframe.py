import pandas as pd

# Exemplo didatico: escolher somente as colunas necessarias de uma base.

df = pd.DataFrame(
    {
        'EMPRESA': ['1000', '3000'],
        'CONTA': ['1101', '1102'],
        'VALOR': [100.0, 200.0],
        'OBSERVACAO': ['ok', 'validar'],
    }
)

colunas_desejadas = ['EMPRESA', 'CONTA', 'VALOR']

base_reduzida = df.loc[:, colunas_desejadas].copy()

print(base_reduzida)
