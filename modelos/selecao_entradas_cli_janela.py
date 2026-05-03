"""
Modelo reutilizavel: selecao de entradas por CLI ou janela grafica.

Objetivo:
- Permitir que um script local escolha pasta de entrada, pasta de saida e arquivo de apoio.
- Funcionar tanto em uso manual, com janela do Windows, quanto em uso tecnico, por linha de comando.
- Evitar caminhos fixos espalhados pelo codigo.
- Retornar caminhos como pathlib.Path, facilitando manutencao e reaproveitamento.

Quando usar:
- Rotinas que processam arquivos Excel, CSV, TXT ou bases extraidas de sistemas.
- Scripts de conciliacao, validacao, consolidacao ou geracao de relatorios.
- Fluxos que precisam rodar manualmente no computador do usuario e tambem por automacao.

Exemplo de execucao manual:
    python modelos/selecao_entradas_cli_janela.py

Exemplo de execucao sem janela:
    python modelos/selecao_entradas_cli_janela.py ^
        --pasta-entrada "C:\\Bases\\Entrada" ^
        --pasta-saida "C:\\Bases\\Saida" ^
        --arquivo-apoio "C:\\Bases\\Apoio\\balancete.xlsx" ^
        --sem-janela
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class EntradasExecucao:
    """
    Contrato unico com as entradas efetivas do script.

    Vantagem:
    - Em vez de passar varios parametros soltos entre funcoes, o fluxo recebe
      um objeto unico, legivel e facil de testar.
    """

    pasta_entrada: Path
    pasta_saida: Path
    arquivo_apoio: Path | None


def escolher_pasta(
    titulo: str,
    pasta_inicial: Path | str | None = None,
    obrigatoria: bool = True,
) -> Path | None:
    """
    Abre uma janela para o usuario escolher uma pasta.

    Retorna:
    - Path com a pasta escolhida; ou
    - None, quando a selecao nao for obrigatoria e o usuario cancelar.

    Se a pasta for obrigatoria e o usuario cancelar, o script e interrompido
    com mensagem clara.
    """

    pasta_base = Path(pasta_inicial) if pasta_inicial else Path.home()

    try:
        from tkinter import Tk, filedialog

        janela = Tk()
        janela.withdraw()
        janela.attributes("-topmost", True)

        pasta_escolhida = filedialog.askdirectory(
            title=titulo,
            initialdir=pasta_base,
        )

        janela.destroy()

    except Exception as exc:
        raise SystemExit(f"Nao foi possivel abrir a janela de selecao de pasta: {exc}") from exc

    if not pasta_escolhida:
        if obrigatoria:
            raise SystemExit(f"Processo cancelado: {titulo}")
        return None

    return Path(pasta_escolhida)


def escolher_arquivo(
    titulo: str,
    pasta_inicial: Path | str | None = None,
    extensoes: tuple[tuple[str, str], ...] = (("Arquivos Excel", "*.xlsx"),),
    obrigatorio: bool = False,
) -> Path | None:
    """
    Abre uma janela para o usuario escolher um arquivo.

    Por padrao, considera o arquivo como opcional. Para arquivos obrigatorios,
    informe obrigatorio=True.
    """

    pasta_base = Path(pasta_inicial) if pasta_inicial else Path.home()

    try:
        from tkinter import Tk, filedialog

        janela = Tk()
        janela.withdraw()
        janela.attributes("-topmost", True)

        arquivo_escolhido = filedialog.askopenfilename(
            title=titulo,
            initialdir=pasta_base,
            filetypes=list(extensoes),
        )

        janela.destroy()

    except Exception as exc:
        raise SystemExit(f"Nao foi possivel abrir a janela de selecao de arquivo: {exc}") from exc

    if not arquivo_escolhido:
        if obrigatorio:
            raise SystemExit(f"Processo cancelado: {titulo}")
        return None

    return Path(arquivo_escolhido)


def validar_pasta_existente(caminho: Path, nome_parametro: str) -> Path:
    """
    Valida se uma pasta existe antes de continuar o processamento.
    """

    if not caminho.exists() or not caminho.is_dir():
        raise SystemExit(f"{nome_parametro} invalida ou inexistente: {caminho}")

    return caminho


def validar_arquivo_existente(caminho: Path | None, nome_parametro: str) -> Path | None:
    """
    Valida arquivo opcional, quando informado.
    """

    if caminho is None:
        return None

    if not caminho.exists() or not caminho.is_file():
        raise SystemExit(f"{nome_parametro} invalido ou inexistente: {caminho}")

    return caminho


def resolver_entradas(
    pasta_entrada: Path | None,
    pasta_saida: Path | None,
    arquivo_apoio: Path | None,
    usar_janela: bool,
) -> EntradasExecucao:
    """
    Resolve as entradas do script com a seguinte prioridade:

    1. Usa o caminho informado por parametro de linha de comando.
    2. Se nao foi informado e usar_janela=True, abre janela para o usuario escolher.
    3. Se nao foi informado e usar_janela=False, interrompe quando a entrada for obrigatoria.

    Neste modelo:
    - pasta_entrada e obrigatoria;
    - pasta_saida e obrigatoria;
    - arquivo_apoio e opcional.
    """

    if pasta_entrada is None:
        if not usar_janela:
            raise SystemExit("Informe --pasta-entrada ou execute sem --sem-janela.")
        pasta_entrada = escolher_pasta(
            titulo="Selecione a pasta de entrada",
            pasta_inicial=Path.home(),
            obrigatoria=True,
        )

    if pasta_saida is None:
        if not usar_janela:
            raise SystemExit("Informe --pasta-saida ou execute sem --sem-janela.")
        pasta_saida = escolher_pasta(
            titulo="Selecione a pasta de saida",
            pasta_inicial=Path.home(),
            obrigatoria=True,
        )

    if arquivo_apoio is None and usar_janela:
        arquivo_apoio = escolher_arquivo(
            titulo="Selecione um arquivo de apoio, se houver",
            pasta_inicial=pasta_entrada,
            extensoes=(
                ("Arquivos Excel", "*.xlsx"),
                ("Arquivos CSV", "*.csv"),
                ("Todos os arquivos", "*.*"),
            ),
            obrigatorio=False,
        )

    pasta_entrada = validar_pasta_existente(Path(pasta_entrada), "Pasta de entrada")
    pasta_saida = validar_pasta_existente(Path(pasta_saida), "Pasta de saida")
    arquivo_apoio = validar_arquivo_existente(arquivo_apoio, "Arquivo de apoio")

    return EntradasExecucao(
        pasta_entrada=pasta_entrada,
        pasta_saida=pasta_saida,
        arquivo_apoio=arquivo_apoio,
    )


def criar_parser() -> argparse.ArgumentParser:
    """
    Centraliza os parametros de linha de comando.

    Boa pratica:
    - Quem opera manualmente pode usar janelas.
    - Quem automatiza pode informar caminhos e usar --sem-janela.
    """

    parser = argparse.ArgumentParser(
        description="Modelo de selecao de entradas por CLI ou janela grafica."
    )
    parser.add_argument(
        "--pasta-entrada",
        type=Path,
        help="Pasta com os arquivos de entrada.",
    )
    parser.add_argument(
        "--pasta-saida",
        type=Path,
        help="Pasta onde os arquivos de saida serao gravados.",
    )
    parser.add_argument(
        "--arquivo-apoio",
        type=Path,
        help="Arquivo opcional de apoio, como balancete, de-para ou parametros.",
    )
    parser.add_argument(
        "--sem-janela",
        action="store_true",
        help="Nao abre janelas graficas. Exige que as entradas obrigatorias sejam informadas por parametro.",
    )
    return parser


def exibir_resumo_entradas(entradas: EntradasExecucao) -> None:
    """
    Exibe as entradas resolvidas para conferencia operacional.
    """

    print("=" * 80)
    print("ENTRADAS RESOLVIDAS")
    print("=" * 80)
    print(f"Pasta de entrada : {entradas.pasta_entrada}")
    print(f"Pasta de saida   : {entradas.pasta_saida}")
    print(f"Arquivo de apoio : {entradas.arquivo_apoio or 'Nao informado'}")
    print("=" * 80)


def main() -> None:
    """
    Exemplo de uso do modelo.

    Em um projeto real, depois de resolver as entradas, o proximo passo seria
    chamar funcoes como:
    - listar arquivos da pasta de entrada;
    - validar cabecalhos;
    - consolidar bases;
    - gerar relatorios na pasta de saida.
    """

    args = criar_parser().parse_args()

    entradas = resolver_entradas(
        pasta_entrada=args.pasta_entrada,
        pasta_saida=args.pasta_saida,
        arquivo_apoio=args.arquivo_apoio,
        usar_janela=not args.sem_janela,
    )

    exibir_resumo_entradas(entradas)


if __name__ == "__main__":
    main()
