import streamlit as st

from data.load_data import load_invoice_master
from common.currency import format_currency


def show_invoices():

    st.title("📄 Invoice Management")
    st.caption("Search, filter and export invoices")

    st.divider()

    df = load_invoice_master().copy()

    filtered_df = df.copy()

    # ==========================================
    # SEARCH
    # ==========================================

    c1, c2, c3 = st.columns([2, 2, 1])

    with c1:
        search = st.text_input(
            "🔍 Search Invoice",
            placeholder="Invoice Number..."
        )

    with c2:

        vendors = ["All"] + sorted(
            df["Vendor Name"].dropna().unique().tolist()
        )

        vendor = st.selectbox(
            "🏢 Vendor",
            vendors
        )

    with c3:

        rows = st.selectbox(
            "Rows",
            [10, 25, 50, 100],
            index=1
        )

    # ==========================================
    # FILTERS
    # ==========================================

    if search:

        filtered_df = filtered_df[
            filtered_df["Invoice No"]
            .astype(str)
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

    if vendor != "All":

        filtered_df = filtered_df[
            filtered_df["Vendor Name"] == vendor
        ]

    if "Category" in filtered_df.columns:

        category = st.selectbox(

            "📂 Category",

            ["All"] +
            sorted(
                filtered_df["Category"]
                .dropna()
                .unique()
                .tolist()
            )

        )

        if category != "All":

            filtered_df = filtered_df[
                filtered_df["Category"] == category
            ]

    st.divider()

    # ==========================================
    # SUMMARY
    # ==========================================

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Invoices",
        len(filtered_df)
    )

    col2.metric(
        "Suppliers",
        filtered_df["Vendor Name"].nunique()
    )

    col3.metric(
        "Invoice Value",
        format_currency(
            filtered_df["Invoice Amount"].sum()
        )
    )

    st.divider()

    # ==========================================
    # EXPORT
    # ==========================================

    csv = filtered_df.to_csv(index=False)

    st.download_button(
        "⬇ Download CSV",
        csv,
        file_name="Invoices.csv",
        mime="text/csv"
    )

    st.divider()

    # ==========================================
    # TABLE
    # ==========================================

    display_df = filtered_df.copy()

    display_df["Invoice Amount"] = display_df["Invoice Amount"].apply(
        format_currency
    )

    st.caption(
        f"Showing {min(rows, len(display_df))} of {len(display_df)} invoices"
    )

    st.dataframe(
        display_df.head(rows),
        width="stretch",
        hide_index=True
    )