import streamlit as st
import pandas as pd
import plotly.express as px

USD_TO_INR = 83.50


def show_supplier_risk_chart(invoice_df):

    required_columns = ["Vendor Name", "Invoice Amount"]

    for col in required_columns:
        if col not in invoice_df.columns:
            st.warning(f"Column '{col}' not found.")
            return

    df = invoice_df.copy()

    df["Invoice Amount"] = pd.to_numeric(
        df["Invoice Amount"],
        errors="coerce"
    )

    df = df.dropna(subset=["Invoice Amount"])

    # ============================================
    # Currency Selection
    # ============================================

    currency = st.session_state.get("currency", "USD")

    if currency == "INR":
        df["Invoice Amount"] = df["Invoice Amount"] * USD_TO_INR
        symbol = "₹"
    else:
        symbol = "$"

    # ============================================
    # Supplier Spend
    # ============================================

    supplier_df = (
        df.groupby("Vendor Name", as_index=False)["Invoice Amount"]
        .sum()
        .sort_values("Invoice Amount", ascending=False)
        .head(10)
    )

    # ============================================
    # Short Labels
    # ============================================

    supplier_df["Amount Label"] = (
        supplier_df["Invoice Amount"] / 1_000_000
    ).round(2)

    supplier_df["Amount Label"] = (
        symbol
        + supplier_df["Amount Label"].astype(str)
        + "M"
    )

    # ============================================
    # Chart
    # ============================================

    fig = px.bar(
        supplier_df,
        x="Invoice Amount",
        y="Vendor Name",
        orientation="h",
        color="Invoice Amount",
        color_continuous_scale="Blues",
        text="Amount Label"
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
        yaxis_title="Supplier",
        margin=dict(l=10, r=140, t=20, b=20),
        showlegend=False
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )