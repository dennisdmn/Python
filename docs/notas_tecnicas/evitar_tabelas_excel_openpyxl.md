# Nota tecnica - Evitar tabelas internas do Excel com openpyxl

## Contexto

Em arquivos grandes gerados por Python, o Excel pode abrir a planilha em modo de reparo quando encontra inconsistencias em tabelas internas do workbook.

O reparo normalmente informa remocao de recursos relacionados a `xl/tables/table*.xml`.

## Diretriz operacional

Para evidencias de conciliacao e arquivos de auditoria, priorize estabilidade de abertura no Excel.

Padrao recomendado:

- usar cabecalho simples;
- evitar objeto `Table` do Excel;
- evitar `AutoFilter` automatico;
- evitar celulas mescladas;
- congelar painel quando necessario;
- formatar somente o essencial.

## Por que evitar mesclas

Celulas mescladas dificultam leitura por:

- pandas;
- Power Query;
- validadores automaticos;
- assistentes de IA;
- processos de reconciliacao automatizada.

## Padrao seguro

1. Escrever o DataFrame com `to_excel`.
2. Reabrir com `openpyxl` somente para formatacao leve.
3. Aplicar titulo em celulas simples.
4. Nao criar tabela interna.
5. Salvar o workbook.

## Checklist para IA

Ao gerar ou modificar scripts de Excel operacional, uma IA deve perguntar:

- O arquivo precisa ser apenas evidencia ou tambem interface de analise?
- O Excel corporativo abre arquivos com tabelas internas sem reparo?
- O output sera consumido por Power Query ou pandas?
- Ha necessidade real de mesclar celulas?
- O ganho visual compensa o risco de corrupcao do workbook?
