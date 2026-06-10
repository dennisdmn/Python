# Descrição estendida — Inspecionar cabeçalho XLSX com openpyxl

## Contexto

Em rotinas de dados, controladoria, conciliação, cargas contábeis e validação de arquivos, é comum receber planilhas Excel com múltiplas abas e estruturas variáveis. Antes de tratar o conteúdo, muitas vezes é necessário entender rapidamente quais abas existem e quais são os campos disponíveis em cada uma delas.

Este exemplo foi criado para fazer essa inspeção inicial de forma simples e segura.

## O que o script faz

O script abre um arquivo `.xlsx` com `openpyxl` em modo somente leitura e percorre todas as abas do workbook.

Para cada aba, ele imprime:

| Informação | Descrição |
|---|---|
| Nome da aba | Nome da planilha dentro do arquivo Excel |
| Colunas | Quantidade de colunas identificadas na primeira linha |
| Linhas | Quantidade estimada de linhas de dados, desconsiderando o cabeçalho |
| Cabeçalho | Lista numerada dos nomes das colunas |

## Trechos principais

Carregamento do arquivo:

```python
wb = openpyxl.load_workbook(arquivo, read_only=True, data_only=True)
```

Leitura das abas:

```python
print(f"Abas    : {wb.sheetnames}")
```

Leitura do cabeçalho da primeira linha:

```python
cabecalho = [cell.value for cell in next(ws.iter_rows(max_row=1))]
```

Fechamento do arquivo:

```python
wb.close()
```

## Por que usar read_only=True

O parâmetro `read_only=True` reduz o consumo de memória e torna a abertura do arquivo mais leve, especialmente em planilhas grandes. Isso é útil quando o objetivo é apenas inspecionar a estrutura, sem editar ou carregar todo o conteúdo em memória.

## Por que usar data_only=True

O parâmetro `data_only=True` permite retornar os valores calculados das células com fórmula, quando esses valores já estão salvos no arquivo Excel. Para inspeção de cabeçalho, esse parâmetro normalmente não impacta muito, mas mantém o comportamento mais próximo do que o usuário enxerga no Excel.

## Limitações conhecidas

- A contagem de linhas é estimada com `ws.max_row - 1`.
- `ws.max_row` pode considerar células formatadas ou usadas anteriormente, dependendo do arquivo.
- O script considera que a primeira linha de cada aba contém o cabeçalho.
- O script não valida tipos de dados.
- O script não identifica colunas obrigatórias ou vazias.

## Melhorias futuras sugeridas

1. Receber o caminho do arquivo por argumento de linha de comando.
2. Permitir escolher uma aba específica.
3. Exportar a estrutura das abas para `.xlsx`, `.csv` ou `.json`.
4. Validar colunas obrigatórias.
5. Comparar o cabeçalho encontrado com um layout esperado.
6. Identificar colunas duplicadas.
7. Identificar cabeçalhos vazios.
8. Gerar relatório de inconsistências.
9. Integrar com rotinas de validação de arquivos antes da carga.

## Status

Versão inicial funcional, indicada para inspeção rápida de arquivos Excel `.xlsx`.
