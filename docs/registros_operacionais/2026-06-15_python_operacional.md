# Registro operacional - criacao da biblioteca python_operacional

## Resumo

Criacao da pasta `python_operacional/` para centralizar blocos reutilizaveis usados em scripts operacionais de controladoria, conciliacao, leitura de bases, validacao de layouts e geracao de evidencias.

## Motivacao

Evitar que rotinas recorrentes sejam reescritas em cada novo desenvolvimento, especialmente:

- escolher pasta;
- escolher arquivo;
- inventariar diretorios;
- validar layouts;
- escolher colunas;
- ler arquivos Excel com pandas;
- ler arquivos Excel com Polars e fastexcel;
- processar varios arquivos em looping;
- usar SQLite como camada temporaria;
- exportar Excel seguro;
- ordenar abas;
- conciliar bases por chaves.

## Escopo implementado

Foram criados modulos em `python_operacional/` para:

- selecao de arquivos e pastas;
- inventario de pastas;
- validacao de layouts;
- escolha e normalizacao de colunas;
- leitura Excel com pandas/openpyxl;
- leitura Excel com Polars/calamine/fastexcel;
- staging SQLite;
- exportacao Excel sem estrutura de tabela interna;
- conciliacao generica com full outer join;
- catalogo de blocos para consulta por pessoas e assistentes de IA.

## Decisoes tecnicas

1. `scripts/` deve concentrar regra de negocio.
2. `python_operacional/` deve concentrar blocos genericos reutilizaveis.
3. Outputs Excel operacionais devem evitar `Table`, `AutoFilter` e celulas mescladas quando o foco for estabilidade.
4. Polars com engine `calamine` deve ser considerado para leitura rapida de Excel quando a base for grande.
5. SQLite deve ser considerado como camada temporaria quando a base pressionar memoria ou exigir consultas intermediarias.

## Uso por IA

Antes de escrever codigo novo, uma IA deve consultar:

1. `python_operacional/catalogo.md`;
2. `python_operacional/README.md`;
3. modelos em `modelos/`;
4. exemplos em `exemplos/`;
5. notas tecnicas em `docs/notas_tecnicas/`.

A IA deve reutilizar blocos existentes sempre que a necessidade operacional ja estiver coberta.

## Criterio de aceite

- A pasta `python_operacional/` existe.
- O catalogo referencia as principais necessidades operacionais.
- Existem modulos para pandas, Polars/fastexcel e SQLite.
- Existe arquivo de requirements especifico.
- A documentacao explica o uso por IA.

## Observacao

Este registro corrige a falta de uma descricao estendida consolidada para as alteracoes criadas inicialmente em commits pequenos.
