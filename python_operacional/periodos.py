"""Calculo e validacao de periodos no formato AAAAMM.

Objetivo:
    Reunir funcoes genericas para manipular periodos contabeis mensais.

Documentacao:
    Consulte `python_operacional/docs/periodos.md` antes de alterar.
"""


def periodo_anterior(periodo: str) -> str:
    """Retorna o periodo mensal anterior no formato AAAAMM.

    Exemplo:
        >>> periodo_anterior("202607")
        '202606'
    """
    if not isinstance(periodo, str):
        raise TypeError("periodo deve ser uma string no formato AAAAMM")

    if len(periodo) != 6 or not periodo.isdigit():
        raise ValueError("periodo deve conter exatamente 6 digitos no formato AAAAMM")

    ano = int(periodo[:4])
    mes = int(periodo[4:])

    if ano == 0:
        raise ValueError("ano deve estar entre 0001 e 9999")

    if not 1 <= mes <= 12:
        raise ValueError("mes deve estar entre 01 e 12")

    if mes == 1:
        return f"{ano - 1:04d}12"

    return f"{ano:04d}{mes - 1:02d}"
