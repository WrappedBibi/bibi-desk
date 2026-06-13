"""Portfolio level allocation across symbols (draft).

The single-symbol desk sizes each trade in isolation. This module is the start
of a portfolio layer that scales the per-symbol Kelly fractions down so the
gross book respects a total risk budget and a per-cluster cap. Not wired into
the desk loop yet.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Allocation:
    symbol: str
    target_fraction: float
    capped: bool


def scale_to_budget(fractions: dict[str, float], gross_budget: float = 3.0) -> list[Allocation]:
    """Scale per-symbol fractions so their sum does not exceed gross_budget.

    Proportional shrink: if the raw book asks for more than the budget, every
    leg is multiplied by budget / total so relative conviction is preserved.
    """
    total = sum(abs(f) for f in fractions.values())
    if total <= gross_budget or total == 0.0:
        return [Allocation(s, f, False) for s, f in fractions.items()]
    k = gross_budget / total
    return [Allocation(s, f * k, True) for s, f in fractions.items()]


# TODO: correlation aware clustering so two highly correlated longs share a cap.
# TODO: hook into Desk.run() once the single-symbol path is fully proven.
