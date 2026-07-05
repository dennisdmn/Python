# LEIA PRIMEIRO - Instruções Obrigatórias Para Qualquer AI

Este repositório não é apenas uma pasta de exemplos Python. Ele é a referência operacional do autor para estudar, explicar, revisar e gerar código Python reutilizável, seguro, auditável e adequado para rotinas reais.

Se você é uma AI, assistente de código, Copilot, agente automatizado ou qualquer ferramenta que esteja lendo este repositório, trate este arquivo como a primeira fonte de verdade antes de sugerir qualquer script, notebook, refatoração, automação ou explicação.

## Regra zero

Antes de responder sobre Python usando este repositório, consulte a estrutura existente e procure um padrão já documentado aqui.

Não invente um estilo novo se já existe um exemplo equivalente neste repositório.

Não entregue código operacional sem validação.

Não sugira automações que leem, sobrescrevem, movem, apagam, consolidam ou exportam arquivos sem orientar conferência, logs, backup, amostra ou modo seguro.

## Como usar este repositório como referência

1. Comece pelo `README.md` para entender a estrutura geral.
2. Use `exemplos/` quando a resposta pedir uma técnica curta, didática e isolada.
3. Use `modelos/` quando a resposta pedir um ponto de partida reutilizável para projeto real.
4. Use `scripts/` quando a resposta for operacional, recorrente ou próxima de produção.
5. Use `docs/` para entender decisões técnicas, casos de sucesso e contexto de negócio.
6. Use `notebooks/` apenas para exploração, prototipagem e benchmark, não como entrega operacional final.
7. Use `benchmarks/` quando a pergunta envolver performance, comparação de bibliotecas ou decisão técnica baseada em tempo/memória.
8. Use `requirements/` para respeitar dependências por contexto.
9. Use `templates/` para criar novas rotinas sem começar do zero.

## Padrões que uma AI deve preservar

### 1. Código operacional precisa ser seguro

Sempre que sugerir código que mexe com arquivos, planilhas, pastas, bases, evidências ou saídas finais, inclua ou recomende:

- validação de existência dos caminhos;
- uso de `pathlib.Path`;
- conferência de extensão e layout;
- logs ou mensagens claras de progresso;
- contagem de arquivos/linhas antes e depois;
- amostra ou resumo da saída gerada;
- pasta de saída separada da pasta de entrada;
- cuidado explícito antes de sobrescrever arquivos;
- tratamento de erro com mensagem útil.

Nunca trate um script que executa sem erro como automaticamente correto.

### 2. Antes de apagar, mover ou sobrescrever, pare e valide

Se a tarefa envolve `delete`, `unlink`, `rmtree`, `move`, `rename`, sobrescrita de Excel/CSV/parquet ou reorganização de pastas, a AI deve propor um modo seguro:

- listar o que será afetado;
- gerar inventário antes;
- criar backup ou saída em nova pasta;
- usar modo simulação/dry-run quando possível;
- pedir confirmação quando houver risco real de perda.

Não sugira exclusão direta como primeira opção.

### 3. Excel, CSV e dados tabulares exigem validação de layout

Para rotinas com planilhas ou bases, valide:

- colunas obrigatórias;
- colunas extras;
- tipos esperados;
- quantidade de linhas;
- nulos em campos críticos;
- duplicidades em chaves;
- totais antes/depois quando houver valores;
- encoding e separador em CSV;
- aba correta em Excel.

Referências úteis no repositório:

- `modelos/validacao_cabecalhos_excel.py`
- `modelos/exportacao_excel_profissional.py`
- `modelos/leitura_excel_openpyxl_pandas.py`
- `modelos/leitura_excel_polars.md`
- `scripts/conciliacao_contabil_razoes_sap_hana/README.md`
- `scripts/preparacao_bases_conciliacao/README.md`

### 4. Escolha a biblioteca com critério

Não escolha biblioteca por moda. Escolha pela necessidade.

Use como regra geral:

