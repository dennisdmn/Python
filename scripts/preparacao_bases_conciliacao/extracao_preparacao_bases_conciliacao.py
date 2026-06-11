# =============================================================================
# EXTRACAO — preparacao das bases para conciliacao
# =============================================================================

import os
import sys
import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

# -----------------------------------------------------------------------------
# CONFIGURACAO — selecao dinamica de pastas via janela
# -----------------------------------------------------------------------------

def selecionar_pasta(titulo, mensagem, initialdir=None):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Selecao de Pasta", mensagem)
    pasta = filedialog.askdirectory(title=titulo, initialdir=initialdir)
    root.destroy()
    if not pasta:
        print(f"  [CANCELADO] Nenhuma pasta selecionada para: {titulo}")
        sys.exit(0)
    return pasta

print("\n" + "="*70)
print("  EXTRACAO — selecao de pastas")
print("="*70)

INPUT_DIR = selecionar_pasta(
    titulo="Bases extraidas Legado x SAP para conciliacao",
    mensagem="Selecione a pasta com as bases extraidas do Legado e do SAP"
)
BASE_DIR = os.path.dirname(INPUT_DIR)

STAGING_DIR = selecionar_pasta(
    titulo="Resultado da Conciliacao",
    mensagem="Selecione a pasta onde sera salva a evidencia da conciliacao em Excel",
    initialdir=BASE_DIR
)

os.makedirs(STAGING_DIR, exist_ok=True)

print(f"\n  BASE_DIR    : {BASE_DIR}")
print(f"  INPUT_DIR   : {INPUT_DIR}")
print(f"  STAGING_DIR : {STAGING_DIR}")
