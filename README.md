# 📊 AP Agent Dashboard

An AI-powered **Accounts Payable (AP) Analytics Dashboard** built using **Streamlit, Plotly, and Pandas**.

The dashboard helps finance teams monitor invoices, supplier spending, invoice matching, workflow status, and overall AP performance through interactive charts and KPIs.

---

# 🚀 Features

### Dashboard

- 📄 Total Invoices KPI
- ✅ Matched Invoices KPI
- ⏳ Pending Invoices KPI
- ⚠️ Exceptions KPI
- 🔁 Duplicate Invoices KPI
- 💰 Total Invoice Value KPI

### Analytics

- 📈 Monthly Invoice Spend
- 🏢 Top Suppliers by Invoice Value
- 🥧 Match Status Distribution
- 📂 Category-wise Invoice Distribution
- 📅 Invoice Aging Analysis
- ⚠️ Supplier Risk Spending Analysis

### Invoice Management

- 🔍 Search Invoice
- 🏢 Vendor Filter
- 📂 Category Filter
- 📄 Invoice Table
- ⬇️ Export CSV

### Settings

- Dashboard Preferences
- Theme Selection
- Currency Selection
- Table Settings

---

# 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Plotly
- Pandas
- OpenPyXL

---

# 📂 Project Structure

```
AP-Agent-Dashboard/

├── app.py
├── requirements.txt
├── README.md
│
├── charts/
│   ├── spend_chart.py
│   ├── vendor_chart.py
│   ├── status_chart.py
│   ├── category_chart.py
│   ├── aging_chart.py
│   └── supplier_risk_chart.py
│
├── components/
│   ├── filters.py
│   ├── metric_cards.py
│   └── export_buttons.py
│
├── data/
│   ├── load_data.py
│   └── AP Agent Sample Dataset copy.xlsx
│
├── pages/
│   ├── dashboard.py
│   ├── invoices.py
│   ├── analytics.py
│   └── settings.py
│
└── assets/
```

---

# 📊 Dashboard Modules

## 🏠 Dashboard

Provides an overview of invoice processing with KPIs and visual analytics.

---

## 📄 Invoice Management

Manage invoices using search, filters, and CSV export.

---

## 📈 Analytics

Displays detailed business insights through interactive charts.

---

## ⚙️ Settings

Configure dashboard appearance and preferences.

---

# 📈 KPIs

- Total Invoices
- Matched Invoices
- Pending Invoices
- Exceptions
- Duplicate Invoices
- Total Invoice Value

---

# 📊 Charts

- Monthly Invoice Spend
- Top Suppliers
- Match Status
- Category Distribution
- Invoice Aging
- Supplier Risk Spending

---

# ▶️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd AP-Agent-Dashboard
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

---

# 📷 Screenshots

Add screenshots here after running the project.

Example:

```
README Images/

dashboard.png

analytics.png

invoice_management.png

settings.png
```

---

# 🔮 Future Enhancements

- PDF Export
- User Authentication
- Database Integration
- AI Invoice Insights
- Real-time Notifications
- Role-based Access Control

---

# 👨‍💻 Developed By

**R. Hemnath**

BE Cyber Security

Streamlit • Plotly • Python • Pandas