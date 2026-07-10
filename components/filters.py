import streamlit as st
import pandas as pd


def show_filters(invoice_df):

    st.subheader("🔍 Dashboard Filters")

    col1, col2, col3 = st.columns(3)

    # ----------------------------------------
    # Search Invoice
    # ----------------------------------------

    with col1:
        search = st.text_input(
            "Invoice Number",
            placeholder="Search..."
        )

    # ----------------------------------------
    # Vendor
    # ----------------------------------------

    with col2:
        vendors = ["All Vendors"] + sorted(
            invoice_df["Vendor Name"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        vendor = st.selectbox(
            "Vendor",
            vendors
        )

    # ----------------------------------------
    # Match Status
    # ----------------------------------------

    with col3:
        status = ["All"] + sorted(
            invoice_df["Matched Status"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        match_status = st.selectbox(
            "Match Status",
            status
        )

    st.markdown("")

    col4, col5, col6 = st.columns(3)

    # ----------------------------------------
    # Buyer
    # ----------------------------------------

    with col4:

        if "Buyer Name" in invoice_df.columns:

            buyers = ["All Buyers"] + sorted(
                invoice_df["Buyer Name"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            buyer = st.selectbox(
                "Buyer",
                buyers
            )

        else:
            buyer = "All Buyers"

    # ----------------------------------------
    # Category
    # ----------------------------------------

    with col5:

        if "Category" in invoice_df.columns:

            categories = ["All Categories"] + sorted(
                invoice_df["Category"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )

            category = st.selectbox(
                "Category",
                categories
            )

        else:
            category = "All Categories"

    # ----------------------------------------
    # Date Range
    # ----------------------------------------

    with col6:

        if "Invoice Date" in invoice_df.columns:

            invoice_df["Invoice Date"] = pd.to_datetime(
                invoice_df["Invoice Date"],
                errors="coerce"
            )

            start = invoice_df["Invoice Date"].min()
            end = invoice_df["Invoice Date"].max()

            dates = st.date_input(
                "Invoice Date",
                value=(start, end)
            )

        else:
            dates = None

    # ----------------------------------------
    # Apply Filters
    # ----------------------------------------

    filtered = invoice_df.copy()

    if search:

        filtered = filtered[
            filtered["Invoice No"]
            .astype(str)
            .str.contains(search, case=False, na=False)
        ]

    if vendor != "All Vendors":

        filtered = filtered[
            filtered["Vendor Name"] == vendor
        ]

    if match_status != "All":

        filtered = filtered[
            filtered["Matched Status"] == match_status
        ]

    if buyer != "All Buyers":

        filtered = filtered[
            filtered["Buyer Name"] == buyer
        ]

    if category != "All Categories":

        filtered = filtered[
            filtered["Category"] == category
        ]

    if dates and len(dates) == 2:

        filtered = filtered[
            (filtered["Invoice Date"] >= pd.Timestamp(dates[0])) &
            (filtered["Invoice Date"] <= pd.Timestamp(dates[1]))
        ]

    return filtered