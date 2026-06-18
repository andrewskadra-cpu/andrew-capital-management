import streamlit as st
import pandas as pd
import os

st.title("Andrew Capital Management")
st.subheader("Trading Journal v2")

FILE_NAME = "trades.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=[
        "Ticker",
        "Entry",
        "Exit",
        "Shares",
        "Profit"
    ])
    df.to_csv(FILE_NAME, index=False)

# Inputs
ticker = st.text_input("Ticker")

entry = st.number_input("Entry Price", min_value=0.0)

exit_price = st.number_input("Exit Price", min_value=0.0)

shares = st.number_input(
    "Number of Shares",
    min_value=1,
    value=1
)

# Save Trade
if st.button("Save Trade"):

    profit = (exit_price - entry) * shares

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

    updated.to_csv(FILE_NAME, index=False)

    st.success("Trade Saved!")

# Display Trades
trades = pd.read_csv(FILE_NAME)

st.header("Performance Dashboard")

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
        "Avg Profit",
        f"${average_profit:.2f}"
    )

st.header("Trade History")

st.dataframe(trades)