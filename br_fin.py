from __future__ import annotations

"""
BlackRoad Finance Pack CLI
Main entry point for finance pack operations.
"""

import sys
from decimal import Decimal
from datetime import datetime
from typing import Literal


class FinancePack:
    """Main CLI interface for BlackRoad Finance Pack."""
    
    def __init__(self):
        self.pack_id = "pack.finance"
        self.version = "0.1.0"
        self.agents = ["budgeteer", "reconcile", "forecast", "audit"]
    
    def info(self) -> dict:
        """Display pack information."""
        return {
            "pack_id": self.pack_id,
            "version": self.version,
            "agents": self.agents,
            "status": "active",
        }
    
    def list_agents(self) -> list[str]:
        """List available agents."""
        return self.agents
    
    def run_agent(self, agent_name: str, *args) -> None:
        """Run a specific agent."""
        if agent_name not in self.agents:
            print(f"Unknown agent: {agent_name}")
            print(f"Available agents: {', '.join(self.agents)}")
            return
        
        print(f"Running agent: {agent_name}")
        # Agent execution would be implemented here
        # TODO(cli): Implement agent execution logic
    
    def help(self) -> None:
        """Display help information."""
        print(f"""
BlackRoad Finance Pack v{self.version}

Usage:
  br_fin info              - Show pack information
  br_fin list              - List available agents
  br_fin run <agent> ...   - Run a specific agent
  br_fin help              - Show this help message

Available agents:
  {chr(10).join(f'  - {agent}' for agent in self.agents)}

Examples:
  br_fin run budgeteer check budget-001 5000.00
  br_fin run reconcile account-001 2024-01-01 2024-01-31
  br_fin run forecast revenue monthly
  br_fin run audit ledger.csv
        """.strip())


def main():
    """Main CLI entry point."""
    pack = FinancePack()
    
    if len(sys.argv) < 2:
        pack.help()
        return
    
    command = sys.argv[1]
    
    if command == "info":
        info = pack.info()
        print(f"Pack: {info['pack_id']}")
        print(f"Version: {info['version']}")
        print(f"Status: {info['status']}")
        print(f"Agents: {', '.join(info['agents'])}")
    
    elif command == "list":
        print("Available agents:")
        for agent in pack.list_agents():
            print(f"  - {agent}")
    
    elif command == "run":
        if len(sys.argv) < 3:
            print("Error: Agent name required")
            print("Usage: br_fin run <agent> [args...]")
            return
        
        agent_name = sys.argv[2]
        pack.run_agent(agent_name, *sys.argv[3:])
    
    elif command == "help":
        pack.help()
    
    else:
        print(f"Unknown command: {command}")
        pack.help()


if __name__ == "__main__":
    main()
