# Instruções Para Copilot e Assistentes de AI

Antes de sugerir qualquer código Python neste repositório, leia `AGENTS.md` e trate aquelas regras como obrigatórias.

## Prioridade

1. Siga `AGENTS.md`.
2. Consulte `README.md` para localizar a pasta correta.
3. Use exemplos, modelos e scripts existentes antes de criar padrões novos.
4. Para rotinas com Excel, CSV ou dados tabulares, valide layout, linhas, nulos, duplicidades e totais.
5. Para rotinas que mexem com arquivos, use inventário, logs, pasta de saída separada e cuidado antes de sobrescrever.
6. Para automações recorrentes, prefira script em `scripts/` ou modelo em `modelos/`, não apenas notebook.

## Regras rápidas

- Não sugira apagar, mover ou sobrescrever arquivos sem validação e confirmação.
- Não ignore colunas obrigatórias em planilhas ou CSV.
- Não use `except: pass`.
- Não crie dependência externa pesada sem necessidade.
- Não use caminhos fixos como solução final.
- Prefira `pathlib.Path` para caminhos.
- Sempre que houver valores ou linhas relevantes, compare antes/depois.
- Quando a rotina for para usuário não técnico no Windows, considere seleção por janela com `tkinter`.

Este repositório privilegia Python seguro, auditável, didático e reutilizável.