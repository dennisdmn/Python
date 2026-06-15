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
