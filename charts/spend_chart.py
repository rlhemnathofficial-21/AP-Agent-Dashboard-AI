import streamlit as st
import pandas as pd
import plotly.express as px

from common.currency import (
    convert_amount,
    get_symbol
)


def show_spend_chart(invoice_df):

    # =====================================================
    # CHECK REQUIRED COLUMNS
    # =====================================================

    if "Invoice Date" not in invoice_df.columns:
        st.warning("Invoice Date column not found.")
        return

    if "Invoice Amount" not in invoice_df.columns:
        st.warning("Invoice Amount column not found.")
        return

    # =====================================================
    # PREPARE DATA
    # =====================================================

    df = invoice_df.copy()

    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"],
        errors="coerce"
    )

    df = df.dropna(subset=["Invoice Date"])

    df["Invoice Amount"] = pd.to_numeric(
        df["Invoice Amount"],
        errors="coerce"
    )

    # Currency Conversion
    df["Invoice Amount"] = df["Invoice Amount"].apply(convert_amount)

    # Month
    df["Month"] = df["Invoice Date"].dt.strftime("%b")

    monthly = (
        df.groupby("Month")["Invoice Amount"]
        .sum()
        .reset_index()
    )

    month_order = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]

    monthly["Month"] = pd.Categorical(
        monthly["Month"],
        categories=month_order,
        ordered=True
    )

    monthly = monthly.sort_values("Month")

    symbol = get_symbol()

    # =====================================================
    # CHART
    # =====================================================

    fig = px.line(
        monthly,
        x="Month",
        y="Invoice Amount",
        markers=True
    )

    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>"
            + f"Amount: {symbol}"
            + "%{y:,.2f}<extra></extra>"
        )
    )

    fig.update_layout(

        height=st.session_state.get("chart_height", 380),

        xaxis_title="Month",

        yaxis_title=f"Invoice Amount ({symbol})",

        margin=dict(
            l=10,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )