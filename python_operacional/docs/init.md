# __init__.py

## Objetivo

Declarar `python_operacional/` como pacote Python e listar os modulos publicos esperados.

## Quando usar

Este arquivo e usado automaticamente pelo Python ao importar o pacote.

## Conteudo esperado

- Docstring breve do pacote.
- Lista `__all__` com modulos que compoem a biblioteca operacional.

## Cuidados

- Atualizar `__all__` quando um novo modulo publico for criado.
- Nao colocar regra de negocio neste arquivo.
- Evitar imports pesados no carregamento inicial do pacote.

## Orientacao para IA

Ao adicionar novo modulo em `python_operacional/`, verificar se ele deve entrar no `__all__` e se precisa de documentacao propria em `python_operacional/docs/`.
