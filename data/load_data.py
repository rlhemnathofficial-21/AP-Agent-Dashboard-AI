import pandas as pd
import streamlit as st

FILE_PATH = "data/AP Agent Sample Dataset copy.xlsx"


@st.cache_data
def load_invoice_master():
    return pd.read_excel(
        FILE_PATH,
        sheet_name="Invoice_Master"
    )


@st.cache_data
def load_workflow():
    return pd.read_excel(
        FILE_PATH,
        sheet_name="Workflow_Transactions"
    )


@st.cache_data
def load_match_scores():
    return pd.read_excel(
        FILE_PATH,
        sheet_name="Match_Scoring"
    )