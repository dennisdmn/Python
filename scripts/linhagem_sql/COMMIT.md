# Histórico da ferramenta de linhagem SQL

## 1.2.0 — 10/11/2026

Adiciona a estimativa de dialeto por arquivo e registra no Excel tanto o `Dialeto provável` quanto o `Modo de análise`. A aba `Tabelas` passa a repetir essas informações em cada origem, destino ou tabela intermediária.

A detecção reconhece sinais específicos de Oracle, SQLite, SQL Server, PostgreSQL e MySQL/MariaDB. Comentários e literais são mascarados. Arquivos sem evidência suficiente permanecem como `Indeterminado`, e arquivos com sinais conflitantes são marcados como `Ambíguo`.

O marcador `<default>` continua preservado quando o SQL não informa schema. A versão também inclui `--versao` e documentação para analisar arquivos de dialetos diferentes em execuções separadas.

Validações realizadas:

- detecção positiva dos dialetos suportados;
- casos genéricos, ambíguos, comentários e literais;
- estrutura das abas `Resumo` e `Tabelas`;
- repetição de dialeto, modo e papel por tabela;
- execução real do exemplo SQLite em banco temporário;
- preservação de relatório Excel existente.

## 1.1.0 — 10/11/2026

Adiciona a exportação opcional para Excel com as abas `Resumo` e `Tabelas`, filtros, congelamento de cabeçalho, registro de erros e proteção contra sobrescrita.

Commit original: [`2b54249`](https://github.com/dennisdmn/Python/commit/2b542490741b11afd3623bfd98126b1a75e646fa).

## 1.0.0 — 10/11/2026

Cria o analisador de linhagem entre tabelas, com seleção de vários arquivos por janela ou linha de comando, suporte a dialeto e continuidade quando um arquivo falha.

Commit original: [`2116c3b`](https://github.com/dennisdmn/Python/commit/2116c3b38239fdc61d8b38a1b8fd88bcdff2a060).
