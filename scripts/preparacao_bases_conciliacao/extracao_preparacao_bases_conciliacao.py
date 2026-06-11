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
    messagebox.showinfo("Seleção de Pasta", mensagem)
    pasta = filedialog.askdirectory(title=titulo, initialdir=initialdir)
    root.destroy()
    if not pasta:
        root2 = tk.Tk()
        root2.withdraw()
        messagebox.showwarning(
            "Processo Encerrado!",
            f"Nenhuma pasta selecionada para:\n'{titulo}'\n\n"
            "O processo de conciliação foi encerrado."
        )
        root2.destroy()
        print(f"\n  [ENCERRADO] Nenhuma pasta selecionada para: {titulo}")
        sys.exit(0)
    return pasta


def validar_arquivos_input(pasta):
    extensoes_validas = {".xlsx", ".xls", ".csv"}
    arquivos = [
        f for f in os.listdir(pasta)
        if os.path.isfile(os.path.join(pasta, f))
        and os.path.splitext(f)[1].lower() in extensoes_validas
    ]
    if not arquivos:
        nome_pasta = os.path.basename(pasta)
        root = tk.Tk()
        root.withdraw()
        root.lift()
        root.attributes("-topmost", True)
        messagebox.showwarning(
            "Processo Encerrado!",
            f"A pasta '{nome_pasta}' não contém\n"
            "arquivos Excel (.xlsx, .xls) ou CSV (.csv).\n\n"
            "O processo de conciliação foi encerrado."
        )
        root.destroy()
        print(f"\n  [ENCERRADO] Pasta sem arquivos válidos: {pasta}")
        sys.exit(0)
    return arquivos


print("\n" + "="*70)
print("  EXTRACAO — seleção de pastas")
print("="*70)

INPUT_DIR = selecionar_pasta(
    titulo="Bases extraídas do Legado x SAP para conciliação.",
    mensagem="Selecione a pasta com as bases extraídas do Legado e do SAP.\n\n"
)
BASE_DIR = os.path.dirname(INPUT_DIR)

arquivos_input = validar_arquivos_input(INPUT_DIR)
print(f"\n  Arquivos encontrados em INPUT_DIR ({len(arquivos_input)}):")
for f in sorted(arquivos_input):
    print(f"    {f}")

STAGING_DIR = selecionar_pasta(
    titulo="Resultado da Conciliação",
    mensagem="Selecione a pasta onde será salva a evidência da conciliação em Excel",
    initialdir=BASE_DIR
)

os.makedirs(STAGING_DIR, exist_ok=True)

print(f"\n  BASE_DIR    : {BASE_DIR}")
print(f"  INPUT_DIR   : {INPUT_DIR}")
print(f"  STAGING_DIR : {STAGING_DIR}")
print("\n  Configuração concluída. Avançando para leitura dos arquivos...")
