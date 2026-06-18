# ==========================================
# TRADING PAGE
# ==========================================

if page == "Trading":

    st.title("Trading Center")

    trades = pd.read_csv(FILE_NAME)

    tab1, tab2, tab3 = st.tabs(
        [
            "Trade Entry",
            "Analytics",
            "History"
        ]
    )

    # ======================================
    # TRADE ENTRY
    # ======================================

    with tab1:

        st.subheader("New Trade")

        trade_date = st.date_input(
            "Trade Date"
        )

        ticker = st.text_input(
            "Ticker"
        )

        direction = st.selectbox(
            "Direction",
            [
                "Long",
                "Short"
            ]
        )

        setup = st.selectbox(
            "Setup Type",
            [
                "Breakout",
                "Pullback",
                "Support Bounce",
                "Trend Continuation",
                "Other"
            ]
        )

        entry = st.number_input(
            "Entry Price",
            min_value=0.0
        )

        stop_loss = st.number_input(
            "Stop Loss",
            min_value=0.0
        )

        target = st.number_input(
            "Target Price",
            min_value=0.0
        )

        exit_price = st.number_input(
            "Exit Price",
            min_value=0.0
        )

        shares = st.number_input(
            "Shares",
            min_value=1,
            value=1
        )

        notes = st.text_area(
            "Trade Notes"
        )

        risk = abs(entry - stop_loss)

        reward = abs(target - entry)

        rr_ratio = 0

        if risk > 0:
            rr_ratio = reward / risk

        st.info(
            f"Risk / Reward Ratio: {rr_ratio:.2f}"
        )

        if st.button("Save Trade"):

            profit = (
                exit_price - entry
            ) * shares

            new_trade = pd.DataFrame([{
                "Date": str(trade_date),
                "Ticker": ticker,
                "Direction": direction,
                "Setup": setup,
                "Entry": entry,
                "Stop": stop_loss,
                "Target": target,
                "Exit": exit_price,
                "Shares": shares,
                "Profit": profit,
                "RR": rr_ratio,
                "Notes": notes
            }])

            if len(trades) > 0:

                updated = pd.concat(
                    [trades, new_trade],
                    ignore_index=True
                )

            else:

                updated = new_trade

            updated.to_csv(
                FILE_NAME,
                index=False
            )

            st.success(
                "Trade Saved!"
            )

    # ======================================
    # ANALYTICS
    # ======================================

    with tab2:

        st.subheader("Trading Analytics")

        if len(trades) > 0:

            total_trades = len(trades)

            total_profit = trades[
                "Profit"
            ].sum()

            winning_trades = len(
                trades[
                    trades["Profit"] > 0
                ]
            )

            win_rate = (
                winning_trades /
                total_trades
            ) * 100

            average_profit = trades[
                "Profit"
            ].mean()

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Trades",
                total_trades
            )

            col2.metric(
                "Profit",
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

    # ======================================
    # HISTORY
    # ======================================

    with tab3:

        st.subheader("Trade History")

        st.dataframe(
            trades,
            use_container_width=True
        )