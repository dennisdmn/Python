# validacao_layouts.py

## Objetivo

Padronizar validacao de colunas obrigatorias e identificacao de layout por cabecalho.

## Quando usar

Use antes de ler ou processar bases completas, principalmente em arquivos Excel ou CSV com origem manual, SAP, legado ou SAS.

## Funcoes principais

- `validar_colunas_obrigatorias`: retorna se o conjunto de colunas atende ao layout esperado.
- `identificar_layout`: identifica o tipo de arquivo com base nas colunas existentes.
- `exigir_colunas`: interrompe a execucao quando faltam colunas obrigatorias.

## Exemplo de uso

```python
from python_operacional.validacao_layouts import exigir_colunas

colunas_obrigatorias = {'EMPRESA', 'CONTA', 'VALOR'}
exigir_colunas(df.columns, colunas_obrigatorias)
```

## Cuidados

- Validar layout em amostra pequena antes de carregar arquivos grandes.
- Manter nomes de colunas documentados no README do processo operacional.
- Separar colunas obrigatorias de colunas opcionais.

## Orientacao para IA

Antes de criar validacao manual de cabecalhos em um script, reutilize este modulo. A IA deve alterar layouts documentados antes de mudar regras no codigo principal.
