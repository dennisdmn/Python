# Layout minimo - Sigamovi

Referencia de layout minimo para a base Sigamovi usada na conciliacao.

## Colunas obrigatorias

- `SGMOVIEMPRESA`
- `SGMOVIFILIAL`
- `EMPRESA`
- `SGMOVIDEBITO`
- `SGMOVICREDITO`
- `SUM_of_SGMOVIVALOR`
- `SGMOVICCD`
- `SGMOVIROTINA`
- `SGMOVIGERADO`
- `IUNICODEMPRESA`
- `SGMOVANO`
- `SGMOVMES`

## Regras usadas

- `SGMOVIGERADO = S` entra na conciliacao.
- Debito entra com sinal positivo.
- Credito entra com sinal negativo.
- A competencia vem de `SGMOVANO` e `SGMOVMES`.
