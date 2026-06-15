# Layout minimo - SAP FBL3H

Referencia de layout minimo para razao SAP/FBL3H usado na conciliacao.

## Colunas obrigatorias

- Empresa
- Exercicio
- Periodo contabil
- Tipo de documento
- Conta do Razao
- Conta do Razao: texto breve
- Codigo da moeda empresa
- Valor em moeda da empresa
- Referencia
- Divisao

## Regras usadas

- O arquivo principal deve conter tipo de documento OI.
- A referencia deve indicar a origem da integracao.
- O arquivo de correcao e opcional.
- A conta SAP e traduzida para conta legado pelo de-para de contas.
- A divisao SAP e usada como chave de empresa no lado SAP.
