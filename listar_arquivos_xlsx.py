import os
import glob
from datetime import datetime

pasta = r"C:\Users\a484377\Documents\Codex\2026-06-06\me-oriente-como-aproveitar-muito-do\outputs\Projeto_Conciliacao_FAGL_FPG5\entrada\FPG5_1000\01_Extracao_26"  # ajuste aqui

registros = []

for caminho in glob.glob(f"{pasta}/*.xlsx"):
    info = os.stat(caminho)
    registros.append({
        "arquivo":        os.path.basename(caminho),
        "caminho":        caminho,
        "tamanho_kb":     round(info.st_size / 1024, 1),
        "modificado_em":  datetime.fromtimestamp(info.st_mtime).strftime("%Y-%m-%d %H:%M"),
    })

# substitui as linhas 18-20
print(f"{'Arquivo':<50} {'KB':>8}  {'Modificado'}")
print("-" * 72)
for r in registros:
    print(f"{r['arquivo']:<50} {r['tamanho_kb']:>8}  {r['modificado_em']}")

print(f"\nTotal: {len(registros)} arquivo(s)")
