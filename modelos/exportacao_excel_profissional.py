"""Modelo mínimo para gerar Excel profissional com XlsxWriter.

Inclui título, totais, tabela formatada, congelamento de painéis e ajuste de colunas.
"""

from pathlib import Path

import xlsxwriter

DADOS = [
    {"conta": "1101011001", "descricao": "Caixa", "montante": 1250.75},
    {"conta": "2101010001", "descricao": "Fornecedor", "montante": -980.10},
]


def gerar_excel(caminho_saida: Path) -> None:
    workbook = xlsxwriter.Workbook(caminho_saida)
    ws = workbook.add_worksheet("Resumo")

    fmt_titulo = workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#5B9BD5", "font_size": 14})
    fmt_cab = workbook.add_format({"bold": True, "font_color": "white", "bg_color": "#4F81BD", "border": 1})
    fmt_texto = workbook.add_format({"border": 1})
    fmt_num = workbook.add_format({"num_format": '_-#,##0.00_-;[Red](#,##0.00)_-;_-* "-"??_-;_-@_-', "border": 1})
    fmt_total = workbook.add_format({"bold": True, "bg_color": "#FFF2CC", "num_format": '_-#,##0.00_-;[Red](#,##0.00)_-;_-* "-"??_-;_-@_-'})

    ws.merge_range("A1:C1", "Resumo Operacional", fmt_titulo)
    ws.write("A3", "TOTAIS:", fmt_total)
    ws.write_formula("C3", "=SUM(C5:C6)", fmt_total)

    ws.write_row("A5", ["conta", "descricao", "montante"], fmt_cab)
    for linha, item in enumerate(DADOS, start=5):
        ws.write(linha, 0, item["conta"], fmt_texto)
        ws.write(linha, 1, item["descricao"], fmt_texto)
        ws.write_number(linha, 2, item["montante"], fmt_num)

    ws.add_table(4, 0, 4 + len(DADOS), 2, {
        "name": "TabelaResumo",
        "style": "Table Style Medium 2",
        "columns": [{"header": "conta"}, {"header": "descricao"}, {"header": "montante"}],
    })
    ws.freeze_panes(5, 0)
    ws.set_column("A:A", 18)
    ws.set_column("B:B", 35)
    ws.set_column("C:C", 16)
    workbook.close()


if __name__ == "__main__":
    gerar_excel(Path("modelo_excel_profissional.xlsx"))
