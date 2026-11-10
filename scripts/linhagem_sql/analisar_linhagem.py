"""Escolha um ou mais arquivos .sql para ver a linhagem entre tabelas."""

import argparse
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from io import BytesIO
from pathlib import Path
from textwrap import wrap


@dataclass(frozen=True)
class Linhagem:
    modo: str
    comandos: int
    origens: tuple[str, ...]
    destinos: tuple[str, ...]
    intermediarias: tuple[str, ...]
    texto_terminal: str


@dataclass(frozen=True)
class ResultadoArquivo:
    arquivo: Path
    linhagem: Linhagem | None = None
    erro: str = ""


def abrir_seletor(salvar=False):
    # Os diálogos só são usados na execução interativa, sem caminhos na linha de comando.
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
        if salvar:
            data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
            return filedialog.asksaveasfilename(
                parent=janela,
                title="Salvar relatório de linhagem",
                filetypes=[("Planilha Excel", "*.xlsx")],
                defaultextension=".xlsx",
                initialfile=f"linhagem_sql_{data_hora}.xlsx",
            )
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
    origens = tuple(dict.fromkeys(f.lower() for f in fontes))
    modo = "Modo didático (Python padrão)"
    texto = "\n".join([modo, *(f"{origem} → {destino[1]}" for origem in origens)])
    return Linhagem(modo, 1, origens, (destino[1],), (), texto)


def analisar_sql(sql, dialeto):
    try:
        from sqllineage.runner import LineageRunner
    except ModuleNotFoundError as erro:
        if erro.name != "sqllineage":
            raise
        return analisar_exemplo(sql)

    resultado = LineageRunner(sql, dialect=dialeto)
    modo = f"SQLLineage (dialeto: {dialeto})"
    return Linhagem(
        modo,
        len(resultado.statements()),
        tuple(map(str, resultado.source_tables)),
        tuple(map(str, resultado.target_tables)),
        tuple(map(str, resultado.intermediate_tables)),
        f"{modo}\n{resultado}",
    )


def escrever_aba(workbook, nome, cabecalhos, larguras, linhas, formato_cabecalho, quebrar=()):
    aba = workbook.add_worksheet(nome)
    aba.freeze_panes(1, 0)
    aba.hide_gridlines(2)
    for coluna, largura in enumerate(larguras):
        aba.set_column(coluna, coluna, largura)
    if linhas:
        status = aba.add_table(0, 0, len(linhas), len(cabecalhos) - 1, {
            "columns": [{"header": coluna} for coluna in cabecalhos],
            "style": "Table Style Medium 2",
        })
        if status != 0:
            raise ValueError(f"Não foi possível preencher a aba {nome}.")
        formato_quebra = workbook.add_format({"text_wrap": True, "valign": "top"}) if quebrar else None
        for numero, linha in enumerate(linhas, start=1):
            altura = 1
            for coluna, valor in enumerate(linha):
                if isinstance(valor, str) and valor:
                    formato = formato_quebra if coluna in quebrar else None
                    aba.write_string(numero, coluna, valor[:32767], formato)
                    if formato is not None:
                        largura = int(larguras[coluna] * 0.9)
                        altura = max(altura, sum(max(1, len(wrap(parte, largura))) for parte in valor.splitlines()))
                elif isinstance(valor, int):
                    aba.write_number(numero, coluna, valor)
            if altura > 1:
                aba.set_row(numero, min(altura * 15, 120))
    else:
        aba.write_row(0, 0, cabecalhos, formato_cabecalho)


