import streamlit as st
import plotly.express as px


def show_category_chart(invoice_df):

    if "Category" not in invoice_df.columns:
        st.warning("Category column not found.")
        return

    category_df = (
        invoice_df.groupby("Category")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        category_df,
        names="Category",
        values="Count",
        hole=0.45,
        title="Invoices by Category"
    )

    fig.update_layout(
        legend=dict(
            orientation="h",
            y=-0.15,
            x=0.5,
            xanchor="center"
        )
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )