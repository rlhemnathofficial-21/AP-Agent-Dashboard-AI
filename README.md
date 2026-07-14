# 📊 AP Agent Dashboard AI

An AI-powered **Accounts Payable Dashboard** built using **Streamlit, Pandas, and Llama 3.2 (Ollama)**. The application provides interactive AP analytics, invoice monitoring, and a natural language AI Assistant for querying invoice data.

---

## 🚀 Features

- 📊 Interactive Dashboard
- 📈 Invoice Analytics
- 🏢 Supplier Analysis
- 📅 Invoice Aging
- 🎯 Match Scoring
- 📄 Invoice Management
- 🤖 AI Assistant (Llama 3.2)
- 📤 Export Reports
- 🔍 Natural Language Queries

---

## 🧠 AI Assistant

The AI Assistant allows users to ask questions about Accounts Payable data in natural language.

### Example Questions

- How many invoices are pending?
- What is the total invoice spend?
- Who is the top supplier?
- Show the match summary.
- What is the highest invoice amount?
- Generate a dashboard summary.

---

## 🏗️ Architecture

```text
Excel Dataset
      │
      ▼
Pandas Data Processing
      │
      ▼
Dashboard Analytics
      │
      ├── KPI Cards
      ├── Charts
      ├── Tables
      │
      ▼
🤖 AP AI Assistant
      │
      ▼
Llama 3.2 (Ollama)
      │
      ▼
Business Response
```

---

## 📂 Project Structure

```text
AP-Agent-Dashboard-AI/
│
├── agents/
├── assets/
├── charts/
├── components/
├── data/
├── llm/
├── pages/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Ollama
- Llama 3.2
- Git & GitHub

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/rlhemnathofficial-21/AP-Agent-Dashboard-AI.git
```

Go to the project folder:

```bash
cd AP-Agent-Dashboard-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2:3b
```

Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run the Project

Start the Streamlit application:

```bash
streamlit run app.py
```

Open your browser:

```text
http://localhost:8501
```

---

## 📊 Dashboard Modules

- Dashboard
- Invoices
- Analytics
- AI Assistant
- Settings

---

## 💡 Sample AI Queries

```text
How many invoices are pending?

Total invoice spend

Average invoice amount

Top supplier

Highest invoice amount

Match summary

Generate dashboard summary
```

---

## 🔮 Future Enhancements

- Chat-style AI conversation
- Invoice risk prediction
- PDF report generation
- Multi-file upload
- Role-based authentication
- Advanced AP insights

---

## 👨‍💻 Author

**R. HEMNATH**

Accounts Payable AI Dashboard Project

---

## ⭐ Acknowledgements

- Streamlit
- Pandas
- Plotly
- Ollama
- Meta Llama 3.2

---

## 📄 License

This project is developed for educational and internship purposes.