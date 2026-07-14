from data.load_data import load_invoice_master

df = load_invoice_master()

print("Received Status Values")
print(df["Received Status"].value_counts(dropna=False))

print("\nMatched Status Values")
print(df["Matched Status"].value_counts(dropna=False))