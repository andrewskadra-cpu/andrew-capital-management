import streamlit as st
import pandas as pd
import os

# ==========================================
# APP CONFIG
# ==========================================

st.set_page_config(
    page_title="Andrew Capital Management",
    layout="wide"
)

FILE_NAME = "trades.csv"

# ==========================================
# CREATE FILE IF NEEDED
# ==========================================

if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=[
        "Ticker",
        "Entry",
        "Exit",
        "Shares",
        "Profit"
    ])
    df.to_csv(FILE_NAME, index=False)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("Andrew Capital Management")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Trading",
        "Wealth",
        "Real Estate",
        "Acquisitions"
    ]
)

# ==========================================
# DASHBOARD PAGE
# ==========================================

if page == "Dashboard":

    st.title("Executive Dashboard")

    trades = pd.read_csv(FILE_NAME)

    if len(trades) > 0:

        total_trades = len(trades)

        total_profit = trades["Profit"].sum()

        winning_trades = len(
            trades[trades["Profit"] > 0]
        )

        win_rate = (
            winning_trades /
            total_trades
        ) * 100

        average_profit = (
            trades["Profit"].mean()
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Trades",
            total_trades
        )

        col2.metric(
            "Total Profit",
            f"${total_profit:.2f}"
        )

        col3.metric(
            "Win Rate",
            f"{win_rate:.1f}%"
        )

        col4.metric(
            "Average Profit",
            f"${average_profit:.2f}"
        )

    st.divider()

    st.subheader("Long-Term Vision")

    col1, col2, col3 = st.columns(3)

    col1.info("📈 Trading")
    col2.info("🏠 Real Estate")
    col3.info("🏢 Acquisitions")

# ==========================================
# TRADING PAGE
# ==========================================

if page == "Trading":

    st.title("Trading Journal")

    ticker = st.text_input("Ticker")

    entry = st.number_input(
        "Entry Price",
        min_value=0.0
    )

    exit_price = st.number_input(
        "Exit Price",
        min_value=0.0
    )

    shares = st.number_input(
        "Number of Shares",
        min_value=1,
        value=1
    )

    if st.button("Save Trade"):

        profit = (
            exit_price - entry
        ) * shares

        new_trade = pd.DataFrame([{
            "Ticker": ticker,
            "Entry": entry,
            "Exit": exit_price,
            "Shares": shares,
            "Profit": profit
        }])

        existing = pd.read_csv(FILE_NAME)

        updated = pd.concat(
            [existing, new_trade],
            ignore_index=True
        )

        updated.to_csv(
            FILE_NAME,
            index=False
        )

        st.success("Trade Saved!")

    trades = pd.read_csv(FILE_NAME)

    st.subheader("Trade History")

    st.dataframe(
        trades,
        use_container_width=True
    )

# ==========================================
# WEALTH PAGE
# ==========================================

if page == "Wealth":

    st.title("Wealth Dashboard")

    st.info(
        "Coming Soon: Net Worth Tracking"
    )

# ==========================================
# REAL ESTATE PAGE
# ==========================================

if page == "Real Estate":

    st.title("Real Estate Analyzer")

    st.info(
        "Coming Soon: Rental Property Analysis"
    )

# ==========================================
# ACQUISITIONS PAGE
# ==========================================

if page == "Acquisitions":

    st.title("Business Acquisition Analyzer")

    st.info(
        "Coming Soon: Business Valuation Tools"
    )