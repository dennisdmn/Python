# Conciliacao Contabil com Razoes SAP HANA

Case de automacao em Python para validar arquivos Excel extraidos do SAP HANA, consolidar razoes contabeis, confrontar com balancete e gerar uma evidencia profissional em Excel.

Este material foi organizado como exemplo reutilizavel para projetos Python operacionais: entrada por CLI ou janela, validacao de layout, processamento incremental com SQLite temporario, geracao de Excel com multiplas abas e empacotamento em executavel.

## O que este case demonstra

- selecao obrigatoria de pasta de entrada, pasta de saida e arquivo de balancete;
- validacao de cabecalhos criticos e opcionais;
- leitura eficiente de multiplos arquivos `.xlsx`;
- uso de SQLite temporario para reduzir pressao de memoria;
- aplicacao de regra contabil de inversao de sinal por classe de conta;
- normalizacao do balancete SAP HANA;
- conciliacao entre balancete e razoes agrupados;
- geracao de workbook Excel com menu, tabelas, totais, links e formatacao;
- build de executavel com PyInstaller para usuario final no Windows.

## Arquivos principais

- `conciliacao_contabil_razoes.py`: script principal do case.
- `build_executavel.ps1`: script PowerShell para gerar executavel via PyInstaller.
- `requirements/conciliacao_contabil_razoes.txt`: dependencias de execucao.
- `requirements/build_executavel.txt`: dependencias de build.

## Como executar em Python

```powershell
python .\scripts\conciliacao_contabil_razoes_sap_hana\conciliacao_contabil_razoes.py --modo producao
```

Por padrao, o script abre janelas para escolher:

1. pasta com os arquivos dos razoes;
2. pasta de saida;
3. arquivo unico do balancete.

## Como executar sem janelas

```powershell
python .\scripts\conciliacao_contabil_razoes_sap_hana\conciliacao_contabil_razoes.py --modo producao --sem-janela --pasta-bases "C:\CAMINHO\RAZOES" --pasta-saida "C:\CAMINHO\SAIDA" --arquivo-balancete "C:\CAMINHO\BALANCETE.xlsx"
```

## Como gerar executavel

```powershell
pip install -r .\requirements\conciliacao_contabil_razoes.txt
pip install -r .\requirements\build_executavel.txt
.\scripts\conciliacao_contabil_razoes_sap_hana\build_executavel.ps1
```

## Campos criticos dos razoes

Se qualquer campo critico faltar, o arquivo e marcado como `REEXTRAIR`. Em modo `producao`, a conciliacao e interrompida para evitar evidencia incompleta.

- `Conta do Razao`
- `Lancamento contabil`
- `Data de lancamento`
- `Mont.moeda empresa`
- `Txt.it.partida indv.`
- `Centro de custo`
- `Empresa`

## Campos opcionais dos razoes

Campos opcionais podem faltar sem bloquear a execucao:

- `Chave de lancamento`
- `Nº de itens`
- `Divisao`
- `Tipo lcto.contabil`

## Observacao sobre dados

Este case nao inclui bases reais, balancetes reais nem executavel. Use dados ficticios ou extracoes autorizadas para testes locais.

