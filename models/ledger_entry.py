from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, validator


class LedgerEntry(BaseModel):
    date: date = Field(..., description="Transaction date")
    account: str = Field(..., description="Account name")
    debit: float | None = Field(0.0, description="Debit amount")
    credit: float | None = Field(0.0, description="Credit amount")
    description: Optional[str] = Field(None, description="Entry detail")

    @validator("debit", "credit", pre=True)
    def empty_to_zero(cls, value: float | None) -> float:
        return float(value or 0)

    @validator("debit", "credit")
    def non_negative(cls, value: float) -> float:
        if value < 0:
            raise ValueError("Amounts must be non-negative")
        return value

    @property
    def net(self) -> float:
        return (self.debit or 0) - (self.credit or 0)

    def is_balanced(self) -> bool:
        return abs(self.net) < 1e-6


class LedgerFile(BaseModel):
    name: str
    entries: list[LedgerEntry]

    def total_debits(self) -> float:
        return sum(e.debit or 0 for e in self.entries)

    def total_credits(self) -> float:
        return sum(e.credit or 0 for e in self.entries)

    def imbalance(self) -> float:
        return round(self.total_debits() - self.total_credits(), 2)

    def summary(self) -> dict[str, float]:
        return {
            "entries": len(self.entries),
            "debits": self.total_debits(),
            "credits": self.total_credits(),
            "imbalance": self.imbalance(),
        }
