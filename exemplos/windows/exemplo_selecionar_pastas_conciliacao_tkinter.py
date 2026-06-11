"""
Exemplo: selecionar pastas de entrada e saida para conciliacao usando Tkinter.

Objetivo:
- Demonstrar como abrir janelas para o usuario selecionar diretorios.
- Selecionar a pasta com bases extraidas do Legado e do SAP.
- Validar se a pasta de entrada contem arquivos Excel ou CSV.
- Derivar BASE_DIR a partir da pasta de entrada.
- Selecionar a pasta onde sera salva a evidencia de conciliacao.
- Criar a pasta de saida, caso ela ainda nao exista.

Este arquivo e um exemplo didatico. Para rotina operacional, veja:
scripts/preparacao_bases_conciliacao/extracao_preparacao_bases_conciliacao.py
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox


def selecionar_pasta(titulo, mensagem, initialdir=None):
    """
    Abre uma janela para selecao de pasta.

    Se o usuario cancelar, exibe um aviso e encerra o processo de forma controlada.
    """

    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Seleção de Pasta", mensagem)

    pasta = filedialog.askdirectory(
        title=titulo,
        initialdir=initialdir,
    )

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
    """
    Verifica se a pasta possui pelo menos um arquivo de entrada valido.

    Extensoes consideradas validas:
    - .xlsx
    - .xls
    - .csv
    """

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


def main():
    print("\n" + "=" * 70)
    print("  EXEMPLO — seleção de pastas para conciliacao")
    print("=" * 70)

    input_dir = selecionar_pasta(
        titulo="Bases extraídas do Legado x SAP para conciliação.",
        mensagem="Selecione a pasta com as bases extraídas do Legado e do SAP.\n\n",
    )

    base_dir = os.path.dirname(input_dir)

    arquivos_input = validar_arquivos_input(input_dir)

    print(f"\n  Arquivos encontrados em INPUT_DIR ({len(arquivos_input)}):")
    for arquivo in sorted(arquivos_input):
        print(f"    {arquivo}")

    staging_dir = selecionar_pasta(
        titulo="Resultado da Conciliação",
        mensagem="Selecione a pasta onde será salva a evidência da conciliação em Excel",
        initialdir=base_dir,
    )

    os.makedirs(staging_dir, exist_ok=True)

    print(f"\n  BASE_DIR    : {base_dir}")
    print(f"  INPUT_DIR   : {input_dir}")
    print(f"  STAGING_DIR : {staging_dir}")
    print("\n  Configuração concluída. Avançando para leitura dos arquivos...")


if __name__ == "__main__":
    main()
