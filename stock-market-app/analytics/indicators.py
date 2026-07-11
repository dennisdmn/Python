from __future__ import annotations

import pandas as pd


def add_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """Adiciona médias móveis e RSI ao DataFrame de preços."""
    result = data.copy()

    if "Close" not in result.columns:
        raise KeyError("A coluna 'Close' não foi encontrada.")

    result["SMA_20"] = result["Close"].rolling(window=20).mean()
    result["SMA_50"] = result["Close"].rolling(window=50).mean()

    delta = result["Close"].diff()
    gains = delta.clip(lower=0)
    losses = -delta.clip(upper=0)

    average_gain = gains.rolling(window=14).mean()
    average_loss = losses.rolling(window=14).mean()
    relative_strength = average_gain / average_loss.replace(0, pd.NA)

    result["RSI_14"] = 100 - (100 / (1 + relative_strength))
    return result
