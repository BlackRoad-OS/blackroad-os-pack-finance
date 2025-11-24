from __future__ import annotations

from pathlib import Path

from lib.csv_utils import load_ledgers


def reconcile_file(path: Path) -> dict[str, float]:
    ledger = load_ledgers(path.parent)
    target = next((l for l in ledger if l.name == path.name), None)
    if target is None:
        raise FileNotFoundError(path)
    return target.summary()


def reconcile_directory(path: Path) -> list[dict[str, float]]:
    ledgers = load_ledgers(path)
    return [ledger.summary() for ledger in ledgers]


if __name__ == "__main__":
    result = reconcile_file(Path("ledgers/2025-11-24-general.csv"))
    print("Reconcile summary", result)
