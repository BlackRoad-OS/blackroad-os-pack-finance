from __future__ import annotations

from datetime import date
from typing import Dict

from pydantic import BaseModel, Field


class BudgetLine(BaseModel):
    account: str = Field(..., description="Account name")
    monthly_limit: float = Field(..., ge=0, description="Planned monthly spend")
    owner: str = Field(..., description="Budget owner")


class BudgetModel(BaseModel):
    effective_date: date = Field(..., description="Budget start date")
    lines: list[BudgetLine]

    def to_summary(self) -> Dict[str, float]:
        return {line.account: line.monthly_limit for line in self.lines}

    def variance(self, actuals: Dict[str, float]) -> Dict[str, float]:
        summary = self.to_summary()
        variances: Dict[str, float] = {}
        for account, planned in summary.items():
            actual = actuals.get(account, 0)
            variances[account] = round(actual - planned, 2)
        return variances
