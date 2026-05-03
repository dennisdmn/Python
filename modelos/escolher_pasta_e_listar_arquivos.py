"""
Modelo basico: escolher uma pasta local e listar arquivos.

Objetivo:
- Abrir uma janela para o usuario escolher uma pasta.
- Listar os arquivos encontrados nessa pasta por extensao.
- Servir como base simples para rotinas que processam arquivos locais.
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


def listar_arquivos(pasta: Path, extensao: str = "*") -> list[Path]:
    if extensao == "*":
        padrao_busca = "*"
    else:
        extensao = extensao if extensao.startswith(".") else f".{extensao}"
        padrao_busca = f"*{extensao}"

    return sorted(arquivo for arquivo in pasta.glob(padrao_busca) if arquivo.is_file())


if __name__ == "__main__":
    pasta_entrada = escolher_pasta("Selecione a pasta de entrada")
    arquivos = listar_arquivos(pasta_entrada, extensao="xlsx")

    print("=" * 80)
    print(f"Pasta escolhida: {pasta_entrada}")
    print(f"Arquivos encontrados: {len(arquivos)}")
    print("=" * 80)

    for arquivo in arquivos:
        print(arquivo.name)
