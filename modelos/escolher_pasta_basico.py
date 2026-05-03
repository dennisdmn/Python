"""
Modelo basico: escolher uma pasta local pelo usuario.

Objetivo:
- Abrir uma janela para o usuario escolher uma pasta.
- Retornar o caminho escolhido como pathlib.Path.
- Servir como base simples para reaproveitar em outros scripts.
"""

from pathlib import Path
from tkinter import Tk, filedialog


def escolher_pasta(titulo: str = "Selecione uma pasta") -> Path:
    janela = Tk()
    janela.withdraw()
    janela.attributes("-topmost", True)

    pasta = filedialog.askdirectory(
        title=titulo,
        initialdir=Path.home(),
    )

    janela.destroy()

    if not pasta:
        raise SystemExit("Processo cancelado: nenhuma pasta foi selecionada.")

    return Path(pasta)


if __name__ == "__main__":
    pasta_escolhida = escolher_pasta("Selecione a pasta de entrada")
    print(f"Pasta escolhida: {pasta_escolhida}")