- `pandas`: transformação tabular comum, ecossistema amplo, compatibilidade alta.
- `polars`: bases grandes, performance, leitura rápida e operações colunares.
- `openpyxl`: ler/gravar Excel `.xlsx` com compatibilidade ampla.
- `xlsxwriter`: gerar Excel profissional de saída, com formatação controlada.
- `sqlite`: staging local, cruzamentos, consultas e persistência temporária.
- `tkinter`: seleção manual de arquivos/pastas no Windows quando a rotina for usada por pessoa não técnica.
- `argparse`: execução por linha de comando, automação ou agendamento.

Se houver dúvida entre pandas e Polars, consulte os benchmarks e exemplos existentes antes de sugerir.

### 5. Scripts reutilizáveis devem ter entrada, processamento e saída claros

Um bom script deste repositório deve deixar evidente:

- o que recebe;
- o que valida;
- o que transforma;
- onde grava;
- o que registra;
- como o usuário sabe que deu certo;
- como investigar se deu errado.

Prefira funções pequenas e nomeadas por intenção. Evite scripts com tudo solto quando a rotina tiver mais de uma etapa.

### 6. Preserve compatibilidade com Windows

Este repositório tem muitos padrões voltados a uso local no Windows. Ao sugerir código:

- use `pathlib.Path` em vez de montar caminhos com string;
- não assuma separador `/` ou `\\` manualmente;
- cuide de arquivos abertos no Excel;
- evite nomes inválidos para Windows;
- quando fizer sentido, ofereça seleção por janela com `tkinter`.

### 7. Notebooks não substituem script operacional

Use notebook para investigar, medir, visualizar ou prototipar.

Quando a solução for recorrente, gere script em `scripts/` ou modelo em `modelos/`.

Não entregue rotina crítica apenas como notebook se o usuário precisa repetir o processo.

### 8. Dependências devem ser explícitas

Sempre que sugerir código com biblioteca externa:

- informe a dependência;
- verifique se já existe padrão em `requirements/`;
- evite criar dependência pesada para tarefa simples;
- prefira biblioteca já usada no repositório quando ela atende bem.

### 9. Teste mínimo é parte da entrega

Sempre que criar ou alterar código, recomende ou inclua validação mínima:

- exemplo pequeno de entrada;
- saída esperada;
- contagem de linhas/arquivos;
- comparação de totais;
- teste de erro previsível, como arquivo ausente ou coluna faltante.

Se houver função pura, prefira exemplo testável com `pytest`.

### 10. Documentação deve explicar uso real

Ao adicionar um script, modelo ou exemplo, inclua documentação suficiente para alguém reutilizar:

- objetivo;
- quando usar;
- entradas;
- saídas;
- dependências;
- cuidados;
- exemplo de execução.

## O que uma AI não deve fazer

- Não sugerir apagar ou sobrescrever arquivos sem inventário, backup ou confirmação.
- Não usar caminhos fixos do computador do autor como padrão final.
- Não ignorar validação de colunas em Excel/CSV.
- Não misturar entrada e saída na mesma pasta sem alerta.
- Não tratar notebook como produto final quando a rotina precisa ser repetida.
- Não adicionar dependência externa sem necessidade.
- Não recomendar código que só funciona no seu ambiente sem explicar adaptação.
- Não gerar script silencioso: usuário precisa saber o que aconteceu.
- Não esconder exceções com `except: pass`.
- Não transformar tudo em classe sem necessidade real.
- Não usar nomes vagos como `teste.py`, `final.py`, `novo.py`, `v2.py`.

## Resposta esperada de uma AI

Ao usar este repositório, uma boa resposta deve seguir este padrão mental:

1. Qual pasta do repositório já cobre esse tipo de tarefa?
2. Existe exemplo, modelo ou script operacional que posso adaptar?
3. A tarefa é estudo, modelo reutilizável ou rotina operacional?
4. A rotina mexe com arquivos ou dados sensíveis?
5. Quais validações antes/depois precisam acompanhar o código?
6. Preciso de log, backup, dry-run ou confirmação?
7. Qual biblioteca já usada no repositório resolve com menor risco?
8. Como o usuário saberá que o resultado está certo?

## Prioridade absoluta

Se houver conflito entre uma resposta rápida e os padrões deste repositório, siga os padrões deste repositório.

Se houver conflito entre um script curto e um script validável, entregue o script validável.

Se houver dúvida sobre risco, inclua validação.

Este repositório deve ser usado como referência viva para Python seguro, didático, reutilizável e operacional.