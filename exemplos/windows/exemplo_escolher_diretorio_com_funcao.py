"""
Exemplo reutilizavel: escolher uma pasta/diretorio no Windows e listar arquivos.

Objetivo:
- Demonstrar como permitir que o usuario escolha uma pasta com janela grafica.
- Manter fallback seguro para ambientes sem interface grafica.
- Mostrar um uso pratico da pasta escolhida: listar arquivos por extensao.

Bibliotecas escolhidas:
- pathlib.Path:
    Biblioteca padrao do Python para manipular caminhos de forma moderna,
    legivel e independente de concatenacao manual de strings.

- tkinter:
    Biblioteca padrao do Python para interface grafica simples.
    Foi escolhida porque nao exige instalacao adicional e atende bem ao caso
    de abrir uma janela nativa para selecao de diretorio.

- typing.Optional:
    Usada para deixar claro que o parametro pasta_padrao pode receber um caminho
    ou None. Isso melhora a leitura da assinatura da funcao.
"""

from pathlib import Path
from typing import Optional


def escolher_diretorio(
    titulo: str = "Selecione uma pasta",
    pasta_padrao: Optional[Path | str] = None,
    usar_janela: bool = True,
) -> Path:
    """
    Retorna uma pasta escolhida pelo usuario.

    Regras da funcao:
    - Se usar_janela=False, retorna diretamente a pasta_padrao.
    - Se o usuario cancelar a selecao, retorna a pasta_padrao.
    - Se a janela nao puder ser aberta, retorna a pasta_padrao.
    - Se pasta_padrao nao for informada, usa a pasta atual de execucao.
    """

    # Converte a pasta padrao para Path.
    # Se nenhuma pasta for informada, usa o diretorio atual onde o script foi executado.
    pasta_base = Path(pasta_padrao) if pasta_padrao else Path.cwd()

    # Permite desligar a janela grafica em automacoes, testes ou servidores sem interface.
    if not usar_janela:
        return pasta_base

    try:
        # Import local: tkinter so e carregado quando a janela realmente sera usada.
        # Isso evita dependencia desnecessaria quando usar_janela=False.
        from tkinter import Tk, filedialog

        # Cria uma janela raiz do tkinter.
        # Ela e necessaria para abrir o seletor de pasta.
        janela = Tk()

        # Oculta a janela principal, deixando visivel apenas o seletor de diretorio.
        janela.withdraw()

        # Mantem a janela de selecao acima das demais, reduzindo chance de o usuario perder a janela.
        janela.attributes("-topmost", True)

        # Abre o seletor de pasta.
        # initialdir posiciona o usuario na pasta padrao, mas permite escolher outra.
        pasta_escolhida = filedialog.askdirectory(
            title=titulo,
            initialdir=pasta_base,
        )

        # Fecha a janela raiz depois da escolha para liberar recursos.
        janela.destroy()

    except Exception as exc:
        # Fallback defensivo:
        # Se tkinter falhar, se nao houver interface grafica ou ocorrer outro erro,
        # o processo continua usando a pasta padrao.
        print(f"Nao foi possivel abrir a janela de selecao de pasta: {exc}")
        print(f"Usando pasta padrao: {pasta_base}")
        return pasta_base

    # Se o usuario clicar em Cancelar, askdirectory retorna string vazia.
    # Nesse caso, usamos a pasta padrao em vez de interromper o programa.
    if not pasta_escolhida:
        print(f"Nenhuma pasta selecionada. Usando pasta padrao: {pasta_base}")
        return pasta_base

    # Retorna sempre Path, mantendo o tipo consistente para quem chamar a funcao.
    return Path(pasta_escolhida)


def listar_arquivos_por_extensao(
    pasta: Path,
    extensao: str = ".xlsx",
    limite: int | None = None,
) -> list[Path]:
    """
    Lista arquivos de uma pasta por extensao.

    Exemplos:
    - extensao=".xlsx"
    - extensao="csv"
    - extensao=".txt"

    Observacao:
    - A busca e feita apenas na pasta informada.
    - Subpastas nao sao varridas.
    """

    # Garante que a extensao comece com ponto.
    # Assim o usuario pode passar "xlsx" ou ".xlsx".
    extensao = extensao if extensao.startswith(".") else f".{extensao}"

    # glob busca arquivos que terminam com a extensao informada.
    # sorted deixa a ordem previsivel, facilitando conferencia e testes.
    arquivos = sorted(pasta.glob(f"*{extensao}"))

    # Limite opcional para testes rapidos em pastas grandes.
    if limite is not None:
        arquivos = arquivos[:limite]

    return arquivos


