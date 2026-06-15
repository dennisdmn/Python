"""Selecao local de pastas e arquivos por janela grafica.

Objetivo:
    Reaproveitar a escolha manual de caminhos em scripts operacionais
    executados localmente.

Quando usar:
    - Scripts Windows com uso manual.
    - Rotinas que precisam de pasta de entrada ou arquivo de apoio.

Documentacao:
    Consulte `python_operacional/docs/selecao_arquivos.md` antes de alterar.

Guia para IA:
    Nao recriar dialogos tkinter em cada script. Reutilizar este modulo
    quando a necessidade for apenas selecionar pasta ou arquivo.
"""

from pathlib import Path
import tkinter as tk
from tkinter import filedialog


def selecionar_pasta(titulo='Selecione uma pasta'):
    root = tk.Tk()
    root.withdraw()
    valor = filedialog.askdirectory(title=titulo)
    root.destroy()
    if not valor:
        raise SystemExit('Operacao cancelada.')
    return Path(valor)


def selecionar_arquivo(titulo='Selecione um arquivo'):
    root = tk.Tk()
    root.withdraw()
    valor = filedialog.askopenfilename(title=titulo)
    root.destroy()
    if not valor:
        raise SystemExit('Operacao cancelada.')
    return Path(valor)
