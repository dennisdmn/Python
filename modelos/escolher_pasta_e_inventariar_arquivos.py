"""
Modelo evoluido: escolher uma pasta local e montar inventario de arquivos.

Objetivo:
- Abrir uma janela para o usuario escolher uma pasta.
- Listar arquivos por extensao.
- Criar um inventario simples com dados basicos dos arquivos encontrados.
- Exibir uma tabela no terminal com:
    nr_arquivo
    nome_arquivo
    extensao
    tamanho_kb
    data_modificacao

Observacoes:
- Este modelo nao varre subpastas.
- Por padrao, lista arquivos .xlsx.
- Para listar todos os arquivos, altere extensao="xlsx" para extensao="*".
"""

# datetime e usado para converter a data de modificacao do arquivo
# de timestamp numerico para texto legivel.
from datetime import datetime

# pathlib.Path e usado para trabalhar com caminhos de arquivos e pastas
# de forma mais moderna e segura do que concatenar strings manualmente.
from pathlib import Path

# Tk e filedialog sao usados para abrir uma janela nativa do Windows
# para o usuario escolher a pasta de entrada.
from tkinter import Tk, filedialog


def escolher_pasta(titulo: str = "Selecione uma pasta") -> Path:
    """
    Abre uma janela para o usuario escolher uma pasta.

    Parametros:
    - titulo: texto exibido no topo da janela de selecao.

    Retorno:
    - Path com o caminho da pasta escolhida.

    Se o usuario cancelar:
    - o script e interrompido com uma mensagem clara.
    """

    # Cria a janela principal do tkinter.
    # Essa janela e obrigatoria para conseguir abrir o filedialog.
    janela = Tk()

    # Oculta a janela principal.
    # Assim o usuario ve apenas a janela de selecao da pasta.
    janela.withdraw()

    # Mantem a janela de selecao acima das demais janelas abertas.
    # Isso evita que a janela fique escondida atras do VS Code.
    janela.attributes("-topmost", True)

    # Abre a janela para selecionar uma pasta.
    # initialdir=Path.home() faz a janela iniciar na pasta do usuario.
    pasta = filedialog.askdirectory(
        title=titulo,
        initialdir=Path.home(),
    )

    # Fecha a janela raiz do tkinter depois da escolha.
    # Isso libera recursos e evita janelas presas em memoria.
    janela.destroy()

    # Se o usuario clicar em Cancelar, a variavel pasta vem vazia.
    # Nesse caso, interrompemos o processo.
    if not pasta:
        raise SystemExit("Processo cancelado: nenhuma pasta foi selecionada.")

    # Retorna o caminho como Path, facilitando o uso de .glob(), .exists(), .name etc.
    return Path(pasta)


def listar_arquivos(pasta: Path, extensao: str = "xlsx") -> list[Path]:
    """
    Lista arquivos diretamente dentro da pasta escolhida.

    Parametros:
    - pasta: pasta onde os arquivos serao procurados.
    - extensao: extensao desejada.

    Exemplos:
    - extensao="xlsx"  -> busca arquivos .xlsx
    - extensao=".xlsx" -> tambem busca arquivos .xlsx
    - extensao="csv"   -> busca arquivos .csv
    - extensao="*"     -> busca todos os arquivos

    Retorno:
    - lista de objetos Path, um para cada arquivo encontrado.

    Observacao:
    - Nao varre subpastas.
    """

    # Se a extensao for "*", busca todos os arquivos.
    if extensao == "*":
        padrao_busca = "*"

    else:
        # Garante que a extensao tenha ponto.
        # Assim o usuario pode informar "xlsx" ou ".xlsx".
        extensao = extensao if extensao.startswith(".") else f".{extensao}"

        # Monta o padrao de busca usado pelo glob.
        # Exemplo: "*.xlsx"
        padrao_busca = f"*{extensao}"

    # pasta.glob(padrao_busca) lista os itens encontrados.
    # arquivo.is_file() garante que apenas arquivos entrem na lista, excluindo pastas.
    # sorted() organiza os arquivos em ordem alfabetica, facilitando conferencia.
    return sorted(arquivo for arquivo in pasta.glob(padrao_busca) if arquivo.is_file())


