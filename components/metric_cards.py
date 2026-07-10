import streamlit as st
from common.currency import format_currency


def show_metrics(filtered_df, match_df=None):

    # ==========================================
    # KPI VALUES
    # ==========================================

    total_invoices = len(filtered_df)

    matched = 0
    if "Matched Status" in filtered_df.columns:
        matched = (
            filtered_df["Matched Status"]
            .astype(str)
            .str.lower()
            .eq("matched")
            .sum()
        )

    pending = total_invoices - matched
    exceptions = pending

    duplicates = 0
    if "Invoice No" in filtered_df.columns:
        duplicates = filtered_df["Invoice No"].duplicated().sum()

    total_value = 0
    if "Invoice Amount" in filtered_df.columns:
        total_value = filtered_df["Invoice Amount"].sum()

    # ==========================================
    # CARD STYLE
    # ==========================================

    st.markdown(
        """
        <style>

        .kpi-card{
            background:#1f2937;
            border:1px solid #374151;
            border-radius:16px;
            padding:20px;
            text-align:center;
            min-height:165px;
            transition:0.25s;
        }

        .kpi-card:hover{
            transform:translateY(-5px);
            border:1px solid #3b82f6;
            box-shadow:0 8px 20px rgba(59,130,246,.25);
        }

        .kpi-icon{
            font-size:36px;
            margin-bottom:10px;
        }

        .kpi-title{
            color:#cbd5e1;
            font-size:16px;
            margin-bottom:10px;
        }

        .kpi-value{
            color:white;
            font-size:32px;
            font-weight:bold;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # ==========================================
    # CARD DATA
    # ==========================================

    cards = [

        ("📄", "Total Invoices", f"{total_invoices:,}"),

        ("✅", "Matched", f"{matched:,}"),

        ("⏳", "Pending", f"{pending:,}"),

        ("⚠️", "Exceptions", f"{exceptions:,}"),

        ("🔁", "Duplicates", f"{duplicates:,}"),

        ("💰", "Total Value", format_currency(total_value)),

    ]

    cols = st.columns(6)

    for col, (icon, title, value) in zip(cols, cards):

        with col:

            html = f"""
            <div class="kpi-card">
                <div class="kpi-icon">{icon}</div>
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """

            st.markdown(
                html,
                unsafe_allow_html=True,
            )