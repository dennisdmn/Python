# Caso de sucesso - Conciliacao Legado x SAP Sigamovi x FBL3H

## Contexto

Automacao de conciliacao entre uma base Sigamovi e uma base SAP/FBL3H, com apoio de de-para de contas e empresas.

## Desafio

A rotina precisava gerar uma evidencia em Excel que abrisse de forma estavel no ambiente corporativo.

## Solucao

O processo foi estruturado em etapas:

1. selecao de pastas por janela local;
2. validacao de arquivos;
3. identificacao de layouts;
4. leitura das bases;
5. explosao de debito e credito;
6. aplicacao de de-para;
7. conciliacao por full outer join;
8. geracao de evidencia Excel sem tabelas internas, sem autofiltro e sem celulas mescladas.

## Resultado

O case virou um padrao operacional reutilizavel para novas conciliacoes financeiras e contabeis.

## Uso por IA

Este documento serve como contexto para ChatGPT, Claude, Codex ou outro assistente entenderem o objetivo do case antes de sugerirem alteracoes no codigo.
