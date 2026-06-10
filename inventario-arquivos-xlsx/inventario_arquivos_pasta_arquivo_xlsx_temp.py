import os
import glob
import tempfile
from datetime import datetime
from pathlib import Path

import pandas as pd

pasta = r"C:\Users\a484377\Documents\Codex\2026-06-06\me-oriente-como-aproveitar-muito-do\outputs\Projeto_Conciliacao_FAGL_FPG5\entrada\FPG5_1000\01_Extracao_26"

registros = [
    {
        "arquivo":       os.path.basename(p),
        "caminho":       p,
        "tamanho_kb":    round(os.stat(p).st_size / 1024, 1),
        "modificado_em": datetime.fromtimestamp(os.stat(p).st_mtime).strftime("%Y-%m-%d %H:%M"),
    }
    for p in glob.glob(f"{pasta}/*.xlsx")
]

df = pd.DataFrame(registros)

# Grava em pasta temporária do sistema — sem deixar rastro na pasta do projeto
with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as tmp:
    caminho_tmp = Path(tmp.name)

df.to_excel(caminho_tmp, index=False)

print(df.to_string(index=False))
print(f"\nTotal: {len(df)} arquivo(s)")

# Abre no Excel sem salvar nada no projeto
os.startfile(caminho_tmp)
