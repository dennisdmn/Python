from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

from analytics.indicators import add_indicators
from providers.yahoo_provider import YahooProvider


st.set_page_config(page_title="US Stock Market App", layout="wide")
st.title("US Stock Market App")
st.caption("Protótipo educacional com dados gratuitos do Yahoo Finance")

with st.sidebar:
    symbol = st.text_input("Ticker", value="AAPL").strip().upper()
    period = st.selectbox("Período", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)
    load_data = st.button("Consultar", type="primary", use_container_width=True)

if load_data or symbol:
    try:
        provider = YahooProvider()
        prices = provider.get_historical_prices(symbol=symbol, period=period)
        data = add_indicators(prices)

        latest = data.iloc[-1]
        previous = data.iloc[-2] if len(data) > 1 else latest
        variation = ((latest["Close"] / previous["Close"]) - 1) * 100 if previous["Close"] else 0

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Fechamento", f"US$ {latest['Close']:,.2f}", f"{variation:.2f}%")
        col2.metric("Máxima", f"US$ {latest['High']:,.2f}")
        col3.metric("Mínima", f"US$ {latest['Low']:,.2f}")
        col4.metric("Volume", f"{latest['Volume']:,.0f}")

        price_chart = go.Figure()
        price_chart.add_trace(go.Scatter(x=data.index, y=data["Close"], name="Fechamento"))
        price_chart.add_trace(go.Scatter(x=data.index, y=data["SMA_20"], name="SMA 20"))
        price_chart.add_trace(go.Scatter(x=data.index, y=data["SMA_50"], name="SMA 50"))
        price_chart.update_layout(title=f"{symbol} — preço e médias móveis", xaxis_title="Data", yaxis_title="Preço (US$)")
        st.plotly_chart(price_chart, use_container_width=True)

        rsi_chart = go.Figure()
        rsi_chart.add_trace(go.Scatter(x=data.index, y=data["RSI_14"], name="RSI 14"))
        rsi_chart.add_hline(y=70, line_dash="dash")
        rsi_chart.add_hline(y=30, line_dash="dash")
        rsi_chart.update_layout(title="Índice de Força Relativa", xaxis_title="Data", yaxis_title="RSI")
        st.plotly_chart(rsi_chart, use_container_width=True)

        with st.expander("Visualizar dados"):
            st.dataframe(data.sort_index(ascending=False), use_container_width=True)

    except Exception as exc:
        st.error(f"Não foi possível carregar os dados: {exc}")
