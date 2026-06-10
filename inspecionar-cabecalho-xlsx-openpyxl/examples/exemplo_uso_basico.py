from pathlib import Path

# Informe o caminho do arquivo XLSX que deseja inspecionar.
# Depois, copie esse caminho para a variável `arquivo` no script principal.

arquivo = Path(r"C:\caminho\para\arquivo.xlsx")

print(f"Arquivo configurado: {arquivo}")
print(f"O arquivo existe? {arquivo.exists()}")
print(f"Extensão: {arquivo.suffix}")
