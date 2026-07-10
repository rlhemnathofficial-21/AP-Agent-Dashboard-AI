import streamlit as st
from datetime import datetime


def show_header():
    """
    Displays the dashboard header.
    """

    today = datetime.now().strftime("%d %B %Y")

    col1, col2 = st.columns([4, 1])

    with col1:
        st.title("📊 AP Agent Dashboard")
        st.caption("AI Powered Accounts Payable Analytics Dashboard")

    with col2:
        st.metric(
            label="📅 Today",
            value=today
        )

    st.divider()