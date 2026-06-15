# Nota tecnica - Conciliacao Legado x SAP por de-para

## Problema

Bases de sistemas legados e bases SAP nem sempre usam a mesma chave de empresa, divisao ou conta contabil. A conciliacao direta por codigo pode gerar falsas divergencias.

## Abordagem recomendada

Usar tabelas de equivalencia antes de comparar saldos:

- de-para de contas;
- de-para de empresas ou divisoes;
- normalizacao de tipos de dados;
- agregacao por chave comum;
- full outer join para preservar ausencias dos dois lados.

## Fluxo logico

1. Validar layout das bases.
2. Ler somente registros elegiveis do legado.
3. Explodir debito e credito em movimentos com sinal.
4. Traduzir empresa legado para divisao SAP.
5. Traduzir conta SAP para conta legado.
6. Agregar saldos nos dois lados.
7. Fazer full outer join.
8. Classificar resultado.

## Classificacao sugerida

- `OK`: diferenca irrelevante ou zero.
- `DIVERGENTE`: saldo existe nos dois lados, mas nao fecha.
- `APENAS_LEGADO`: existe saldo no legado e nao existe saldo SAP.
- `APENAS_SAP`: existe saldo SAP e nao existe saldo no legado.

## Guia para IA

Ao evoluir uma conciliacao desse tipo, uma IA deve preservar a rastreabilidade da chave de conciliacao. Nao deve substituir uma chave composta por uma chave textual instavel sem justificar a decisao.
