import pandas as pd

from llm.ollama_client import OllamaClient


class APAIAgent:

    def __init__(self):

        self.llm = OllamaClient()

    # ==========================================================
    # MAIN AI FUNCTION
    # ==========================================================

    def ask(self, df: pd.DataFrame, question: str):

        q = question.lower().strip()

        # ==========================================================
        # PENDING INVOICES
        # ==========================================================

        if "pending" in q:

            pending = df[
                df["Received Status"] == "Partially Received"
            ]

            return f"""
Pending Invoices : {len(pending)}

Business Meaning

Invoices marked as "Partially Received" are considered pending because the complete goods/services have not yet been received.
"""

        # ==========================================================
        # FULLY RECEIVED
        # ==========================================================

        if "received" in q:

            received = df[
                df["Received Status"] == "Fully Received"
            ]

            return f"""
Fully Received Invoices : {len(received)}
"""

        # ==========================================================
        # MATCH SUMMARY
        # ==========================================================

        if "match" in q:

            summary = (

                df["Matched Status"]

                .value_counts()

                .to_string()

            )

            return f"""
Invoice Match Summary

{summary}
"""

        # ==========================================================
        # DUPLICATES
        # ==========================================================

        if "duplicate" in q:

            duplicates = df[
                df["Matched Status"] == "Duplicates"
            ]

            return f"""
Duplicate Invoices : {len(duplicates)}
"""

        # ==========================================================
        # PARTIAL MATCH
        # ==========================================================

        if "partial" in q:

            partial = df[
                df["Matched Status"] == "Partial Match"
            ]

            return f"""
Partial Match Invoices : {len(partial)}
"""

        # ==========================================================
        # TOTAL INVOICES
        # ==========================================================

        if (

            "total invoice" in q

            or "invoice count" in q

            or "number of invoices" in q

        ):

            return f"""
Total Invoices : {len(df)}
"""

        # ==========================================================
        # TOTAL SPEND
        # ==========================================================

        if (

            "total spend" in q

            or "invoice spend" in q

            or "total amount" in q

        ):

            total = df["Invoice Amount"].sum()

            return f"""
Total Invoice Spend

${total:,.2f}
"""

        # ==========================================================
        # AVERAGE INVOICE
        # ==========================================================

        if "average invoice" in q:

            avg = df["Invoice Amount"].mean()

            return f"""
Average Invoice Amount

${avg:,.2f}
"""

        # ==========================================================
        # HIGHEST INVOICE
        # ==========================================================

        if (

            "highest invoice" in q

            or "largest invoice" in q

            or "maximum invoice" in q

        ):

            row = df.loc[

                df["Invoice Amount"].idxmax()

            ]

            return f"""
Highest Invoice

Vendor

{row["Vendor Name"]}

Invoice Number

{row["Invoice No"]}

Invoice Amount

${row["Invoice Amount"]:,.2f}
"""

        # ==========================================================
        # TOP SUPPLIERS
        # ==========================================================

        if (

            "top supplier" in q

            or "top vendor" in q

            or "highest supplier" in q

        ):

            suppliers = (

                df.groupby("Vendor Name")["Invoice Amount"]

                .sum()

                .sort_values(ascending=False)

                .head(5)

            )

            return f"""
Top 5 Suppliers

{suppliers.to_string()}
"""

        # ==========================================================
        # HIGHEST TAX
        # ==========================================================

        if "highest tax" in q:

            row = df.loc[
                df["Invoice Tax Amount"].idxmax()
            ]

            return f"""
Highest Tax Invoice

Vendor

{row["Vendor Name"]}

Invoice

{row["Invoice No"]}

Tax

${row["Invoice Tax Amount"]:,.2f}
"""

        # ==========================================================
        # LATEST INVOICE
        # ==========================================================

        if (

            "latest invoice" in q

            or "recent invoice" in q

        ):

            latest = (

                df.sort_values(

                    "Invoice Date",

                    ascending=False

                )

                .iloc[0]

            )

            return f"""
Latest Invoice

Invoice Number

{latest["Invoice No"]}

Vendor

{latest["Vendor Name"]}

Date

{latest["Invoice Date"]}

Amount

${latest["Invoice Amount"]:,.2f}
"""

        # ==========================================================
        # AI DASHBOARD SUMMARY
        # ==========================================================

        if (

            "summary" in q

            or "dashboard" in q

            or "overview" in q

        ):

            total = len(df)

            spend = df["Invoice Amount"].sum()

            avg = df["Invoice Amount"].mean()

            received = (

                df["Received Status"]

                == "Fully Received"

            ).sum()

            partial = (

                df["Received Status"]

                == "Partially Received"

            ).sum()

            prompt = f"""

You are an Accounts Payable Business Analyst.

Using the statistics below, generate a professional business summary.

Total Invoices : {total}

Total Spend : {spend}

Average Invoice : {avg}

Fully Received : {received}

Partially Received : {partial}

Write a professional summary in bullet points.

"""

            return self.llm.ask(prompt)

        # ==========================================================
        # FALLBACK TO LLM
        # ==========================================================

        context = df.head(50).to_string(index=False)

        prompt = f"""

You are an expert Accounts Payable AI Assistant.

Answer ONLY using the dataset below.

Dataset

{context}

Question

{question}

If the answer cannot be determined,
reply:

"I couldn't find that information in the current dataset."

Provide a concise business answer.

"""

        return self.llm.ask(prompt)