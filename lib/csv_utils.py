from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List

import pandas as pd

from models.ledger_entry import LedgerEntry, LedgerFile


def read_ledger_csv(path: Path) -> LedgerFile:
    rows: List[LedgerEntry] = []
    with path.open() as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(LedgerEntry(**row))
    return LedgerFile(name=path.name, entries=rows)


def load_ledgers(directory: Path) -> list[LedgerFile]:
    return [read_ledger_csv(path) for path in sorted(directory.glob("*.csv"))]


def to_dataframe(ledger: LedgerFile) -> pd.DataFrame:
    data = [entry.dict() for entry in ledger.entries]
    return pd.DataFrame(data)


def aggregate_balances(ledgers: Iterable[LedgerFile]) -> pd.DataFrame:
    frames = [to_dataframe(ledger) for ledger in ledgers]
    if not frames:
        return pd.DataFrame(columns=["account", "debit", "credit"])
    combined = pd.concat(frames, ignore_index=True)
    grouped = combined.groupby("account").agg({"debit": "sum", "credit": "sum"})
    grouped["net"] = grouped["debit"] - grouped["credit"]
    return grouped.reset_index()
