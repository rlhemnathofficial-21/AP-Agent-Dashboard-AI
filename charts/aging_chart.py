import streamlit as st
import plotly.express as px
import pandas as pd


def show_aging_chart(invoice_df):

    if "Invoice Date" not in invoice_df.columns:
        st.warning("Invoice Date column not found.")
        return

    df = invoice_df.copy()

    df["Invoice Date"] = pd.to_datetime(
        df["Invoice Date"],
        errors="coerce"
    )

    df = df.dropna(subset=["Invoice Date"])

    # =====================================================
    # USE LATEST INVOICE DATE AS REFERENCE
    # =====================================================

    reference_date = df["Invoice Date"].max()

    df["Age"] = (
        reference_date -
        df["Invoice Date"]
    ).dt.days

    bins = [-1, 30, 60, 90, 120, 10000]

    labels = [
        "0–30 Days",
        "31–60 Days",
        "61–90 Days",
        "91–120 Days",
        "120+ Days"
    ]

    df["Aging Bucket"] = pd.cut(
        df["Age"],
        bins=bins,
        labels=labels
    )

    aging = (
        df.groupby("Aging Bucket", observed=False)
        .size()
        .reset_index(name="Invoices")
    )

    fig = px.bar(
        aging,
        x="Aging Bucket",
        y="Invoices",
        text="Invoices",
        color="Invoices"
    )

    fig.update_layout(
        height=380,
        xaxis_title="Invoice Age",
        yaxis_title="Number of Invoices",
        showlegend=False
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )