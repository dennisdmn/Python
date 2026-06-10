from pathlib import Path

# Exemplo simples de configuração de pasta.
# Troque o texto abaixo pelo diretório local que deseja inventariar.

pasta = Path(r"C:\caminho\para\sua\pasta")

print(f"Pasta configurada: {pasta}")
print(f"A pasta existe? {pasta.exists()}")

# Depois de validar o caminho, copie esse valor para a variável `pasta`
# no script principal.
