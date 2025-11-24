"""Finance pack Growth Catalyst agent for budgeting and burn tracking."""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Protocol, Dict, Any


class CostExplorerClient(Protocol):
    def get_cost_and_usage(self, **kwargs: Any) -> Dict[str, Any]:
        """Protocol for AWS Cost Explorer client."""


class Reporter(Protocol):
    def post(self, channel: str, message: str) -> None:
        """Protocol for posting messages to chat destinations."""


def _default_time_range(days_elapsed: int) -> Dict[str, str]:
    today = date.today()
    start = today - timedelta(days=days_elapsed)
    return {"Start": start.isoformat(), "End": today.isoformat()}


@dataclass
class BudgetForecast:
    current_spend: float
    burn_rate: float
    forecast_monthly: float
    percent_of_budget: float


class Budgeteer:
    """Forecasts burn rate and prepares weekly spending reports."""

    def __init__(self, budget_limit: float, slack_channel: str = "#finops") -> None:
        self.budget_limit = budget_limit
        self.slack_channel = slack_channel

    def get_month_to_date_spend(
        self,
        client: CostExplorerClient,
        days_elapsed: int,
        time_range: Dict[str, str] | None = None,
    ) -> float:
        """Fetch month-to-date spend from a Cost Explorer compatible client."""

        window = time_range or _default_time_range(days_elapsed)
        response = client.get_cost_and_usage(
            TimePeriod=window,
            Granularity="MONTHLY",
            Metrics=["UnblendedCost"],
        )
        total = response.get("ResultsByTime", [{}])[0].get("Total", {})
        amount = total.get("UnblendedCost", {}).get("Amount", "0")
        try:
            return float(amount)
        except (TypeError, ValueError):
            return 0.0

    def forecast(self, current_spend: float, days_elapsed: int, days_in_month: int) -> BudgetForecast:
        if days_elapsed <= 0 or days_in_month <= 0:
            raise ValueError("days_elapsed and days_in_month must be positive")

        burn_rate = current_spend / days_elapsed
        forecast_monthly = burn_rate * days_in_month
        percent_of_budget = (forecast_monthly / self.budget_limit) * 100 if self.budget_limit else 0.0
        return BudgetForecast(
            current_spend=current_spend,
            burn_rate=burn_rate,
            forecast_monthly=forecast_monthly,
            percent_of_budget=percent_of_budget,
        )

    def build_weekly_report(
        self,
        client: CostExplorerClient,
        days_elapsed: int,
        days_in_month: int,
        reporter: Reporter | None = None,
    ) -> str:
        current_spend = self.get_month_to_date_spend(client, days_elapsed)
        forecast = self.forecast(current_spend, days_elapsed, days_in_month)

        report = (
            f"[finance-budgeteer] Week closeout — MTD spend: ${forecast.current_spend:,.2f}\n"
            f"Daily burn: ${forecast.burn_rate:,.2f}\n"
            f"Projected month-end: ${forecast.forecast_monthly:,.2f} ({forecast.percent_of_budget:,.1f}% of budget)"
        )

        if reporter:
            reporter.post(self.slack_channel, report)
        return report


__all__ = ["Budgeteer", "BudgetForecast", "CostExplorerClient", "Reporter"]
