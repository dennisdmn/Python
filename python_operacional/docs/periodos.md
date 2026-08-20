# periodos.py

## Objetivo

Padronizar o calculo de periodos contabeis mensais representados por strings no formato `AAAAMM`.

## Quando usar

Use quando uma rotina precisar derivar o mes anterior a partir de um periodo de referencia, inclusive na virada de janeiro para dezembro do ano anterior.

## Funcao principal

- `periodo_anterior`: valida o periodo recebido e retorna o periodo mensal anterior.

## Exemplo de uso

```python
from python_operacional.periodos import periodo_anterior

periodo_ant_txt = periodo_anterior("202607")
print(periodo_ant_txt)  # 202606
```

## Validacoes

- A entrada deve ser uma string.
- A string deve conter exatamente seis digitos.
- O ano deve estar entre `0001` e `9999`.
- O mes deve estar entre `01` e `12`.
- Entradas invalidas geram `TypeError` ou `ValueError` com mensagem clara.

## Origem

A funcao foi generalizada a partir de uma rotina de calculo de IFRS 15 para permitir reuso em outros fechamentos e processos contabeis.
