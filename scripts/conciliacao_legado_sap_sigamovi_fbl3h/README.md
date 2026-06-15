# Conciliacao Legado x SAP - Sigamovi x FBL3H

Case operacional em Python para preparar, validar e conciliar bases extraidas do Legado/Sigamovi contra razoes SAP/FBL3H, usando de-para de contas e empresas.

Este material foi organizado para ser reutilizado por pessoas e por assistentes de IA como ChatGPT, Claude e Codex em futuros desenvolvimentos. O objetivo e deixar explicito o contexto de negocio, as entradas esperadas, as decisoes tecnicas e os cuidados de auditoria.

## Objetivo operacional

Gerar uma evidencia em Excel com:

1. resumo consolidado por conta;
2. resumo por divisao/empresa e conta;
3. base Sigamovi integral;
4. base Razao SAP/FBL3H;
5. de-para de empresas;
6. de-para de contas.

A ordem recomendada das abas do output e:

1. `Resumo`
2. `Resumo por Empresa`
3. `Sigamovi`
4. `Razao_SAP`
5. `De_Para_Empresa_sas`
6. `De_Para_Conta_sas`

## Arquivo principal

- `conciliacao_legado_sap_sigamovi_fbl3h.py`: script principal de conciliacao.

## O que o script demonstra

- selecao de pasta de entrada e saida por janela local no Windows;
- validacao minima de arquivos `.xlsx`, `.xls` e `.csv`;
- identificacao de arquivos por layout/cabecalho;
- identificacao de FBL3H de integracao e FBL3H de correcao;
- leitura de de-para de conta e empresa;
- explosao de debito e credito do legado;
- traducao de contas e empresas por de-para;
- conciliacao por full outer join;
- classificacao `OK`, `DIVERGENTE`, `APENAS_LEGADO`, `APENAS_SAP`;
- exportacao de workbook Excel sem `Table`, sem `AutoFilter` e sem celulas mescladas.

## Como executar

Na raiz do repositorio:

```powershell
pip install -r .\requirements\conciliacao_legado_sap_sigamovi_fbl3h.txt
python .\scripts\conciliacao_legado_sap_sigamovi_fbl3h\conciliacao_legado_sap_sigamovi_fbl3h.py
```

## Arquivos esperados na pasta de entrada

A pasta de entrada deve conter ao menos:

1. arquivo Sigamovi/Legado;
2. arquivo SAP/FBL3H da primeira conciliacao;
3. arquivo de-para de contas;
4. arquivo de-para de empresas.

Opcionalmente, pode conter um FBL3H de correcao/carga manual.

## Layouts documentados

Os layouts minimos ficam em `exemplos_layout/`:

- `layout_sigamovi.md`
- `layout_fbl3h.md`
- `layout_depara_conta.md`
- `layout_depara_empresa.md`

## Decisoes tecnicas importantes

### 1. Nao usar Tabela interna do Excel

Em bases grandes, `openpyxl.Table` pode gerar arquivos que o Excel abre em modo de reparo, removendo recursos como `/xl/tables/table*.xml`. Por isso, este case usa cabecalho simples e formatacao basica.

### 2. Nao usar AutoFilter automatico

O AutoFilter tambem pode ficar associado a estruturas internas de tabela. Para evidencias operacionais, a prioridade e abrir sem reparo no Excel corporativo.

### 3. Nao mesclar cabecalhos

Cabecalhos mesclados dificultam leitura automatizada por Power Query, pandas e assistentes de IA. O padrao do case e manter titulos nas primeiras linhas, sem merge.

### 4. Separar regra de negocio de formatacao

A conciliacao deve ser calculada antes da exportacao. O Excel e apenas evidencia, nao motor de calculo.

## Guia para IA e futuros desenvolvimentos

Ao evoluir este case, uma IA deve seguir esta ordem:

1. preservar os nomes das abas de saida, salvo pedido explicito;
2. preservar a ordem das abas;
3. evitar `Table`, `AutoFilter` e celulas mescladas em outputs grandes;
4. manter validacao de layout antes de ler bases completas;
5. nunca incluir bases reais, prints sensiveis ou evidencias reais no repositorio;
6. preferir funcoes pequenas e reutilizaveis;
7. documentar toda nova regra de conciliacao no README antes de alterar o codigo;
8. validar sintaxe com `python -m py_compile` antes de commitar;
9. quando houver divergencia, diagnosticar origem: apenas legado, apenas SAP ou ambos.

## Observacao sobre dados

Este repositorio nao deve armazenar bases reais extraidas do Legado, SAP, SAS ou evidencias de conciliacao. Use somente dados ficticios, layouts ou descricoes tecnicas sem informacao sensivel.
