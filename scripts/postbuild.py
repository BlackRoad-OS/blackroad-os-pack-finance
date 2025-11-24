from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

BEACON_PATH = Path("public/sig.beacon.json")


def write_beacon(path: Path = BEACON_PATH) -> None:
    payload = {"ts": datetime.utcnow().isoformat(), "agent": "FinancePack-Gen-0"}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2))


if __name__ == "__main__":
    write_beacon()
