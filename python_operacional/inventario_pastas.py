"""Inventario operacional de arquivos em pastas.

Objetivo:
    Gerar uma visao tabular dos arquivos disponiveis antes do
    processamento de bases em lote.

Quando usar:
    - Validar entradas de uma rotina.
    - Registrar rastreabilidade de arquivos processados.
    - Filtrar arquivos por extensao.

Documentacao:
    Consulte `python_operacional/docs/inventario_pastas.md` antes de alterar.

Guia para IA:
    Antes de criar loops com Path.glob em scripts operacionais, verificar
    se `inventariar_pasta` ou `listar_arquivos` atende ao caso.
"""

from pathlib import Path
import pandas as pd


def inventariar_pasta(pasta, extensoes=None, recursivo=False):
    pasta = Path(pasta)
    padrao = '**/*' if recursivo else '*'
    extensoes_norm = None if extensoes is None else {e.lower() for e in extensoes}
    linhas = []
    for p in pasta.glob(padrao):
        if not p.is_file():
            continue
        if extensoes_norm and p.suffix.lower() not in extensoes_norm:
            continue
        st = p.stat()
        linhas.append({
            'nome': p.name,
            'extensao': p.suffix.lower(),
            'tamanho_bytes': st.st_size,
            'modificado_em': pd.to_datetime(st.st_mtime, unit='s'),
            'caminho': str(p),
        })
    return pd.DataFrame(linhas)


def listar_arquivos(pasta, extensoes=None):
    inv = inventariar_pasta(pasta, extensoes=extensoes, recursivo=False)
    if inv.empty:
        return []
    return [Path(x) for x in inv['caminho'].tolist()]