def exibir_resumo_arquivos(pasta: Path, arquivos: list[Path], extensao: str) -> None:
    """
    Exibe no terminal um resumo simples dos arquivos encontrados.
    """

    print("=" * 80)
    print("EXEMPLO DE SELECAO DE DIRETORIO")
    print("=" * 80)
    print(f"Pasta escolhida : {pasta}")
    print(f"Extensao buscada: {extensao}")
    print(f"Arquivos achados: {len(arquivos)}")
    print()

    if not arquivos:
        print("Nenhum arquivo encontrado.")
        return

    for indice, arquivo in enumerate(arquivos, start=1):
        print(f"{indice:>3}. {arquivo.name}")


# =============================================================================
# EXEMPLO DE USO REUTILIZAVEL
# =============================================================================
#
# Em outro script do projeto, voce poderia importar apenas a funcao
# escolher_diretorio e usar assim:
#
# from exemplos.windows.exemplo_escolher_diretorio_com_funcao import escolher_diretorio
#
# pasta_bases = escolher_diretorio(
#     titulo="Selecione a pasta das bases",
#     pasta_padrao=r"C:\Python\Projeto_Conciliacao_Contabil_v2\_Bases_Razoes",
#     usar_janela=True,
# )
#
# print(f"Pasta selecionada: {pasta_bases}")
#
# A vantagem desse formato e que a funcao pode ser reaproveitada sem executar
# todo o exemplo de listagem de arquivos. Isso acontece porque o bloco main()
# so roda quando este arquivo e executado diretamente.


def exemplo_reuso_funcao() -> None:
    """
    Exemplo didatico de como reutilizar apenas a funcao escolher_diretorio.

    Em um script real, voce poderia importar assim:

        from exemplos.windows.exemplo_escolher_diretorio_com_funcao import escolher_diretorio

    Depois, chamaria a funcao para obter a pasta desejada.
    """

    # Exemplo parecido com o fluxo dos arquivos de razao.
    # Aqui indicamos uma pasta padrao, mas permitimos que o usuario escolha outra.
    pasta_bases = escolher_diretorio(
        titulo="Selecione a pasta das bases",
        pasta_padrao=r"C:\Python\Projeto_Conciliacao_Contabil_v2\_Bases_Razoes",
        usar_janela=True,
    )

    # Depois que a funcao retorna, pasta_bases ja e um objeto Path.
    # Isso permite usar metodos como .glob(), .exists(), .is_dir(), etc.
    print(f"Pasta selecionada: {pasta_bases}")


def main() -> None:
    """
    Fluxo principal do exemplo completo.

    Este main mostra um uso pratico:
    1. Escolher uma pasta.
    2. Listar arquivos .xlsx dentro dela.
    3. Exibir o resultado no terminal.
    """

    # Pasta inicial sugerida ao usuario.
    # Em um projeto real, poderia ser uma pasta de entrada, bases, relatorios etc.
    pasta_padrao = Path.cwd()

    # Parametro central do exemplo.
    # Troque para ".csv", ".txt", ".xlsx" etc. conforme a necessidade.
    extensao_desejada = ".xlsx"

    # Escolhe a pasta de entrada.
    pasta = escolher_diretorio(
        titulo="Selecione a pasta com os arquivos de entrada",
        pasta_padrao=pasta_padrao,
        usar_janela=True,
    )

    # Usa a pasta escolhida em uma tarefa pratica.
    arquivos = listar_arquivos_por_extensao(
        pasta=pasta,
        extensao=extensao_desejada,
        limite=None,
    )

    # Mostra o resultado ao usuario.
    exibir_resumo_arquivos(
        pasta=pasta,
        arquivos=arquivos,
        extensao=extensao_desejada,
    )


# Este bloco garante que o exemplo completo so rode quando o arquivo for executado diretamente.
# Se o arquivo for importado por outro script, as funcoes ficam disponiveis sem executar o main().
if __name__ == "__main__":
    main()
