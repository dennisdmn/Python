# leitura_excel_polars.py

## Objetivo

Padronizar leitura de arquivos Excel com Polars usando engine `calamine`, viabilizada pelo pacote `fastexcel`.

## Quando usar

Use quando houver muitos arquivos Excel, bases grandes ou necessidade de leitura mais performatica antes de converter para pandas ou gravar em SQLite.

## Funcoes principais

- `ler_excel_polars`: le um Excel com Polars.
- `ler_excels_pasta_polars`: le varios Excel de uma pasta e empilha os resultados.
- `para_pandas`: converte DataFrame Polars para pandas.

## Exemplo de uso

```python
from python_operacional.leitura_excel_polars import ler_excels_pasta_polars

base = ler_excels_pasta_polars('C:/bases', padrao='*.xlsx')
```

## Dependencias

- `polars`
- `fastexcel`

## Cuidados

- Conferir tipos inferidos em arquivos com colunas mistas.
- Usar `columns` para reduzir leitura quando possivel.
- Converter para pandas apenas quando a etapa seguinte exigir pandas.

## Orientacao para IA

Quando a demanda mencionar performance, arquivos grandes, leitura em looping ou lentidao com openpyxl, considerar este modulo antes de sugerir pandas puro.
