import streamlit as st
import pandas as pd
from io import BytesIO


def show_export_buttons(filtered_df):

    st.subheader("📤 Export")

    col1, col2 = st.columns(2)

    # ============================
    # CSV Export
    # ============================

    with col1:

        csv = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="📄 Download CSV",
            data=csv,
            file_name="Filtered_Invoices.csv",
            mime="text/csv",
            use_container_width=True
        )

    # ============================
    # Excel Export
    # ============================

    with col2:

        output = BytesIO()

        with pd.ExcelWriter(
            output,
            engine="openpyxl"
        ) as writer:

            filtered_df.to_excel(
                writer,
                index=False,
                sheet_name="Invoices"
            )

        st.download_button(
            label="📊 Download Excel",
            data=output.getvalue(),
            file_name="Filtered_Invoices.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )