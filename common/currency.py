import streamlit as st

USD_TO_INR = 83.50


def get_currency():
    return st.session_state.get("currency", "USD")


def get_symbol():
    return "₹" if get_currency() == "INR" else "$"


def convert_amount(amount):
    if get_currency() == "INR":
        return amount * USD_TO_INR
    return amount


def format_currency(amount):
    amount = convert_amount(amount)
    return f"{get_symbol()}{amount:,.2f}"