"""Pacote de blocos operacionais reutilizaveis.

Objetivo:
    Expor modulos genericos usados por scripts Python de controladoria,
    conciliacao, leitura de bases e geracao de evidencias.

Documentacao:
    Consulte `python_operacional/README.md` e `python_operacional/docs/init.md`.

Guia para IA:
    Ao adicionar novo modulo publico em `python_operacional/`, avaliar se
    ele deve entrar em `__all__` e criar documentacao em `docs/`.
"""

__all__ = [
    'selecao_arquivos',
    'inventario_pastas',
    'validacao_layouts',
    'colunas',
    'leitura_excel_pandas',
    'leitura_excel_polars',
    'sqlite_cache',
    'exportacao_excel',
    'conciliacao',
]
