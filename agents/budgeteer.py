from __future__ import annotations

from decimal import Decimal
from datetime import datetime
from typing import Protocol


class BudgetService(Protocol):
    """Protocol for budget management service."""
    
    def get_budget(self, budget_id: str) -> dict:
        """Retrieve budget by ID."""
        ...
    
    def update_spent(self, budget_id: str, amount: Decimal) -> None:
        """Update spent amount for a budget."""
        ...


class Budgeteer:
    """Agent for budget management and tracking."""
    
    def __init__(self, budget_service: BudgetService):
        self.budget_service = budget_service
        self.agent_id = "agent.budgeteer"
        self.display_name = "Budgeteer"
        self.pack_id = "pack.finance"
    
    def check_budget(self, budget_id: str, proposed_amount: Decimal) -> dict:
        """
        Check if a proposed expense fits within budget.
        
        Args:
            budget_id: ID of the budget to check
            proposed_amount: Amount of proposed expense
        
        Returns:
            Dictionary with approval status and details
        """
        budget = self.budget_service.get_budget(budget_id)
        allocated = Decimal(budget['allocated'])
        spent = Decimal(budget['spent'])
        remaining = allocated - spent
        
        approved = proposed_amount <= remaining
        
        return {
            'approved': approved,
            'budget_id': budget_id,
            'proposed_amount': str(proposed_amount),
            'remaining': str(remaining),
            'utilization': str((spent / allocated * 100) if allocated > 0 else 0),
            'timestamp': datetime.now().isoformat(),
        }
    
    def allocate_budget(self, name: str, amount: Decimal, period: str) -> dict:
        """
        Allocate a new budget.
        
        Args:
            name: Budget name
            amount: Allocated amount
            period: Budget period (monthly, quarterly, yearly)
        
        Returns:
            Dictionary with budget details
        """
        return {
            'name': name,
            'allocated': str(amount),
            'period': period,
            'created_at': datetime.now().isoformat(),
        }
    
    def generate_report(self, budget_id: str) -> dict:
        """Generate budget utilization report."""
        budget = self.budget_service.get_budget(budget_id)
        allocated = Decimal(budget['allocated'])
        spent = Decimal(budget['spent'])
        
        return {
            'budget_id': budget_id,
            'name': budget['name'],
            'allocated': str(allocated),
            'spent': str(spent),
            'remaining': str(allocated - spent),
            'utilization_pct': str((spent / allocated * 100) if allocated > 0 else 0),
            'period': budget['period'],
            'report_generated': datetime.now().isoformat(),
        }


# CLI interface
if __name__ == "__main__":
    import sys
    
    class MockBudgetService:
        """Mock budget service for testing."""
        
        def get_budget(self, budget_id: str) -> dict:
            return {
                'id': budget_id,
                'name': 'Q1 Operations',
                'allocated': '100000.00',
                'spent': '45000.00',
                'period': 'quarterly',
            }
        
        def update_spent(self, budget_id: str, amount: Decimal) -> None:
            pass
    
    budgeteer = Budgeteer(MockBudgetService())
    
    if len(sys.argv) > 1 and sys.argv[1] == 'check':
        result = budgeteer.check_budget('budget-001', Decimal('5000.00'))
        print(f"Budget check result: {result}")
    elif len(sys.argv) > 1 and sys.argv[1] == 'report':
        report = budgeteer.generate_report('budget-001')
        print(f"Budget report: {report}")
    else:
        print("Usage: python budgeteer.py [check|report]")
