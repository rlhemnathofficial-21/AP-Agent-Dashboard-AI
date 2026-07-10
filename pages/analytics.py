import streamlit as st

from data.load_data import load_invoice_master

from charts.spend_chart import show_spend_chart
from charts.vendor_chart import show_vendor_chart
from charts.status_chart import show_status_chart
from charts.category_chart import show_category_chart
from charts.aging_chart import show_aging_chart
from charts.supplier_risk_chart import show_supplier_risk_chart

from common.currency import format_currency


def show_analytics():

    st.title("📈 Analytics")
    st.caption("Detailed Accounts Payable Analytics")

    st.divider()

    # ==========================================
    # LOAD DATA
    # ==========================================

    invoice_df = load_invoice_master().copy()

    # DO NOT convert currency here

    # ==========================================
    # SUMMARY
    # ==========================================

    total_value = invoice_df["Invoice Amount"].sum()

    avg_invoice = invoice_df["Invoice Amount"].mean()

    vendors = invoice_df["Vendor Name"].nunique()

    avg_match = 0

    if "Match Score" in invoice_df.columns:
        avg_match = invoice_df["Match Score"].mean()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "💰 Total Value",
            format_currency(total_value)
        )

    with c2:
        st.metric(
            "📄 Avg Invoice",
            format_currency(avg_invoice)
        )

    with c3:
        st.metric(
            "🏢 Vendors",
            vendors
        )

    with c4:
        st.metric(
            "⭐ Avg Match",
            f"{avg_match:.2f}"
        )

    st.divider()

    # ==========================================
    # ROW 1
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("📈 Monthly Invoice Spend")
            show_spend_chart(invoice_df)

    with col2:
        with st.container(border=True):
            st.subheader("🥧 Match Status")
            show_status_chart(invoice_df)

    st.write("")

    # ==========================================
    # ROW 2
    # ==========================================

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.subheader("🏢 Top Suppliers")
            show_vendor_chart(invoice_df)

    with col4:
        with st.container(border=True):
            st.subheader("📂 Category Distribution")
            show_category_chart(invoice_df)

    st.write("")

    # ==========================================
    # ROW 3
    # ==========================================

    col5, col6 = st.columns(2)

    with col5:
        with st.container(border=True):
            st.subheader("📅 Invoice Aging")
            show_aging_chart(invoice_df)

    with col6:
        with st.container(border=True):
            st.subheader("🏢 Top Supplier Spend")
            show_supplier_risk_chart(invoice_df)