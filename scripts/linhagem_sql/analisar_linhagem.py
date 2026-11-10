"""Escolha um ou mais arquivos .sql para ver a linhagem entre tabelas."""

import argparse
import re
import sys
from pathlib import Path


def escolher_arquivos():
    # O seletor é usado apenas quando nenhum caminho é passado no terminal.
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError as erro:
        raise RuntimeError("Informe os caminhos dos arquivos .sql no terminal.") from erro

    try:
        janela = tk.Tk()
    except tk.TclError as erro:
        raise RuntimeError("Sem interface gráfica. Informe os caminhos dos arquivos .sql no terminal.") from erro

    janela.withdraw()
    try:
        return filedialog.askopenfilenames(
            parent=janela,
            title="Escolha um ou mais arquivos SQL",
            filetypes=[("Arquivos SQL", "*.sql")],
        )
    finally:
        janela.destroy()


def analisar_exemplo(sql):
    # Modo didático: reconhece um CREATE TABLE AS SELECT com FROM e JOIN explícitos.
    sql = re.sub(
        r"'(?:''|[^'])*'|--[^\n]*|/\*.*?\*/",
        lambda token: " '' " if token[0].startswith("'") else " ",
        sql,
        flags=re.S,
    )
    nome = r"[a-z_][a-z0-9_]*(?:\.[a-z_][a-z0-9_]*)?"
    sql = sql.strip().removesuffix(";")
    destino = re.match(rf"CREATE\s+TABLE\s+({nome})\s+AS\s+SELECT\b", sql, re.I)
    erro = "O modo didático aceita um CREATE TABLE AS SELECT simples. Para outros SQLs, instale sqllineage."
    if not destino or re.search(r'[;"`\[\]]|\b(?:WITH|UNION|INTERSECT|EXCEPT|MINUS)\b', sql, re.I):
        raise ValueError(erro)
    if len(re.findall(r"\bSELECT\b", sql, re.I)) != 1:
        raise ValueError(erro)

    trecho = re.search(r"\bFROM\b.+?(?=\b(?:WHERE|GROUP\s+BY|HAVING|ORDER\s+BY)\b|\Z)", sql, re.I | re.S)
    if not trecho or "," in trecho[0]:
        raise ValueError(erro)
    fontes = re.findall(rf"\b(?:FROM|JOIN)\s+({nome})(?=\s|\Z)", trecho[0], re.I)
    if len(fontes) != len(re.findall(r"\b(?:FROM|JOIN)\b", trecho[0], re.I)):
        raise ValueError(erro)
    return "Modo didático (Python padrão)\n" + "\n".join(
        f"{origem} → {destino[1]}" for origem in dict.fromkeys(f.lower() for f in fontes)
    )


def analisar_sql(sql, dialeto):
    try:
        from sqllineage.runner import LineageRunner
    except ModuleNotFoundError as erro:
        if erro.name != "sqllineage":
            raise
        return analisar_exemplo(sql)

    resultado = LineageRunner(sql, dialect=dialeto)
    return f"SQLLineage (dialeto: {dialeto})\n{resultado}"


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="O script analisa cada arquivo separadamente e não executa SQL.",
    )
    parser.add_argument("arquivos", nargs="*", help="Caminhos dos arquivos .sql; sem eles, abre o seletor.")
    parser.add_argument("--dialeto", default="ansi", help="Dialeto para o SQLLineage, por exemplo oracle.")
    args = parser.parse_args()

    try:
        caminhos = args.arquivos or escolher_arquivos()
    except RuntimeError as erro:
        parser.exit(1, f"Erro: {erro}\n")

    if not caminhos:
        return 0

    falhas = 0
    for caminho in caminhos:
        arquivo = Path(caminho)
        try:
            if arquivo.suffix.lower() != ".sql":
                raise ValueError("Escolha um arquivo com extensão .sql.")
            sql = arquivo.read_text(encoding="utf-8-sig")
            resultado = analisar_sql(sql, args.dialeto)
        except Exception as erro:
            # Se um arquivo não puder ser analisado, continua com os demais.
            print(f"Arquivo: {arquivo.name}\nErro: {erro}\n", file=sys.stderr, flush=True)
            falhas += 1
        else:
            print(f"Arquivo: {arquivo.name}\n{resultado}\n", flush=True)

    total = len(caminhos)
    print(f"Arquivos selecionados: {total} | Analisados: {total - falhas} | Com erro: {falhas}")
    return int(falhas > 0)


if __name__ == "__main__":
    raise SystemExit(main())
