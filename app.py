import streamlit as st
from datetime import datetime

# =====================================================
# IMPORT PAGES
# =====================================================

from pages.dashboard import show_dashboard
from pages.invoices import show_invoices
from pages.analytics import show_analytics
from pages.ai_assistant import show_ai_assistant
from pages.settings import show_settings

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AP Agent Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
<style>

/* Hide Streamlit Sidebar */
[data-testid="stSidebar"]{
    display:none;
}

/* Hide Sidebar Toggle Button */
[data-testid="collapsedControl"]{
    display:none;
}

/* Dashboard Padding */
.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:2rem;
}

/* Reduce blank space */
hr{
    margin-top:0.7rem;
    margin-bottom:0.7rem;
}

</style>
""",
    unsafe_allow_html=True
)

# =====================================================
# HEADER
# =====================================================

left, right = st.columns([5, 1])

with left:

    st.title("📊 AP Agent Dashboard")

    st.caption(
        "AI Powered Accounts Payable Analytics Dashboard"
    )

with right:

    st.markdown("### ")

    st.write(
        datetime.now().strftime("%d %b %Y")
    )

st.divider()

# =====================================================
# TOP NAVIGATION
# =====================================================

page = st.radio(
    label="Navigation",
    options=[
        "🏠 Dashboard",
        "📄 Invoices",
        "📈 Analytics",
        "🤖 AI Assistant",
        "⚙ Settings"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# =====================================================
# ROUTING
# =====================================================

if page == "🏠 Dashboard":

    show_dashboard()

elif page == "📄 Invoices":

    show_invoices()

elif page == "📈 Analytics":

    show_analytics()

elif page == "🤖 AI Assistant":

    show_ai_assistant()

elif page == "⚙ Settings":

    show_settings()