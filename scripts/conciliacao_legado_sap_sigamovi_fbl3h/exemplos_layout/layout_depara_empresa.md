# Layout minimo - De-Para de Empresas

Referencia de layout para a tabela de equivalencia entre empresa do legado e divisao SAP.

## Colunas obrigatorias

- `MP_EMPRESA`
- `DIVISAO`

## Regras usadas

- `MP_EMPRESA` representa a empresa no padrao legado.
- `DIVISAO` representa a divisao no SAP.
- O script usa esta tabela para traduzir a empresa legado para a divisao SAP.
- Empresas sem mapeamento sao sinalizadas no terminal e nao entram no saldo legado conciliado.

## Boa pratica

Validar duplicidades de mapeamento antes de executar a rotina operacional.
