import streamlit as st
import plotly.express as px

from data.load_data import load_workflow


def show_workflow_chart():

    df = load_workflow()

    # Possible workflow status column names
    possible_columns = [
        "Workflow Status",
        "Status",
        "WorkflowStatus",
        "Current Status",
        "Current Stage",
        "Workflow Stage",
        "Stage",
        "Approval Status"
    ]

    status_column = None

    for col in possible_columns:
        if col in df.columns:
            status_column = col
            break

    if status_column is None:
        st.error("Workflow status column not found.")
        st.write("Available columns:")
        st.write(df.columns.tolist())
        return

    workflow_status = (
        df.groupby(status_column)
        .size()
        .reset_index(name="Count")
    )

    st.subheader("🔄 Workflow Status")

    fig = px.bar(
        workflow_status,
        x=status_column,
        y="Count",
        text="Count",
        title="Workflow Status Distribution"
    )

    fig.update_layout(
        height=450,
        xaxis_title=status_column,
        yaxis_title="Count"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )