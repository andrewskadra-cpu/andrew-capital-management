"""CSV persistence facade.

All existing storage remains CSV-backed for backward compatibility. Future
database adapters can implement the same read/save surface here.
"""

from utils.runtime import (
    initialize_files,
    read_acquisition_deals,
    read_acquisition_tasks,
    read_liabilities,
    read_net_worth_snapshots,
    read_playbook,
    read_real_estate_properties,
    read_trades,
    read_watchlist,
    read_wealth_accounts,
    save_acquisition_deals,
    save_acquisition_tasks,
    save_liabilities,
    save_net_worth_snapshots,
    save_playbook,
    save_real_estate_properties,
    save_trades,
    save_watchlist,
    save_wealth_accounts,
)

__all__ = [
    "initialize_files",
    "read_acquisition_deals",
    "read_acquisition_tasks",
    "read_liabilities",
    "read_net_worth_snapshots",
    "read_playbook",
    "read_real_estate_properties",
    "read_trades",
    "read_watchlist",
    "read_wealth_accounts",
    "save_acquisition_deals",
    "save_acquisition_tasks",
    "save_liabilities",
    "save_net_worth_snapshots",
    "save_playbook",
    "save_real_estate_properties",
    "save_trades",
    "save_watchlist",
    "save_wealth_accounts",
]
