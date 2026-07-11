from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
import yfinance as yf


@dataclass(slots=True)
class YahooProvider:
    """Provedor simples de dados históricos via Yahoo Finance."""

    auto_adjust: bool = True

    def get_historical_prices(
        self,
        symbol: str,
        period: str = "1y",
        interval: str = "1d",
    ) -> pd.DataFrame:
        ticker = symbol.strip().upper()
        if not ticker:
            raise ValueError("Informe um ticker válido.")

        data = yf.download(
            ticker,
            period=period,
            interval=interval,
            auto_adjust=self.auto_adjust,
            progress=False,
            threads=False,
        )

        if data.empty:
            raise ValueError(f"Nenhum dado encontrado para {ticker}.")

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        return data.dropna(how="all")
