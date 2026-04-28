"""
Exemplo procedural: escolher uma pasta/diretorio no Windows e listar arquivos.

Objetivo:
- Demonstrar o fluxo mais simples possivel para selecionar uma pasta.
- Mostrar uma aplicacao pratica depois da escolha: listar arquivos por extensao.
- Manter fallback seguro caso a janela grafica nao possa ser aberta.

Bibliotecas escolhidas:
- pathlib.Path:
    Biblioteca padrao do Python para trabalhar com caminhos de forma moderna,
    legivel e mais segura do que concatenar strings manualmente.

- tkinter:
    Biblioteca padrao do Python para interface grafica simples.
    Foi usada porque permite abrir uma janela nativa de selecao de diretorio
    sem instalar dependencias externas.
"""

from pathlib import Path


# =============================================================================
# CONFIGURACOES DO EXEMPLO
# =============================================================================

# Pasta sugerida inicialmente ao usuario.
# Em um projeto real, poderia ser uma pasta de entrada, bases, relatorios etc.
pasta_padrao = Path.cwd()

# Extensao que sera buscada depois que a pasta for escolhida.
# Troque para ".csv", ".txt", ".xlsx" etc. conforme a necessidade.
extensao_desejada = ".xlsx"

# Controla se a janela de selecao sera aberta.
# Use False em automacoes, testes ou ambientes sem interface grafica.
usar_janela = True


# =============================================================================
# ESCOLHA DO DIRETORIO
# =============================================================================

if not usar_janela:
    # Fluxo sem interface grafica: usa diretamente a pasta padrao.
    pasta_escolhida = pasta_padrao
else:
    try:
        # Import local: tkinter so e carregado quando a janela realmente sera usada.
        from tkinter import Tk, filedialog

        # Cria a janela raiz exigida pelo tkinter.
        janela = Tk()

        # Oculta a janela principal, deixando visivel apenas o seletor de diretorio.
        janela.withdraw()

        # Mantem a janela de selecao acima das demais janelas.
        janela.attributes("-topmost", True)

        # Abre a janela para o usuario escolher uma pasta.
        caminho_escolhido = filedialog.askdirectory(
            title="Selecione a pasta com os arquivos de entrada",
            initialdir=pasta_padrao,
        )

        # Fecha a janela raiz depois da escolha para liberar recursos.
        janela.destroy()

        if caminho_escolhido:
            # Quando o usuario escolhe uma pasta, askdirectory retorna o caminho como string.
            # Convertemos para Path para manter o restante do codigo mais legivel.
            pasta_escolhida = Path(caminho_escolhido)
        else:
            # Se o usuario cancelar, askdirectory retorna string vazia.
            # Nesse caso, usamos a pasta padrao.
            print(f"Nenhuma pasta selecionada. Usando pasta padrao: {pasta_padrao}")
            pasta_escolhida = pasta_padrao

    except Exception as exc:
        # Fallback defensivo:
        # Se tkinter falhar ou nao houver interface grafica, o script continua.
        print(f"Nao foi possivel abrir a janela de selecao de pasta: {exc}")
        print(f"Usando pasta padrao: {pasta_padrao}")
        pasta_escolhida = pasta_padrao


# =============================================================================
# USO PRATICO DA PASTA ESCOLHIDA
# =============================================================================

# Garante que a extensao comece com ponto.
# Assim o usuario pode configurar "xlsx" ou ".xlsx".
extensao_normalizada = (
    extensao_desejada if extensao_desejada.startswith(".") else f".{extensao_desejada}"
)

# Lista somente arquivos da pasta escolhida; subpastas nao sao varridas.
# sorted deixa a ordem previsivel, facilitando conferencia e testes.
arquivos = sorted(pasta_escolhida.glob(f"*{extensao_normalizada}"))


# =============================================================================
# SAIDA NO TERMINAL
# =============================================================================

print("=" * 80)
print("EXEMPLO PROCEDURAL DE SELECAO DE DIRETORIO")
print("=" * 80)
print(f"Pasta escolhida : {pasta_escolhida}")
print(f"Extensao buscada: {extensao_normalizada}")
print(f"Arquivos achados: {len(arquivos)}")
print()

if not arquivos:
    print("Nenhum arquivo encontrado.")
else:
    for indice, arquivo in enumerate(arquivos, start=1):
        print(f"{indice:>3}. {arquivo.name}")
