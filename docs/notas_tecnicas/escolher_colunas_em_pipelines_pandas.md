# Nota tecnica - Escolher colunas em pipelines pandas

## Contexto

Em rotinas operacionais, escolher colunas e uma etapa recorrente antes de validar layout, reduzir memoria, padronizar bases ou gerar evidencias.

## Boas praticas

- definir explicitamente as colunas desejadas;
- validar colunas obrigatorias antes de recortar a base;
- preservar a ordem das colunas no output;
- criar uma copia com `.copy()` para evitar efeitos colaterais;
- separar colunas obrigatorias de colunas opcionais.

## Padrao recomendado

```python
colunas_desejadas = ['EMPRESA', 'CONTA', 'VALOR']
base = df.loc[:, colunas_desejadas].copy()
```

## Quando usar

- leitura de Excel com muitas colunas;
- bases SAP com campos excedentes;
- bases legado com campos auxiliares;
- preparacao de evidencia;
- padronizacao antes de joins e conciliacoes.

## Uso por IA

Ao criar novos scripts, uma IA deve procurar primeiro por modelos de escolha de colunas antes de escrever selecoes manuais repetidas dentro do codigo principal.
