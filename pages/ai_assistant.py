import streamlit as st

from data.load_data import load_invoice_master
from agents.ap_ai_agent import APAIAgent


def show_ai_assistant():

    st.title("🤖 AP AI Assistant")

    st.caption(
        "Ask questions about your Accounts Payable data using AI."
    )

    st.info(
        """
Examples:

• How many invoices are pending?
• Total invoice spend
• Average invoice amount
• Highest invoice amount
• Top supplier
• Highest tax
• Latest invoice
• Match summary
• Dashboard summary
"""
    )

    # ==========================================
    # Load Dataset
    # ==========================================

    df = load_invoice_master()

    # ==========================================
    # User Question
    # ==========================================

    question = st.text_input(
        "Ask your question",
        placeholder="Example: Which vendor has the highest invoice amount?"
    )

    # ==========================================
    # Ask AI
    # ==========================================

    if st.button("🚀 Ask AI", use_container_width=True):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Analyzing AP data..."):

                try:

                    agent = APAIAgent()

                    answer = agent.ask(
                        df,
                        question
                    )

                    st.success("Analysis Complete")

                    st.markdown("## 💡 AI Response")

                    st.write(answer)

                except Exception as e:

                    st.error(f"AI Error: {e}")

    st.divider()

    # ==========================================
    # Quick Questions
    # ==========================================

    st.subheader("📌 Suggested Questions")

    st.markdown("""
- How many invoices are pending?
- Total invoice spend
- Average invoice amount
- Highest invoice amount
- Top supplier
- Highest tax
- Latest invoice
- Match summary
- Dashboard summary
- Duplicate invoices
- Partial match invoices
- Fully received invoices
""")