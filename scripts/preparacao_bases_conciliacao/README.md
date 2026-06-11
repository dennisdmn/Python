# Preparacao de Bases para Conciliacao

Script operacional em Python para iniciar a preparacao das bases extraidas do Legado e do SAP antes da geracao da evidencia de conciliacao.

A rotina usa janelas locais do Windows para selecionar:

1. a pasta com as bases extraidas do Legado e do SAP;
2. a pasta onde sera salva a evidencia da conciliacao em Excel.

## Arquivo principal

- `extracao_preparacao_bases_conciliacao.py`: script de selecao dinamica das pastas de entrada e saida.

## O que este script faz

- abre janela para selecionar a pasta de entrada das bases;
- define `BASE_DIR` a partir da pasta de entrada selecionada;
- abre janela para selecionar a pasta de saida da evidencia;
- cria a pasta de saida, caso ela ainda nao exista;
- imprime no terminal os caminhos selecionados para rastreabilidade.

## Como executar

Na raiz do repositorio:

```powershell
python .\scripts\preparacao_bases_conciliacao\extracao_preparacao_bases_conciliacao.py
```

## Dependencias

O script usa bibliotecas nativas do Python e `pandas`.

```powershell
pip install -r .\requirements\preparacao_bases_conciliacao.txt
```

## Observacao sobre dados

Este repositorio nao deve armazenar bases reais extraidas do Legado, SAP ou evidencias de conciliacao. Mantenha somente codigo, documentacao e exemplos sem dados sensiveis.
