"""Modelo para selecionar entradas por CLI ou janela no Windows.

A mesma rotina pode ser usada por usuário final, com janelas, ou por suporte técnico,
com parâmetros de linha de comando.
"""

import argparse
from pathlib import Path
from tkinter import Tk, filedialog


def escolher_pasta(titulo: str) -> Path:
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    caminho = filedialog.askdirectory(title=titulo)
    root.destroy()
    if not caminho:
        raise SystemExit("Operação cancelada pelo usuário.")
    return Path(caminho)


def escolher_arquivo_xlsx(titulo: str) -> Path:
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    caminho = filedialog.askopenfilename(title=titulo, filetypes=[("Excel", "*.xlsx")])
    root.destroy()
    if not caminho:
        raise SystemExit("Operação cancelada pelo usuário.")
    return Path(caminho)


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Exemplo de seleção de entradas por CLI ou janela.")
    parser.add_argument("--pasta-entrada", type=Path)
    parser.add_argument("--pasta-saida", type=Path)
    parser.add_argument("--arquivo-apoio", type=Path)
    parser.add_argument("--sem-janela", action="store_true")
    return parser


def main() -> None:
    args = criar_parser().parse_args()
    if args.sem_janela and (not args.pasta_entrada or not args.pasta_saida or not args.arquivo_apoio):
        raise SystemExit("Informe todos os caminhos quando usar --sem-janela.")

    pasta_entrada = args.pasta_entrada or escolher_pasta("Selecione a pasta de entrada")
    pasta_saida = args.pasta_saida or escolher_pasta("Selecione a pasta de saída")
    arquivo_apoio = args.arquivo_apoio or escolher_arquivo_xlsx("Selecione o arquivo de apoio")

    print("Entrada:", pasta_entrada)
    print("Saída:", pasta_saida)
    print("Arquivo:", arquivo_apoio)


if __name__ == "__main__":
    main()
