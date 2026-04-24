# Caso de Sucesso: Leitura de Excel com Polars

## Contexto
O projeto de conciliacao contabil precisava ler multiplos arquivos `.xlsx` da pasta `_Bases_Razoes` e consolidar os dados em um unico DataFrame.

A abordagem inicial com `pandas` e `openpyxl` apresentou desempenho abaixo do necessario, principalmente na leitura dos arquivos e na consolidacao final em memoria.

## Problema
Os gargalos observados foram:

- leitura lenta dos arquivos `.xlsx`
- tempo elevado para consolidar varios arquivos
- custo desnecessario ao carregar mais dados do que o necessario

## Abordagem inicial
A implementacao inicial utilizava `pandas.read_excel(...)` com engine `openpyxl`, lendo a aba necessaria e as colunas de interesse.

Exemplo simplificado:

```python
import pandas as pd
from pathlib import Path

PASTA_BASES = Path(r"C:\Python\Projeto_Conciliacao_Contabil\_Bases_Razoes")
ABA = "Exportação SAPUI5"
COLUNAS = ["Conta do Razão", "Mont.moeda empresa"]

arquivos = sorted(PASTA_BASES.glob("*.xlsx"))
dataframes = []

for arquivo in arquivos:
    df = pd.read_excel(
        arquivo,
        sheet_name=ABA,
        usecols=COLUNAS,
        engine="openpyxl"
    )
    dataframes.append(df)

if dataframes:
    df_final = pd.concat(dataframes, ignore_index=True)
```

## Solucao aplicada
A solucao adotada foi substituir `pandas + openpyxl` por `polars` com `engine="calamine"`.

Principais mudancas:

- uso de `Polars` para processamento tabular
- uso de `calamine` para leitura mais eficiente de Excel
- leitura de apenas uma aba especifica
- leitura de apenas duas colunas necessarias
- concatenacao unica no final com `pl.concat(...)`

Codigo utilizado:

```python
import polars as pl
from pathlib import Path
from time import perf_counter
from tqdm import tqdm

PASTA_BASES = Path(r"C:\Python\Projeto_Conciliacao_Contabil\_Bases_Razoes")
ABA = "Exportação SAPUI5"
COLUNAS = ["Conta do Razão", "Mont.moeda empresa"]

def processar_razoes_polars():
    arquivos = sorted(PASTA_BASES.glob("*.xlsx"))
    if not arquivos:
        print("Nenhum arquivo encontrado na pasta especificada.")
        return None

    print(f"Processando {len(arquivos)} arquivos com Polars...")
    inicio = perf_counter()

    dataframes = []

    for arquivo in tqdm(arquivos, desc="Lendo Excel", unit="arq"):
        df = pl.read_excel(
            arquivo,
            sheet_name=ABA,
            columns=COLUNAS,
            engine="calamine"
        )

        dataframes.append(df)

    if not dataframes:
        print("Nenhum dataframe valido foi carregado.")
        return None

    df_final = pl.concat(dataframes)

    fim = perf_counter()

    print("\n" + "=" * 30)
    print(f"Arquivos lidos: {len(arquivos)}")
    print(f"Linhas totais: {df_final.height}")
    print(f"Tempo de execucao: {fim - inicio:.2f} segundos")
    print("=" * 30)

    return df_final


df_razao = processar_razoes_polars()
if df_razao is not None:
    print(df_razao.head())
```

## Por que ficou mais rapido
O ganho de desempenho veio de quatro pontos objetivos:

- `Polars` tem processamento tabular mais eficiente do que `pandas` em muitas cargas de leitura e consolidacao
- `calamine` e mais rapido para leitura de Excel do que `openpyxl` neste caso de uso
- a leitura foi limitada a uma unica aba
- a leitura foi limitada apenas as colunas necessarias
- a consolidacao foi feita uma unica vez ao final

## Resultado pratico
A nova abordagem resolveu os gargalos de leitura e de agregacao em memoria para a etapa inicial do projeto.

Beneficios observados:

- menor tempo total de leitura dos arquivos `.xlsx`
- consolidacao mais rapida em um unico DataFrame
- codigo simples para benchmark da ingestao
- base melhor para a proxima etapa de carga no SQLite

## Dependencias
Para essa abordagem funcionar, as dependencias principais sao:

```bash
pip install polars fastexcel tqdm
```

Observacao:

- `engine="calamine"` em `pl.read_excel(...)` depende de `fastexcel`

## Conclusao
Para a etapa de ingestao inicial dos arquivos Excel, a combinacao `polars + calamine` se mostrou mais adequada do que `pandas + openpyxl` quando o objetivo principal e performance.

Essa abordagem passa a ser uma boa referencia para leitura basica dos arquivos antes da persistencia no SQLite.
