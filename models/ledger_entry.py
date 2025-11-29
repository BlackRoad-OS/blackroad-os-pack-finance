from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Literal


@dataclass
class LedgerEntry:
    """Represents a financial ledger entry."""
    
    id: str
    timestamp: datetime
    account: str
    description: str
    amount: Decimal
    currency: str = "USD"
    entry_type: Literal["debit", "credit"] = "debit"
    category: str | None = None
    tags: list[str] | None = None
    metadata: dict[str, str] | None = None
    
    def __post_init__(self):
        """Ensure amount is a Decimal."""
        if not isinstance(self.amount, Decimal):
            self.amount = Decimal(str(self.amount))
        
        if self.tags is None:
            self.tags = []
        
        if self.metadata is None:
            self.metadata = {}
    
    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "account": self.account,
            "description": self.description,
            "amount": str(self.amount),
            "currency": self.currency,
            "entry_type": self.entry_type,
            "category": self.category,
            "tags": self.tags,
            "metadata": self.metadata,
        }
