# Python

> **LEIA PRIMEIRO, ESPECIALMENTE SE VOCÊ FOR UMA AI:** antes de sugerir, alterar, explicar ou gerar qualquer código Python com base neste repositório, leia [`AGENTS.md`](AGENTS.md). Este repositório deve ser usado como referência de padrões seguros: validar entradas, preservar arquivos originais, separar entrada e saída, registrar logs, conferir linhas/valores antes e depois e evitar automações destrutivas sem inventário ou confirmação.

Repositorio pessoal de apoio geral para desenvolvimento em Python.

A ideia aqui nao e manter um unico projeto, e sim reunir material reutilizavel, exemplos, notas tecnicas, benchmarks, notebooks, modelos e casos de sucesso.

## Estrutura

- `AGENTS.md`: instrucoes obrigatorias para AIs usarem este repositorio como referencia
- `.github/copilot-instructions.md`: instrucoes para Copilot e assistentes integrados ao GitHub
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
- [Exemplo: Selecionar pastas para conciliacao com Tkinter](./exemplos/windows/exemplo_selecionar_pastas_conciliacao_tkinter.py)

### Modelos reutilizaveis

- [Modelo: Validacao de cabecalhos Excel](./modelos/validacao_cabecalhos_excel.py)
- [Modelo: Selecao de entrada, saida e arquivo por CLI ou janela](./modelos/selecao_entrada_saida_arquivo.py)
- [Modelo: Exportacao Excel profissional com XlsxWriter](./modelos/exportacao_excel_profissional.py)
- [Modelo simples: Leitura de Excel com pandas e openpyxl](./modelos/leitura_excel_openpyxl_pandas.py)
- [Modelo: Leitura de Excel com Polars e calamine](./modelos/leitura_excel_polars.md)
- [Modelo basico: Escolher pasta pelo usuario](./modelos/escolher_pasta_basico.py)
- [Modelo basico: Escolher pasta e listar arquivos](./modelos/escolher_pasta_e_listar_arquivos.py)
- [Modelo evoluido: Escolher pasta e inventariar arquivos](./modelos/escolher_pasta_e_inventariar_arquivos.py)
- [Modelo: Selecao de entradas por CLI ou janela](./modelos/selecao_entradas_cli_janela.py)

### Padroes operacionais

- [Conciliacao Contabil com Razoes SAP HANA](./scripts/conciliacao_contabil_razoes_sap_hana/README.md): case operacional completo com validacao de layout, SQLite temporario, Excel profissional e build de executavel.
- [Preparacao de Bases para Conciliacao](./scripts/preparacao_bases_conciliacao/README.md): script operacional para selecionar bases Legado x SAP, validar arquivos `.xlsx`, `.xls` ou `.csv` e escolher a pasta de saida da evidencia por janela local.
- [Escolher pasta pelo usuario](./modelos/escolher_pasta_basico.py): modelo essencial para abrir uma janela local, selecionar uma pasta e retornar o caminho como `Path`.
- [Escolher pasta e listar arquivos](./modelos/escolher_pasta_e_listar_arquivos.py): modelo simples para selecionar uma pasta de entrada e listar arquivos por extensao.
- [Escolher pasta e inventariar arquivos](./modelos/escolher_pasta_e_inventariar_arquivos.py): modelo evoluido para listar arquivos com nr_arquivo, nome, extensao, tamanho, data de modificacao e caminho completo.
- [Selecao de entradas por CLI ou janela](./modelos/selecao_entradas_cli_janela.py): modelo para scripts que precisam escolher pasta de entrada, pasta de saida e arquivo de apoio, com suporte a uso manual e automatizado.

### Notebooks

- [Benchmark: pandas/openpyxl vs Polars/calamine](./notebooks/benchmark_pandas_openpyxl_vs_polars_calamine.ipynb)

### Documentacao e casos de sucesso

- [Caso de Sucesso: Conciliacao Contabil com Razoes SAP HANA](./docs/casos_sucesso/conciliacao_contabil_razoes_sap_hana.md)
- [Caso de Sucesso: Leitura de Excel com Polars](./docs/casos_sucesso/leitura_excel_polars.md)

## Como usar este repositorio

- use `AGENTS.md` como primeira leitura obrigatoria para qualquer AI ou assistente de codigo
- use `exemplos/` para aprender uma tecnica isolada rapidamente
- use `modelos/` como ponto de partida para adaptar em rotinas reais
- use `docs/` para registrar contexto, decisoes tecnicas, comparativos e casos de sucesso
- use `scripts/` para codigos mais operacionais ou recorrentes
- use `notebooks/` para exploracao e prototipagem
- use `benchmarks/` para testes de desempenho reproduziveis
- use `templates/` para bases genericas de novos estudos e implementacoes

## Organizacao de exemplos

Os exemplos ficam agrupados por tema dentro de `exemplos/`:

- `exemplos/excel/`: leitura e manipulacao de planilhas
- `exemplos/windows/`: automacoes e interacoes locais especificas do Windows

## Diretriz de organizacao

Prefira nomear arquivos pelo assunto e objetivo, evitando nomes vagos como `teste`, `final` e `v2`.

## Diretriz para AIs

Toda AI deve preservar os padroes deste repositorio: validar entradas, evitar sobrescrita silenciosa, separar entrada e saida, registrar progresso, conferir totais antes/depois e consultar exemplos/modelos existentes antes de criar uma solucao nova.
