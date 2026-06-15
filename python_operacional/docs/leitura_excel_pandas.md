# leitura_excel_pandas.py

## Objetivo

Padronizar leitura de arquivos Excel com pandas e openpyxl, incluindo leitura de amostra e leitura em lote por pasta.

## Quando usar

Use quando o foco for compatibilidade, simplicidade e integracao direta com DataFrames pandas.

## Funcoes principais

- `ler_excel_pandas`: le um arquivo Excel.
- `ler_amostra_excel_pandas`: le uma quantidade reduzida de linhas para validacao.
- `ler_excels_pasta_pandas`: consolida varios arquivos Excel de uma pasta.

## Exemplo de uso

```python
from python_operacional.leitura_excel_pandas import ler_excels_pasta_pandas

base = ler_excels_pasta_pandas('C:/bases', padrao='*.xlsx')
```

## Cuidados

- Para arquivos grandes, ler primeiro amostra com `nrows`.
- Use `usecols` quando souber quais colunas sao necessarias.
- Para bases muito grandes, avaliar Polars/fastexcel ou SQLite.

## Orientacao para IA

Antes de criar loops de leitura com pandas, consulte este modulo. Se o arquivo for grande ou houver muitos Excel, compare com o modulo Polars.
