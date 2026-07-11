# Stock Market App

Aplicação Python open source para consultar e analisar ações do mercado americano usando fontes gratuitas.

## Recursos iniciais

- Consulta de cotações históricas com `yfinance`
- Gráfico de preços e volume
- Médias móveis de 20 e 50 períodos
- Indicador RSI de 14 períodos
- Resumo estatístico do ativo
- Estrutura preparada para novos provedores, como SEC EDGAR, FRED e Finnhub

## Instalação

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run app.py
```

## Estrutura

```text
stock-market-app/
├── app.py
├── requirements.txt
├── .gitignore
├── analytics/
│   ├── __init__.py
│   └── indicators.py
└── providers/
    ├── __init__.py
    └── yahoo_provider.py
```

## Próximas etapas

- Integração com SEC EDGAR para demonstrações financeiras oficiais
- Integração com FRED para indicadores macroeconômicos
- Integração com Finnhub para notícias e calendário de resultados
- Comparação entre empresas do mesmo setor
- Persistência local com DuckDB ou SQLite
- Testes automatizados

## Aviso

Este projeto tem finalidade educacional. Dados do Yahoo Finance podem sofrer atrasos, indisponibilidades ou mudanças de formato. Não use o conteúdo como recomendação de investimento.
