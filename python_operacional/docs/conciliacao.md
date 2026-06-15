# conciliacao.py

## Objetivo

Concentrar funcoes genericas de conciliacao entre duas bases por chaves comuns.

## Quando usar

Use em processos que precisam comparar saldos, quantidades ou valores entre duas origens.

## Funcoes principais

- `full_outer_conciliacao`: compara duas bases por full outer join.
- `agregar_saldo`: agrega uma base por chaves e soma uma coluna de valor.

## Exemplo de uso

```python
from python_operacional.conciliacao import full_outer_conciliacao

resultado = full_outer_conciliacao(
    base_a,
    base_b,
    chaves=['EMPRESA', 'CONTA'],
    valor_a='SALDO_A',
    valor_b='SALDO_B',
)
```

## Cuidados

- Validar chaves antes da conciliacao.
- Agregar bases antes do confronto final.
- Evitar chaves textuais instaveis quando existir chave composta mais confiavel.
- Documentar regra de sinal antes de comparar valores.

## Orientacao para IA

Antes de criar um merge de conciliacao do zero, reutilize este modulo. A regra de negocio deve ficar no script operacional, nao neste modulo generico.
