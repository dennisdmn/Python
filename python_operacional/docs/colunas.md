# colunas.py

## Objetivo

Centralizar operacoes recorrentes de escolha, reducao e normalizacao de colunas em DataFrames.

## Quando usar

Use quando a base tem muitas colunas, quando o processo precisa preservar uma ordem especifica de campos ou quando e necessario reduzir memoria antes de joins e conciliacoes.

## Funcoes principais

- `escolher_colunas`: seleciona colunas desejadas e valida obrigatorias.
- `normalizar_nomes_colunas`: remove espacos laterais dos nomes das colunas.
- `colunas_por_texto`: seleciona colunas cujo nome contem termos informados.

## Exemplo de uso

```python
from python_operacional.colunas import escolher_colunas

base = escolher_colunas(
    df,
    colunas=['EMPRESA', 'CONTA', 'VALOR'],
    obrigatorias=['EMPRESA', 'VALOR'],
)
```

## Cuidados

- Preserve a ordem das colunas quando o output for evidencia.
- Use `.copy()` ao recortar colunas para evitar efeitos colaterais.
- Nao remova colunas de rastreabilidade antes de validar o processo.

## Orientacao para IA

Antes de escrever `df[[...]]` repetidamente em scripts operacionais, considere usar este modulo. Ele ajuda a padronizar selecao de campos e validacao minima.
