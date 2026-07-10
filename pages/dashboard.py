import streamlit as st

from data.load_data import (
    load_invoice_master,
    load_workflow,
    load_match_scores
)

from components.filters import show_filters
from components.export_buttons import show_export_buttons
from components.metric_cards import show_metrics

from charts.spend_chart import show_spend_chart
from charts.vendor_chart import show_vendor_chart
from charts.status_chart import show_status_chart
from charts.category_chart import show_category_chart
from charts.aging_chart import show_aging_chart
from charts.supplier_risk_chart import show_supplier_risk_chart


def show_dashboard():

    # =====================================================
    # LOAD DATA
    # =====================================================

    invoice_df = load_invoice_master()
    workflow_df = load_workflow()
    match_df = load_match_scores()

    # =====================================================
    # FILTERS
    # =====================================================

    filtered_df = show_filters(invoice_df)

    # =====================================================
    # EXPORT BUTTONS
    # =====================================================

    show_export_buttons(filtered_df)

    st.divider()

    # =====================================================
    # KPI CARDS
    # =====================================================

    show_metrics(filtered_df, match_df)

    st.divider()

    # =====================================================
    # ANALYTICS
    # =====================================================

    st.markdown("## 📊 Invoice Analytics")

    # ================= ROW 1 =================

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("📈 Monthly Invoice Spend")
            st.caption("Monthly trend of total invoice amount")
            show_spend_chart(filtered_df)

    with col2:
        with st.container(border=True):
            st.subheader("🥧 Match Status")
            st.caption("Distribution of invoice matching status")
            show_status_chart(filtered_df)

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= ROW 2 =================

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.subheader("🏢 Top Suppliers")
            st.caption("Top suppliers ranked by invoice value")
            show_vendor_chart(filtered_df)

    with col4:
        with st.container(border=True):
            st.subheader("📂 Category-wise Invoice Distribution")
            st.caption("Invoice count by category")
            show_category_chart(filtered_df)

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= ROW 3 =================

    col5, col6 = st.columns(2)

    with col5:
        with st.container(border=True):
            st.subheader("📅 Invoice Aging Analysis")
            st.caption("Outstanding invoices grouped by age")
            show_aging_chart(filtered_df)

    with col6:
        with st.container(border=True):
            st.subheader("🏢 Top Supplier Spend")
            st.caption("Top suppliers ranked by total invoice value")
            show_supplier_risk_chart(filtered_df)

    st.divider()

    # =====================================================
    # INVOICE MASTER
    # =====================================================

    st.header("📄 Invoice Master")

    st.caption(f"Showing {len(filtered_df):,} invoices")

    st.dataframe(
        filtered_df,
        width="stretch",
        hide_index=True
    )

    st.divider()

    # =====================================================
    # WORKFLOW TRANSACTIONS
    # =====================================================

    st.header("🔄 Workflow Transactions")

    st.dataframe(
        workflow_df,
        width="stretch",
        hide_index=True
    )

    st.divider()

    # =====================================================
    # MATCH SCORING
    # =====================================================

    st.header("🎯 Match Scoring")

    st.dataframe(
        match_df,
        width="stretch",
        hide_index=True
    )