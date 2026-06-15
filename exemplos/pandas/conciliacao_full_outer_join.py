import pandas as pd

base_a = pd.DataFrame({'EMPRESA': ['1000'], 'CONTA': ['1101'], 'SALDO_A': [100.0]})
base_b = pd.DataFrame({'EMPRESA': ['1000'], 'CONTA': ['1101'], 'SALDO_B': [100.0]})

conc = pd.merge(base_a, base_b, on=['EMPRESA', 'CONTA'], how='outer')
conc['SALDO_A'] = conc['SALDO_A'].fillna(0)
conc['SALDO_B'] = conc['SALDO_B'].fillna(0)
conc['DIFERENCA'] = conc['SALDO_B'] - conc['SALDO_A']
print(conc)
