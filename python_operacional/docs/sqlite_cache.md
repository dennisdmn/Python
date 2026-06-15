# sqlite_cache.py

## Objetivo

Fornecer funcoes simples para usar SQLite como camada temporaria de staging, cache e consulta intermediaria em scripts operacionais.

## Quando usar

Use quando a base for grande, quando houver muitos joins, quando for necessario criar indices ou quando o processamento em memoria ficar lento.

## Funcoes principais

- `conectar_sqlite`: cria conexao SQLite e garante a pasta do banco.
- `gravar_dataframe_sqlite`: grava um DataFrame em uma tabela SQLite.
- `ler_tabela_sqlite`: le uma tabela SQLite para pandas.
- `executar_sql`: executa uma consulta SQL e retorna DataFrame.
- `criar_indice`: cria indice simples para acelerar consultas.

## Exemplo de uso

```python
from python_operacional.sqlite_cache import gravar_dataframe_sqlite, executar_sql

gravar_dataframe_sqlite(df, 'work/staging.db', 'base')
resultado = executar_sql('work/staging.db', 'SELECT * FROM base')
```

## Cuidados

- Nao gravar dados sensiveis em bancos temporarios fora de pasta controlada.
- Criar indices em colunas usadas em joins ou filtros.
- Remover arquivos temporarios quando a politica do processo exigir.

## Orientacao para IA

Quando um script apresentar lentidao por volume, muitos merges ou memoria alta, considerar SQLite antes de aumentar complexidade do pandas.
