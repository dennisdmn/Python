# Linhagem de tabelas em arquivos SQL

Use este script para responder rapidamente: **quais tabelas alimentam este resultado?** Ele lê um ou mais arquivos `.sql` locais em UTF-8, analisa o texto e mostra as tabelas de origem e destino no terminal. Não executa consultas, não se conecta ao banco e não altera os arquivos.

## Instalação

Abra a raiz do repositório Python no VS Code. No terminal, instale a dependência no mesmo ambiente Python em que vai rodar o script:

```powershell
python -m pip install -r requirements/linhagem_sql.txt
```

A janela de seleção usa `tkinter`. Em um ambiente sem interface gráfica, informe os caminhos no terminal.

## Como usar

Para abrir o seletor, rode o comando abaixo. No Windows, use **Ctrl + clique** para marcar mais de um `.sql` e depois clique em **Abrir**.

```powershell
python scripts/linhagem_sql/analisar_linhagem.py
```

Para Oracle, use `--dialeto oracle`. O mesmo dialeto vale para todos os arquivos selecionados na execução; rode novamente para arquivos de outro dialeto.

```powershell
python scripts/linhagem_sql/analisar_linhagem.py --dialeto oracle
```

Sem abrir a janela, você pode passar um ou mais caminhos diretamente. Use aspas se o caminho tiver espaços.

```powershell
python scripts/linhagem_sql/analisar_linhagem.py scripts/linhagem_sql/exemplo_financeiro.sql
```

## Como conferir o resultado

No [exemplo financeiro](exemplo_financeiro.sql), as tabelas `financeiro.lancamentos` e `cadastro.empresas` aparecem como origens; `relatorios.resumo_por_empresa` é o destino. O `CREATE TABLE ... AS SELECT` conta como um comando. Um `SELECT` isolado pode ter origens sem destino declarado.

Cada arquivo tem seu próprio resultado. A ferramenta mostra quantos arquivos foram analisados e quantos deram erro. Se um falhar, ela continua com os demais e termina com código `1`, útil para automações. Ela não cruza dependências entre arquivos.

O [exemplo Oracle no repositório SQL](https://github.com/dennisdmn/SQL/tree/main/14-linhagem-de-dados) usa duas CTEs, filtro de datas e `NVL`. Para testá-lo, baixe o `.sql` e escolha-o na janela com o dialeto `oracle`.

## Limites e solução de erros

- Se aparecer `Modo didático (Python padrão)`, o `sqllineage` não foi encontrado nesse ambiente. O modo didático é restrito ao formato simples do exemplo (`CREATE TABLE ... AS SELECT` com `FROM` e `JOIN`). Para CTEs e sintaxes mais completas, instale a dependência.
- A saída mostra **linhagem entre tabelas**. Não valida os saldos, a cardinalidade das junções ou se a execução teve sucesso no banco.
- SQL montado dinamicamente, variáveis que ainda não foram substituídas e views sem definição disponível podem esconder dependências. Revise o SQL gerado e analise os arquivos que definem essas views quando necessário.
