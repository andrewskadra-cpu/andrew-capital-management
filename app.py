"""ACMOS Streamlit entrypoint.

This file intentionally contains only page initialization, navigation, and routing.
Business logic, analytics, persistence, reports, and page renderers live in the
package folders so ACMOS can continue growing without turning app.py into a
monolith again.
"""

from __future__ import annotations

import streamlit as st

from pages.acquisitions import render_acquisition_analyzer
from pages.ai_cio import render_ai_chief_investment_officer
from pages.dashboard import render_dashboard
from pages.executive_decision import render_executive_decision_engine
from pages.executive_reporting import render_executive_reporting_center
from pages.real_estate import render_real_estate_analyzer
from pages.trading import render_trading_center
from pages.universal_scoring import render_universal_scoring_engine
from pages.wealth import render_wealth_dashboard
from utils.runtime import APP_NAME, configure_page, initialize_files


PAGES = {
    "Dashboard": render_dashboard,
    "Trading": render_trading_center,
    "Wealth": render_wealth_dashboard,
    "Real Estate": render_real_estate_analyzer,
    "Acquisitions": render_acquisition_analyzer,
    "AI Chief Investment Officer": render_ai_chief_investment_officer,
    "Universal Scoring Engine": render_universal_scoring_engine,
    "Executive Decision Engine": render_executive_decision_engine,
    "Executive Reporting Center": render_executive_reporting_center,
}


def render_sidebar() -> str:
    """Render the global ACMOS navigation and return the selected page name."""
    st.sidebar.title(APP_NAME)
    return st.sidebar.selectbox("Navigation", list(PAGES.keys()))


def main() -> None:
    """Initialize ACMOS and route the selected page."""
    configure_page()
    initialize_files()
    selected_page = render_sidebar()
    PAGES[selected_page]()


if __name__ == "__main__":
    main()
