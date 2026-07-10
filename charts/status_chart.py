import streamlit as st
import plotly.express as px


@st.cache_data
def prepare_status(df):

    return (
        df.groupby("Matched Status")
        .size()
        .reset_index(name="Count")
    )


def show_status_chart(invoice_df):

    status = prepare_status(invoice_df)


    fig = px.pie(
        status,
        names="Matched Status",
        values="Count",
        hole=0.45
    )

    fig.update_layout(
        height=450,
        legend=dict(
            orientation="h",
            y=-0.15,
            x=0.5,
            xanchor="center"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )