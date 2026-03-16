**📊 Enterprise Sales Analytics System + AI SQL Agent**

An end-to-end analytics platform that combines business KPI engineering, API-driven analytics, interactive dashboards, and an AI-powered natural language SQL agent.

This project demonstrates how modern analytics systems are built in production: from raw data → KPI computation → API exposure → dashboard consumption → natural language querying.

**🚀 Project Overview**

The system is designed to simulate how enterprises answer business questions through structured analytics and AI-assisted querying.

It provides:

KPI-driven executive dashboards

API-based analytics delivery

SQL-backed business intelligence

Natural language to SQL using LLMs

🎯 Goal: Convert raw business data into decision-ready intelligence using SQL, Python, APIs, and GenAI.

**🧠 Core Business KPIs**
📈 Revenue Growth

Month-over-Month (MoM)

Quarter-over-Quarter (QoQ)

Year-over-Year (YoY)

🛍️ Product Performance

Category-wise revenue

Sub-category profit contribution

Product quantity trends

🌍 Regional Performance

Revenue by region

Profit by geography

Top-performing region identification

💰 Discount Impact

Discount range vs revenue

Discount range vs profitability

Quantity sold by discount band

📊 Executive Summary

Total Revenue

Average Growth %

Total Profit

Top Region

🤖 AI SQL Agent (Natural Language to Database)

Users can ask business questions in plain English such as:

"Show top 5 customers by revenue"
"What are top products by quantity sold?"
"Which region has highest profit?"

The AI agent performs:

✅ Converts English → SQL
✅ Executes SQL on MySQL database
✅ Returns result
✅ Explains output

**🛠️ Tech Stack**
Backend

Python

FastAPI

SQLAlchemy

MySQL

Pandas

Frontend

Streamlit

Plotly

AI Layer

LangChain

Google Gemini API

Configuration

python-dotenv

modular project structure

**🔹 Dev Practices**

.env based secret management

Modular KPI computation

API-first analytics design

Clean separation of concerns

**⚙️ Setup Instructions**
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/enterprise-sales-analytics-system.git
cd enterprise-sales-analytics-system

2️⃣ Create Virtual Environment
python -m venv env
env\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file using .env.example as reference:

DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password

5️⃣ Run Backend (FastAPI)
uvicorn backend.main:app --reload


API Docs:

http://127.0.0.1:8000/docs

6️⃣ Run Frontend (Streamlit)
streamlit run frontend/app.py

**📊 Dashboard Features**

Executive KPI cards

Revenue trend visualizations

Product hierarchy insights

Region-wise performance

Discount impact analytics

AI query tab for natural language business questions

**🔐 Safety Controls in AI SQL Agent**

To protect the database:

Only SELECT queries are allowed.

Unsafe operations are blocked:

❌ DELETE
❌ DROP
❌ UPDATE
❌ INSERT

📊 Dashboard Features

Executive KPI cards

Revenue trend visualizations

Product hierarchy insights

Region-wise performance

Discount impact analytics

AI query tab for natural language business questions

🔐 Safety Controls in AI SQL Agent

To protect the database:

Only SELECT queries are allowed.

Unsafe operations are blocked:

❌ DELETE
❌ DROP
❌ UPDATE
❌ INSERT

**🎯 What This Project Demonstrates**

✔️ SQL-based analytics engineering
✔️ KPI ownership
✔️ Backend API development
✔️ Interactive BI dashboarding
✔️ LLM integration with databases
✔️ Natural language analytics workflows
