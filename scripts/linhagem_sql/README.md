# Linhagem de tabelas em arquivos SQL

**Versão atual: 1.2.0**

Use este script para responder rapidamente: **quais tabelas alimentam este resultado?** Ele lê um ou mais arquivos `.sql` locais em UTF-8, analisa o texto e mostra as tabelas de origem e destino no terminal e em um relatório Excel opcional. Não executa consultas, não se conecta ao banco e não altera os arquivos SQL.

## Instalação

Abra a raiz do repositório Python no VS Code. No terminal, instale a dependência no mesmo ambiente Python em que vai rodar o script:

```powershell
python -m pip install -r requirements/linhagem_sql.txt
```

A janela de seleção usa `tkinter`. Em um ambiente sem interface gráfica, informe os caminhos no terminal.

## Como usar

Para abrir o seletor, rode o comando abaixo. No Windows, use **Ctrl + clique** para marcar mais de um `.sql` e depois clique em **Abrir**. Após a análise, escolha onde salvar o `.xlsx`. Se cancelar essa segunda janela, o resultado fica no terminal.

```powershell
python scripts/linhagem_sql/analisar_linhagem.py
```

Para Oracle, use `--dialeto oracle`. O mesmo dialeto vale para todos os arquivos selecionados na execução; rode novamente para arquivos de outro dialeto.

```powershell
python scripts/linhagem_sql/analisar_linhagem.py --dialeto oracle
```

Sem abrir as janelas, passe um ou mais caminhos diretamente e use `--excel` para salvar a planilha. Sem essa opção, a execução por caminhos só escreve no terminal. Use aspas se o caminho tiver espaços.

```powershell
python scripts/linhagem_sql/analisar_linhagem.py scripts/linhagem_sql/exemplo_financeiro.sql --excel linhagem.xlsx
```

## O que sai no Excel

| Aba | Conteúdo |
| --- | --- |
| `Resumo` | Uma linha por arquivo, com dialeto provável, status, modo de análise, contagens e mensagem de erro, se houver. |
| `Tabelas` | Uma linha por tabela, com arquivo, dialeto provável, modo de análise e papel: origem, destino ou intermediária. |

As abas preenchidas têm filtros nos cabeçalhos. O ID do arquivo liga as duas abas, inclusive quando há arquivos de mesmo nome em pastas diferentes. Escolha uma pasta de saída separada para guardar os relatórios. O script não sobrescreve um `.xlsx` existente.

## Como conferir o resultado

No [exemplo financeiro](exemplo_financeiro.sql), as tabelas `financeiro.lancamentos` e `cadastro.empresas` aparecem como origens; `relatorios.resumo_por_empresa` é o destino. O `CREATE TABLE ... AS SELECT` conta como um comando. Um `SELECT` isolado pode ter origens sem destino declarado.

Cada arquivo tem seu próprio resultado. A ferramenta mostra quantos arquivos foram analisados e quantos deram erro. Se um falhar, ela continua com os demais e termina com código `1`, útil para automações. Ela não cruza dependências entre arquivos.

O [exemplo Oracle no repositório SQL](https://github.com/dennisdmn/SQL/tree/main/14-linhagem-de-dados) usa duas CTEs, filtro de datas e `NVL`. Para testá-lo, baixe o `.sql` e escolha-o na janela com o dialeto `oracle`.

O mesmo diretório contém um exemplo SQLite com CTEs, junções, agregação, função de janela e `julianday`. Analise-o em uma execução separada com `--dialeto sqlite`.

## Dialeto provável e modo de análise

`Dialeto provável` é uma estimativa do script. Ela procura sinais específicos de Oracle, SQLite, SQL Server, PostgreSQL e MySQL/MariaDB. Sintaxe comum a vários bancos aparece como `Indeterminado`; sinais de mais de um banco aparecem como `Ambíguo`. Comentários e literais são ignorados na detecção.

`Modo de análise` registra como o arquivo foi interpretado. Por exemplo, `SQLLineage (dialeto: sqlite)` significa que o argumento `--dialeto sqlite` foi usado. O mesmo argumento vale para todos os arquivos da execução; agrupe os arquivos por dialeto para obter resultados mais confiáveis.

As duas colunas podem divergir. Um arquivo pode ter `Dialeto provável = Oracle` e `Modo de análise = SQLLineage (dialeto: ansi)` quando foi executado sem `--dialeto oracle`.

## O marcador `<default>`

Quando uma tabela não tem schema no texto SQL, o SQLLineage pode mostrá-la como `<default>.nome_tabela`. `<default>` é um marcador de schema não informado, não um erro nem parte do nome real. O relatório preserva esse valor para não inventar um schema.

No SQLite, você pode qualificar uma tabela como `main.nome_tabela`. No Oracle, use `SCHEMA.NOME_TABELA` quando o schema for conhecido.

Para conferir a versão instalada:

```powershell
python scripts/linhagem_sql/analisar_linhagem.py --versao
```

## Limites e solução de erros

- Se aparecer `Modo didático (Python padrão)`, o `sqllineage` não foi encontrado nesse ambiente. O modo didático é restrito ao formato simples do exemplo (`CREATE TABLE ... AS SELECT` com `FROM` e `JOIN`). Para CTEs e sintaxes mais completas, instale a dependência.
- Se a exportação informar que o `xlsxwriter` está ausente, rode novamente a instalação de `requirements/linhagem_sql.txt` no mesmo Python que executa o script.
- A saída mostra **linhagem entre tabelas**. Não valida os saldos, a cardinalidade das junções ou se a execução teve sucesso no banco.
- A detecção de dialeto é heurística. `Indeterminado` é preferível a atribuir um banco sem evidência suficiente.
- SQL montado dinamicamente, variáveis que ainda não foram substituídas e views sem definição disponível podem esconder dependências. Revise o SQL gerado e analise os arquivos que definem essas views quando necessário.
