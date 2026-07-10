import streamlit as st


def show_settings():

    st.title("⚙ Dashboard Settings")
    st.caption("Customize your AP Agent Dashboard")

    st.divider()

    # =====================================================
    # DEFAULT SETTINGS
    # =====================================================

    if "theme" not in st.session_state:
        st.session_state.theme = "Dark"

    if "currency" not in st.session_state:
        st.session_state.currency = "USD"

    if "rows_per_table" not in st.session_state:
        st.session_state.rows_per_table = 25

    if "chart_height" not in st.session_state:
        st.session_state.chart_height = 400

    # =====================================================
    # APPEARANCE
    # =====================================================

    st.subheader("Appearance")

    theme = st.selectbox(
        "Theme",
        ["Dark", "Light"],
        index=0 if st.session_state.theme == "Dark" else 1
    )

    currency = st.selectbox(
        "Currency",
        ["USD", "INR"],
        index=0 if st.session_state.currency == "USD" else 1
    )

    rows = st.selectbox(
        "Rows per Table",
        [10, 25, 50, 100],
        index=[10,25,50,100].index(st.session_state.rows_per_table)
    )

    chart_height = st.slider(
        "Chart Height",
        300,
        600,
        value=st.session_state.chart_height
    )

    # =====================================================
    # SAVE SETTINGS
    # =====================================================

    st.session_state.theme = theme
    st.session_state.currency = currency
    st.session_state.rows_per_table = rows
    st.session_state.chart_height = chart_height

    st.divider()

    st.subheader("About")

    st.info(
        """
**AP Agent Dashboard**

Version 1.0

Built with:

• Streamlit

• Plotly

• Pandas

• Python
"""
    )

    st.success("✅ Settings saved successfully.")