# Inventário de arquivos XLSX em uma pasta

Este diretório contém um script em Python para gerar um inventário simples dos arquivos `.xlsx` existentes em uma pasta local.

O script coleta nome do arquivo, caminho completo, tamanho em KB e data/hora da última modificação. Em seguida, monta um `DataFrame` com `pandas`, exporta o resultado para um arquivo Excel temporário e abre esse arquivo automaticamente no Excel.

## Arquivo principal

- `inventario_arquivos_pasta_arquivo_xlsx_temp.py`

## Objetivo

Automatizar a conferência de arquivos de extração em pastas locais, especialmente em rotinas de conciliação, validação de cargas e controle de arquivos recebidos.

Esse tipo de rotina é útil quando há muitos arquivos `.xlsx` em uma pasta e é necessário verificar rapidamente:

- quantidade total de arquivos;
- nome de cada arquivo;
- caminho completo;
- tamanho em KB;
- última data/hora de modificação.

## Dependências

O script usa bibliotecas nativas do Python e a biblioteca externa `pandas`.

Bibliotecas nativas:

- `os`
- `glob`
- `tempfile`
- `datetime`
- `pathlib`

Biblioteca externa:

- `pandas`
- `openpyxl`, usado pelo `pandas` para gravar o arquivo `.xlsx`

Instalação:

```bash
pip install pandas openpyxl
```

Ou, usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Como usar

1. Abra o arquivo `inventario_arquivos_pasta_arquivo_xlsx_temp.py`.
2. Ajuste a variável `pasta` para o diretório que deseja monitorar/listar.
3. Execute o script.

Exemplo:

```python
pasta = r"C:\Users\seu_usuario\Documents\minha_pasta\extracoes"
```

Executar no terminal:

```bash
python inventario_arquivos_pasta_arquivo_xlsx_temp.py
```

## Saída esperada

O script imprime no console uma tabela com os arquivos encontrados e abre uma planilha temporária no Excel.

Exemplo de saída no console:

```text
             arquivo                                      caminho  tamanho_kb    modificado_em
base_001.xlsx  C:\extracoes\base_001.xlsx                       850.4  2026-06-10 09:30
base_002.xlsx  C:\extracoes\base_002.xlsx                      1290.8  2026-06-10 09:35

Total: 2 arquivo(s)
```

## Observações importantes

- O arquivo Excel gerado fica em uma pasta temporária do sistema operacional.
- O script não salva nenhum relatório dentro da pasta do projeto.
- A função `os.startfile()` funciona no Windows.
- Para Linux ou macOS, a abertura automática do arquivo exigiria adaptação.

## Uso recomendado

Este script é indicado para rotinas rápidas de conferência operacional antes de iniciar cargas, conciliações ou tratamentos de arquivos em massa.

Em projetos maiores, ele pode ser evoluído para:

- receber o caminho da pasta por parâmetro;
- gerar arquivo `.xlsx` em pasta definida pelo usuário;
- registrar logs;
- validar data de criação/modificação;
- filtrar arquivos por padrão de nome;
- comparar inventários entre execuções.
