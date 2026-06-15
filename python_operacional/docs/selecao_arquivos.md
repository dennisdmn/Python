# selecao_arquivos.py

## Objetivo

Centralizar funcoes simples de selecao de pasta e arquivo por janela local.

## Quando usar

Use este modulo em scripts executados manualmente no Windows quando o usuario precisa escolher caminhos sem editar variaveis no codigo.

## Funcoes principais

- `selecionar_pasta`: abre janela para escolha de uma pasta.
- `selecionar_arquivo`: abre janela para escolha de um arquivo.

## Exemplo de uso

```python
from python_operacional.selecao_arquivos import selecionar_pasta, selecionar_arquivo

pasta = selecionar_pasta('Selecione a pasta de entrada')
arquivo = selecionar_arquivo('Selecione o arquivo de apoio')
```

## Cuidados

- Evitar este modulo em rotinas agendadas ou servidores sem interface grafica.
- Para automacoes sem janela, prefira argumentos de linha de comando.
- Nao misturar regra de negocio com selecao de caminho.

## Orientacao para IA

Antes de criar uma nova funcao de escolha de pasta ou arquivo, reutilize este modulo. Crie funcao nova somente se houver requisito diferente, como filtros de extensao, modo CLI ou selecao multipla.