def exportar_excel(saida, resultados):
    if saida.suffix.lower() != ".xlsx":
        raise ValueError("Informe um arquivo de saída com extensão .xlsx.")
    if saida.exists():
        raise FileExistsError("O relatório já existe. Escolha outro nome.")

    try:
        from xlsxwriter import Workbook
    except ImportError as erro:
        raise RuntimeError("Para exportar Excel, instale xlsxwriter no mesmo Python.") from erro

    resumo, tabelas = [], []
    for numero, item in enumerate(resultados, start=1):
        info = item.linhagem
        contagens = (
            (info.comandos, len(info.origens), len(info.destinos), len(info.intermediarias))
            if info else (None,) * 4
        )
        resumo.append((
            numero, item.arquivo.name, "OK" if info else "Erro", info.modo if info else "",
            *contagens, item.erro, str(item.arquivo.absolute()),
        ))
        if info:
            for papel, nomes in (("Origem", info.origens), ("Destino", info.destinos), ("Intermediária", info.intermediarias)):
                tabelas.extend((numero, item.arquivo.name, papel, tabela) for tabela in nomes)

    # Gera antes de abrir o destino; dados do SQL são tratados como texto.
    memoria = BytesIO()
    with Workbook(memoria, {"in_memory": True, "strings_to_formulas": False, "strings_to_urls": False}) as workbook:
        cabecalho = workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#305786"})
        escrever_aba(workbook, "Resumo", (
            "ID", "Arquivo", "Status", "Modo de análise", "Comandos", "Origens",
            "Destinos", "Intermediárias", "Mensagem de erro", "Caminho do SQL",
        ), (7, 29, 11, 34, 12, 10, 11, 16, 52, 48), resumo, cabecalho, quebrar=(8, 9))
        escrever_aba(workbook, "Tabelas", ("ID", "Arquivo", "Papel", "Tabela"),
                     (7, 29, 16, 48), tabelas, cabecalho)

    # A abertura exclusiva evita sobrescrever um arquivo criado durante a análise.
    with saida.open("xb") as arquivo:
        arquivo.write(memoria.getbuffer())


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="O script analisa cada arquivo separadamente e não executa SQL.",
    )
    parser.add_argument("arquivos", nargs="*", help="Caminhos dos arquivos .sql; sem eles, abre o seletor.")
    parser.add_argument("--dialeto", default="ansi", help="Dialeto para o SQLLineage, por exemplo oracle.")
    parser.add_argument("--excel", type=Path, metavar="ARQUIVO.xlsx", help="Caminho do relatório Excel.")
    args = parser.parse_args()

    try:
        caminhos = args.arquivos or abrir_seletor()
    except RuntimeError as erro:
        parser.exit(1, f"Erro: {erro}\n")

    if not caminhos:
        return 0

    resultados = []
    for caminho in caminhos:
        arquivo = Path(caminho)
        try:
            if arquivo.suffix.lower() != ".sql":
                raise ValueError("Escolha um arquivo com extensão .sql.")
            sql = arquivo.read_text(encoding="utf-8-sig")
            linhagem = analisar_sql(sql, args.dialeto)
        except Exception as erro:
            # Se um arquivo não puder ser analisado, continua com os demais.
            mensagem = str(erro) or type(erro).__name__
            resultados.append(ResultadoArquivo(arquivo, erro=mensagem))
            print(f"Arquivo: {arquivo.name}\nErro: {mensagem}\n", file=sys.stderr, flush=True)
        else:
            resultados.append(ResultadoArquivo(arquivo, linhagem))
            print(f"Arquivo: {arquivo.name}\n{linhagem.texto_terminal}\n", flush=True)

    total = len(caminhos)
    falhas = sum(item.linhagem is None for item in resultados)
    print(f"Arquivos selecionados: {total} | Analisados: {total - falhas} | Com erro: {falhas}")
    try:
        saida = args.excel
        if saida is None and not args.arquivos:
            caminho_saida = abrir_seletor(salvar=True)
            saida = Path(caminho_saida) if caminho_saida else None
        if saida is not None:
            exportar_excel(saida, resultados)
            print(f"Relatório Excel: {saida.absolute()}")
    except (OSError, ValueError, RuntimeError) as erro:
        parser.exit(1, f"Erro ao salvar o Excel: {erro}\n")
    return int(falhas > 0)


if __name__ == "__main__":
    raise SystemExit(main())
