# Preparacao de Bases para Conciliacao

Script operacional em Python para iniciar a preparacao das bases extraidas do Legado e do SAP antes da geracao da evidencia de conciliacao.

A rotina usa janelas locais do Windows para selecionar:

1. a pasta com as bases extraidas do Legado e do SAP;
2. a pasta onde sera salva a evidencia da conciliacao em Excel.

Antes de seguir para a pasta de saida, o script valida se a pasta de entrada contem ao menos um arquivo aceito.

## Arquivo principal

- `extracao_preparacao_bases_conciliacao.py`: script de selecao dinamica das pastas de entrada e saida, com validacao dos arquivos de entrada.

## O que este script faz

- abre janela para selecionar a pasta de entrada das bases;
- encerra o processo com aviso grafico se o usuario cancelar a selecao;
- valida se a pasta de entrada possui arquivos `.xlsx`, `.xls` ou `.csv`;
- encerra o processo com aviso grafico se a pasta nao tiver arquivos validos;
- lista no terminal os arquivos validos encontrados;
- define `BASE_DIR` a partir da pasta de entrada selecionada;
- abre janela para selecionar a pasta de saida da evidencia;
- cria a pasta de saida, caso ela ainda nao exista;
- imprime no terminal os caminhos selecionados para rastreabilidade.

## Como executar

Na raiz do repositorio:

```powershell
python .\scripts\preparacao_bases_conciliacao\extracao_preparacao_bases_conciliacao.py
```

## Arquivos aceitos na entrada

A pasta de entrada precisa conter pelo menos um arquivo com uma das extensoes abaixo:

- `.xlsx`
- `.xls`
- `.csv`

Se nenhum arquivo valido for encontrado, a conciliacao e encerrada antes da etapa de leitura.

## Dependencias

O script usa bibliotecas nativas do Python e `pandas`.

```powershell
pip install -r .\requirements\preparacao_bases_conciliacao.txt
```

## Observacao sobre dados

Este repositorio nao deve armazenar bases reais extraidas do Legado, SAP ou evidencias de conciliacao. Mantenha somente codigo, documentacao e exemplos sem dados sensiveis.
