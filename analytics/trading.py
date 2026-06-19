"""Trading analytics facade.

New trading analytics should be added here or migrated here from utils.runtime
as the codebase grows.
"""

from utils.runtime import (
    a_plus_setup_analysis,
    advanced_trade_metrics,
    day_of_week_analysis,
    drawdown_statistics,
    grade_performance,
    grouped_trade_analysis,
    mistake_analysis,
    monthly_performance_calendar,
    render_a_plus_setup_analysis,
    render_equity_curve_dashboard,
    render_monthly_performance_calendar,
    render_risk_of_ruin_calculator,
    render_trading_monte_carlo,
    risk_of_ruin_probability,
    run_trading_monte_carlo,
    setup_performance,
    summarize_trades,
    trading_equity_curves,
)

__all__ = [
    "a_plus_setup_analysis",
    "advanced_trade_metrics",
    "day_of_week_analysis",
    "drawdown_statistics",
    "grade_performance",
    "grouped_trade_analysis",
    "mistake_analysis",
    "monthly_performance_calendar",
    "render_a_plus_setup_analysis",
    "render_equity_curve_dashboard",
    "render_monthly_performance_calendar",
    "render_risk_of_ruin_calculator",
    "render_trading_monte_carlo",
    "risk_of_ruin_probability",
    "run_trading_monte_carlo",
    "setup_performance",
    "summarize_trades",
    "trading_equity_curves",
]
