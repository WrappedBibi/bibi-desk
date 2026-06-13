"""Risk parity weighting experiment (draft, not in the desk path).

Instead of equal-dollar or pure-Kelly weights, size each symbol inversely to its
realized volatility so every position contributes roughly the same variance.
Kept on a branch while we compare it against half-Kelly on the backtester.
"""
from __future__ import annotations

import numpy as np


def inverse_vol_weights(returns: np.ndarray) -> np.ndarray:
    """Columns are per-symbol return series. Returns weights summing to 1."""
    vol = np.std(returns, axis=0, ddof=1)
    vol = np.where(vol < 1e-9, 1e-9, vol)
    inv = 1.0 / vol
    return inv / inv.sum()


# Open question: does risk parity beat half-Kelly once fees are netted out on
# the 1h book? Early backtests say it lowers drawdown but also clips the edge.
