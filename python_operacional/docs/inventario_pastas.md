# inventario_pastas.py

## Objetivo

Gerar inventario de arquivos de uma pasta em formato tabular, incluindo nome, extensao, tamanho, data de modificacao e caminho.

## Quando usar

Use antes de processar bases em lote, validar quantidade de arquivos, auditar entradas ou registrar rastreabilidade de uma execucao.

## Funcoes principais

- `inventariar_pasta`: retorna um DataFrame com os arquivos encontrados.
- `listar_arquivos`: retorna uma lista de caminhos filtrada por extensao.

## Exemplo de uso

```python
from python_operacional.inventario_pastas import inventariar_pasta

inventario = inventariar_pasta('C:/bases', extensoes={'.xlsx', '.csv'})
print(inventario)
```

## Cuidados

- Use `recursivo=True` apenas quando precisar varrer subpastas.
- Filtre extensoes para evitar processar arquivos temporarios.
- Guarde o inventario quando a rastreabilidade da execucao for importante.

## Orientacao para IA

Antes de criar loops manuais com `Path.glob`, consulte este modulo. Ele deve ser o ponto inicial para scripts que processam varios arquivos.
