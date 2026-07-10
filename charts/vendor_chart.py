import streamlit as st
import pandas as pd
import plotly.express as px

from common.currency import (
    convert_amount,
    get_symbol
)


def show_vendor_chart(invoice_df):

    # =====================================================
    # CHECK REQUIRED COLUMNS
    # =====================================================

    if "Vendor Name" not in invoice_df.columns:
        st.warning("Vendor Name column not found.")
        return

    if "Invoice Amount" not in invoice_df.columns:
        st.warning("Invoice Amount column not found.")
        return

    # =====================================================
    # PREPARE DATA
    # =====================================================

    df = invoice_df.copy()

    df["Invoice Amount"] = pd.to_numeric(
        df["Invoice Amount"],
        errors="coerce"
    )

    df = df.dropna(subset=["Invoice Amount"])

    # Currency conversion
    df["Invoice Amount"] = df["Invoice Amount"].apply(convert_amount)

    vendor_df = (
        df.groupby("Vendor Name", as_index=False)["Invoice Amount"]
        .sum()
        .sort_values("Invoice Amount", ascending=False)
        .head(10)
    )

    symbol = get_symbol()

    # Short labels (K / M)

    def short_label(value):

        if value >= 1_000_000:
            return f"{symbol}{value/1_000_000:.2f}M"

        elif value >= 1_000:
            return f"{symbol}{value/1_000:.2f}K"

        return f"{symbol}{value:.0f}"

    vendor_df["Label"] = vendor_df["Invoice Amount"].apply(short_label)

    # =====================================================
    # CHART
    # =====================================================

    fig = px.bar(
        vendor_df,
        x="Invoice Amount",
        y="Vendor Name",
        orientation="h",
        text="Label",
        color="Invoice Amount",
        color_continuous_scale="Blues"
    )

    fig.update_yaxes(autorange="reversed")

    fig.update_traces(
        textposition="outside",
        cliponaxis=False,
        hovertemplate=(
            "<b>%{y}</b><br>"
            + f"Invoice Amount: {symbol}"
            + "%{x:,.2f}<extra></extra>"
        )
    )

    fig.update_layout(
        height=st.session_state.get("chart_height", 380),
        xaxis_title=f"Invoice Amount ({symbol})",
        yaxis_title="Vendor",
        margin=dict(l=10, r=120, t=20, b=20),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )