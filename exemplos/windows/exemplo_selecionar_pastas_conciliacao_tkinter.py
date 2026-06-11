"""
Exemplo: selecionar pastas de entrada e saida para conciliacao usando Tkinter.

Objetivo:
- Demonstrar como abrir janelas para o usuario selecionar diretorios.
- Selecionar a pasta com bases extraidas do Legado e do SAP.
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

    Parametros:
    - titulo: titulo exibido na janela de selecao.
    - mensagem: aviso exibido antes da selecao.
    - initialdir: pasta inicial sugerida para o usuario.

    Retorno:
    - Caminho da pasta selecionada como string.
    """

    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Selecao de Pasta", mensagem)

    pasta = filedialog.askdirectory(
        title=titulo,
        initialdir=initialdir,
    )

    root.destroy()

    if not pasta:
        print(f"  [CANCELADO] Nenhuma pasta selecionada para: {titulo}")
        sys.exit(0)

    return pasta


def main():
    print("\n" + "=" * 70)
    print("  EXEMPLO — selecao de pastas para conciliacao")
    print("=" * 70)

    input_dir = selecionar_pasta(
        titulo="Bases extraidas Legado x SAP para conciliacao",
        mensagem="Selecione a pasta com as bases extraidas do Legado e do SAP",
    )

    base_dir = os.path.dirname(input_dir)

    staging_dir = selecionar_pasta(
        titulo="Resultado da Conciliacao",
        mensagem="Selecione a pasta onde sera salva a evidencia da conciliacao em Excel",
        initialdir=base_dir,
    )

    os.makedirs(staging_dir, exist_ok=True)

    print(f"\n  BASE_DIR    : {base_dir}")
    print(f"  INPUT_DIR   : {input_dir}")
    print(f"  STAGING_DIR : {staging_dir}")


if __name__ == "__main__":
    main()
