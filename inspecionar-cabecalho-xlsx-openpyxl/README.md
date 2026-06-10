# Inspecionar cabeçalho de arquivo XLSX com openpyxl

Este diretório contém um exemplo simples em Python para inspecionar a estrutura de um arquivo Excel `.xlsx` usando a biblioteca `openpyxl`.

O script abre o arquivo em modo somente leitura, lista as abas existentes e imprime o cabeçalho da primeira linha de cada aba.

## Arquivo principal

- `exemplo_inspecionar_cabecalho_xlsx_openpyxl.py`

## Objetivo

Facilitar a conferência rápida da estrutura de arquivos Excel antes de iniciar cargas, tratamentos, validações ou conciliações.

Esse tipo de inspeção é útil para verificar:

- nome do arquivo analisado;
- abas disponíveis no arquivo;
- quantidade de colunas por aba;
- quantidade estimada de linhas por aba;
- nome das colunas/cabeçalhos da primeira linha.

## Dependências

O script usa:

- `pathlib`, biblioteca nativa do Python;
- `openpyxl`, biblioteca externa para leitura de arquivos `.xlsx`.

Instalação:

```bash
pip install openpyxl
```

Ou, usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Como usar

1. Abra o arquivo `exemplo_inspecionar_cabecalho_xlsx_openpyxl.py`.
2. Ajuste a variável `arquivo` para apontar para o arquivo `.xlsx` desejado.
3. Execute o script.

Exemplo:

```python
arquivo = Path(r"C:\Users\seu_usuario\Documents\arquivo.xlsx")
```

Executar no terminal:

```bash
python exemplo_inspecionar_cabecalho_xlsx_openpyxl.py
```

## Saída esperada

O script imprime no console o nome do arquivo, a lista de abas e, para cada aba, a quantidade de colunas, linhas estimadas e cabeçalhos encontrados.

Exemplo:

```text
Arquivo : arquivo.xlsx
Abas    : ['Planilha1', 'Base']

Aba     : Planilha1
Colunas : 3
Linhas  : 100 (estimado)
    1. ID
    2. Data
    3. Valor
```

## Observações importantes

- O parâmetro `read_only=True` torna a leitura mais leve para arquivos grandes.
- O parâmetro `data_only=True` retorna o valor calculado das fórmulas, quando disponível no arquivo.
- `ws.max_row - 1` é uma estimativa de linhas de dados, pois considera que a primeira linha é o cabeçalho.
- O script não altera o arquivo original.
- Ao final, o arquivo é fechado com `wb.close()`.

## Uso recomendado

Use este exemplo antes de desenvolver processos de importação, tratamento ou validação de arquivos Excel, especialmente quando não há certeza sobre a estrutura de abas e colunas.
