# Layout minimo - De-Para de Contas

Referencia de layout para a tabela de equivalencia entre contas do legado e contas SAP.

## Colunas obrigatorias

- `MP_CONTA`
- `CONTA`

## Regras usadas

- `MP_CONTA` representa a conta no padrao legado.
- `CONTA` representa a conta no padrao SAP.
- O script usa esta tabela para traduzir a conta SAP para a conta legado.
- Contas SAP sem mapeamento nao entram no saldo SAP conciliado.

## Boa pratica

Manter uma unica linha por par de equivalencia e revisar duplicidades antes de executar a rotina.