def montar_inventario(arquivos: list[Path]) -> list[dict[str, object]]:
    """
    Monta um inventario simples dos arquivos encontrados.

    Parametros:
    - arquivos: lista de arquivos retornada pela funcao listar_arquivos().

    Retorno:
    - lista de dicionarios.
    - cada dicionario representa uma linha da tabela final.

    Campos gerados:
    - nr_arquivo: numero sequencial do arquivo na lista.
    - nome_arquivo: nome do arquivo com extensao.
    - extensao: extensao do arquivo.
    - tamanho_kb: tamanho do arquivo em KB.
    - data_modificacao: ultima data/hora de modificacao.
    - caminho_completo: caminho completo do arquivo.
    """

    # Lista que armazenara uma linha de inventario para cada arquivo.
    inventario = []

    # enumerate cria uma numeracao sequencial.
    # start=1 faz a contagem comecar em 1, e nao em 0.
    for nr_arquivo, arquivo in enumerate(arquivos, start=1):

        # arquivo.stat() retorna propriedades do arquivo,
        # como tamanho, data de modificacao, data de criacao etc.
        dados_arquivo = arquivo.stat()

        # st_mtime e a data de modificacao em formato timestamp.
        # datetime.fromtimestamp converte para data/hora.
        # strftime formata a data para texto legivel.
        data_modificacao = datetime.fromtimestamp(
            dados_arquivo.st_mtime
        ).strftime("%Y-%m-%d %H:%M:%S")

        # Monta uma linha do inventario.
        linha_inventario = {
            "nr_arquivo": nr_arquivo,
            "nome_arquivo": arquivo.name,
            "extensao": arquivo.suffix.lower(),
            "tamanho_kb": round(dados_arquivo.st_size / 1024, 2),
            "data_modificacao": data_modificacao,
            "caminho_completo": str(arquivo),
        }

        # Adiciona a linha na lista final.
        inventario.append(linha_inventario)

    return inventario


def exibir_inventario(pasta: Path, inventario: list[dict[str, object]]) -> None:
    """
    Exibe o inventario no terminal em formato de tabela simples.

    Parametros:
    - pasta: pasta escolhida pelo usuario.
    - inventario: lista de dicionarios criada por montar_inventario().
    """

    # Cabecalho visual do relatorio no terminal.
    print("=" * 120)
    print("INVENTARIO DE ARQUIVOS")
    print("=" * 120)
    print(f"Pasta escolhida      : {pasta}")
    print(f"Arquivos encontrados : {len(inventario)}")
    print("=" * 120)

    # Se nao houver arquivos, exibe mensagem e encerra a funcao.
    if not inventario:
        print("Nenhum arquivo encontrado.")
        return

    # Imprime o cabecalho da tabela.
    # Os simbolos > e < controlam alinhamento:
    # > alinha a direita
    # < alinha a esquerda
    print(
        f"{'nr_arquivo':>10} | "
        f"{'nome_arquivo':<45} | "
        f"{'extensao':<8} | "
        f"{'tamanho_kb':>10} | "
        f"{'data_modificacao':<19}"
    )

    # Linha separadora entre cabecalho e dados.
    print("-" * 120)

    # Percorre cada linha do inventario e imprime em formato tabular.
    for item in inventario:
        print(
            f"{item['nr_arquivo']:>10} | "
            f"{str(item['nome_arquivo'])[:45]:<45} | "
            f"{item['extensao']:<8} | "
            f"{item['tamanho_kb']:>10.2f} | "
            f"{item['data_modificacao']:<19}"
        )


def main() -> None:
    """
    Funcao principal do script.

    Fluxo:
    1. Usuario escolhe a pasta de entrada.
    2. Script lista os arquivos da extensao definida.
    3. Script monta o inventario dos arquivos encontrados.
    4. Script exibe o inventario no terminal.
    """

    # Etapa 1: usuario escolhe a pasta.
    pasta_entrada = escolher_pasta("Selecione a pasta de entrada")

    # Etapa 2: lista arquivos da pasta escolhida.
    # Troque extensao="xlsx" por extensao="*" se quiser listar todos os arquivos.
    arquivos = listar_arquivos(pasta_entrada, extensao="xlsx")

    # Etapa 3: monta a estrutura tabular com propriedades dos arquivos.
    inventario = montar_inventario(arquivos)

    # Etapa 4: exibe o resultado no terminal.
    exibir_inventario(pasta_entrada, inventario)


# Este bloco garante que o script so execute automaticamente
# quando for rodado diretamente pelo Python.
#
# Se este arquivo for importado por outro script, o main() nao roda sozinho.
if __name__ == "__main__":
    main()
