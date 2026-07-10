import streamlit as st
import pandas as pd


def show_invoice_table():

    data = {

        "Invoice No": [
            "INV-2026-001",
            "INV-2026-002",
            "INV-2026-003",
            "INV-2026-004",
            "INV-2026-005"
        ],

        "Vendor": [
            "ABC Office Supplies",
            "Dell Technologies",
            "HP India",
            "Lenovo",
            "Canon India"
        ],

        "Invoice Date": [
            "07-Jul-2026",
            "08-Jul-2026",
            "08-Jul-2026",
            "09-Jul-2026",
            "10-Jul-2026"
        ],

        "Amount": [
            12508,
            85000,
            42000,
            67000,
            15500
        ],

        "GST": [
            1908,
            12966,
            6406,
            10220,
            2364
        ],

        "Status": [
            "Approved",
            "Pending",
            "Approved",
            "Rejected",
            "Pending"
        ]

    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )