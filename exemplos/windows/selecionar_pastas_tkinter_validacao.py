from pathlib import Path
import tkinter as tk
from tkinter import filedialog

EXTENSOES_VALIDAS = {'.xlsx', '.xls', '.csv'}


def selecionar_pasta(titulo: str) -> Path:
    root = tk.Tk()
    root.withdraw()
    pasta = filedialog.askdirectory(title=titulo)
    root.destroy()
    if not pasta:
        raise SystemExit('Nenhuma pasta selecionada.')
    return Path(pasta)


def listar_arquivos_validos(pasta: Path) -> list[Path]:
    return sorted(
        p for p in pasta.iterdir()
        if p.is_file() and p.suffix.lower() in EXTENSOES_VALIDAS
    )


if __name__ == '__main__':
    entrada = selecionar_pasta('Pasta de entrada')
    saida = selecionar_pasta('Pasta de saida')
    print('Entrada:', entrada)
    print('Saida:', saida)
    print('Arquivos:')
    for arquivo in listar_arquivos_validos(entrada):
        print('-', arquivo.name)
