# Python

Repositorio pessoal de apoio geral para desenvolvimento em Python.

A ideia aqui nao e manter um unico projeto, e sim reunir material reutilizavel, exemplos, notas tecnicas, benchmarks, notebooks, modelos e casos de sucesso.

## Estrutura

- `docs/`: documentacao, notas tecnicas, comparativos e casos de sucesso
- `exemplos/`: exemplos curtos, didaticos e autocontidos
- `modelos/`: modelos simples e reutilizaveis para adaptar em projetos reais
- `scripts/`: scripts reutilizaveis e mais proximos de uso operacional
- `notebooks/`: exploracao, estudos e prototipos em Jupyter
- `benchmarks/`: comparacoes de desempenho reproduziveis
- `templates/`: modelos base para novos estudos e implementacoes
- `requirements/`: dependencias separadas por contexto

## Conteudo em destaque

### Exemplos rapidos

- [Indice de exemplos](./exemplos/README.md)
- [Exemplo: Leitura de Excel com pandas e openpyxl](./exemplos/excel/pandas_ler_excel_openpyxl.py)
- [Exemplo: Leitura de Excel com Polars e calamine](./exemplos/excel/polars_ler_excel_calamine.py)
- [Exemplo: Selecionar diretorio no Windows sem funcao](./exemplos/windows/exemplo_escolher_diretorio_sem_funcao.py)
- [Exemplo: Selecionar diretorio no Windows com funcao reutilizavel](./exemplos/windows/exemplo_escolher_diretorio_com_funcao.py)

### Modelos reutilizaveis

- [Modelo simples: Leitura de Excel com pandas e openpyxl](./modelos/leitura_excel_openpyxl_pandas.py)
- [Modelo: Leitura de Excel com Polars e calamine](./modelos/leitura_excel_polars.md)
- [Modelo basico: Escolher pasta pelo usuario](./modelos/escolher_pasta_basico.py)
- [Modelo: Selecao de entradas por CLI ou janela](./modelos/selecao_entradas_cli_janela.py)

### Padroes operacionais

- [Escolher pasta pelo usuario](./modelos/escolher_pasta_basico.py): modelo essencial para abrir uma janela local, selecionar uma pasta e retornar o caminho como `Path`.
- [Selecao de entradas por CLI ou janela](./modelos/selecao_entradas_cli_janela.py): modelo para scripts que precisam escolher pasta de entrada, pasta de saida e arquivo de apoio, com suporte a uso manual e automatizado.

### Notebooks

- [Benchmark: pandas/openpyxl vs Polars/calamine](./notebooks/benchmark_pandas_openpyxl_vs_polars_calamine.ipynb)

### Documentacao e casos de sucesso

- [Caso de Sucesso: Leitura de Excel com Polars](./docs/casos_sucesso/leitura_excel_polars.md)

## Como usar este repositorio

- use `exemplos/` para aprender uma tecnica isolada rapidamente
- use `modelos/` como ponto de partida para adaptar em rotinas reais
- use `docs/` para registrar contexto, decisoes tecnicas, comparativos e casos de sucesso
- use `scripts/` para codigos mais operacionais ou recorrentes
- use `notebooks/` para exploracao e prototipagem
- use `benchmarks/` para testes de desempenho reproduziveis
- use `templates/` para bases genericas de novos estudos ou implementacoes

## Organizacao de exemplos

Os exemplos ficam agrupados por tema dentro de `exemplos/`:

- `exemplos/excel/`: leitura e manipulacao de planilhas
- `exemplos/windows/`: automacoes e interacoes locais especificas do Windows

## Diretriz de organizacao

Prefira nomear arquivos pelo assunto e objetivo, evitando nomes vagos como `teste`, `final` e `v2`.
