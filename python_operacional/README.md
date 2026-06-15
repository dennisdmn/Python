# python_operacional

Biblioteca operacional interna para reaproveitar blocos comuns em scripts Python de controladoria, conciliacao, leitura de bases e geracao de evidencias.

A pasta existe para evitar reescrever rotinas repetidas como escolher pasta, escolher arquivo, inventariar diretorios, validar layouts, escolher colunas, ler Excel em lote, usar Polars/fastexcel e usar SQLite como camada temporaria.

## Modulos

- `selecao_arquivos.py`: escolha de pasta e arquivo por janela local.
- `inventario_pastas.py`: inventario de arquivos em uma pasta.
- `validacao_layouts.py`: validacao de colunas obrigatorias e identificacao de layout.
- `colunas.py`: escolha e normalizacao de colunas.
- `leitura_excel_pandas.py`: leitura de Excel com pandas/openpyxl.
- `leitura_excel_polars.py`: leitura de Excel com Polars usando engine calamine/fastexcel.
- `sqlite_cache.py`: gravacao e leitura de tabelas temporarias em SQLite.
- `exportacao_excel.py`: exportacao Excel simples e segura.
- `conciliacao.py`: funcoes genericas de conciliacao.

## Documentacao por arquivo

Cada modulo possui uma documentacao propria em `python_operacional/docs/`:

- `docs/selecao_arquivos.md`
- `docs/inventario_pastas.md`
- `docs/validacao_layouts.md`
- `docs/colunas.md`
- `docs/leitura_excel_pandas.md`
- `docs/leitura_excel_polars.md`
- `docs/sqlite_cache.md`
- `docs/exportacao_excel.md`
- `docs/conciliacao.md`
- `docs/catalogo.md`
- `docs/init.md`

## Dependencias

```powershell
pip install -r .\requirements\python_operacional.txt
```

## Guia para IA

Ao criar um novo script operacional, procurar primeiro aqui antes de escrever funcoes novas. Reutilizar estes blocos sempre que a tarefa envolver selecao de arquivos, leitura de Excel, validacao de layout, reducao de colunas, staging SQLite ou exportacao de evidencia.

## Regra de ouro

Scripts em `scripts/` devem concentrar regra de negocio. Funcoes genericas devem ficar aqui.
