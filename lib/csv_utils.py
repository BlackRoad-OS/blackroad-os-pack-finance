from __future__ import annotations

import csv
from typing import Any, Protocol
from decimal import Decimal
from datetime import datetime
from pathlib import Path


class CSVReader(Protocol):
    """Protocol for CSV reading operations."""
    
    def read(self, path: Path) -> list[dict[str, Any]]:
        """Read CSV file and return list of dictionaries."""
        ...


class CSVWriter(Protocol):
    """Protocol for CSV writing operations."""
    
    def write(self, path: Path, data: list[dict[str, Any]]) -> None:
        """Write data to CSV file."""
        ...


def read_ledger_csv(path: Path) -> list[dict[str, Any]]:
    """Read ledger entries from CSV file."""
    entries = []
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            entries.append({
                'id': row['id'],
                'timestamp': datetime.fromisoformat(row['timestamp']),
                'account': row['account'],
                'description': row['description'],
                'amount': Decimal(row['amount']),
                'currency': row.get('currency', 'USD'),
                'entry_type': row.get('entry_type', 'debit'),
                'category': row.get('category'),
            })
    return entries


def write_ledger_csv(path: Path, entries: list[dict[str, Any]]) -> None:
    """Write ledger entries to CSV file."""
    if not entries:
        return
    
    fieldnames = ['id', 'timestamp', 'account', 'description', 'amount', 
                  'currency', 'entry_type', 'category']
    
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            row = {
                'id': entry['id'],
                'timestamp': entry['timestamp'].isoformat() if isinstance(entry['timestamp'], datetime) else entry['timestamp'],
                'account': entry['account'],
                'description': entry['description'],
                'amount': str(entry['amount']),
                'currency': entry.get('currency', 'USD'),
                'entry_type': entry.get('entry_type', 'debit'),
                'category': entry.get('category', ''),
            }
            writer.writerow(row)
