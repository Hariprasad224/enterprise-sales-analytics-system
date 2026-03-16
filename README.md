**📊 Enterprise Sales Analytics System**

An end-to-end enterprise-grade sales analytics platform designed to demonstrate business KPI ownership, revenue-driven decision-making, and production-ready analytics engineering — not just SQL queries.

This project simulates how real-world organizations build analytics backends, KPI APIs, and executive dashboards.

**🚀 Project Overview**

The Enterprise Sales Analytics System ingests structured sales data, models it into analytical tables, computes business-critical KPIs, exposes them via FastAPI, and visualizes insights through an interactive Streamlit dashboard.

🎯 Goal: Prove the ability to translate raw data into actionable business insights using SQL, Python, and modern analytics tooling.

🧠 Business KPIs Covered
📈 Revenue Growth

Month-over-Month (MoM)

Quarter-over-Quarter (QoQ)

Year-over-Year (YoY)

**🛍️ Product Performance**

Category-wise & Sub-category-wise revenue

Profit contribution by product segment

**🌍 Regional Performance**

Revenue & profit by region

Identification of top-performing regions

**💰 Profitability & Discount Impact**

Profit margin analysis

Discount band impact on sales, quantity, and profit

**📊 Executive Summary KPIs**

Total Revenue

Average Growth %

Total Profit

Top Performing Region

**🛠️ Tech Stack**
🔹 Backend & Data

Python

FastAPI

SQLAlchemy (2.x)

MySQL

Pandas / NumPy

🔹 Frontend

Streamlit

Plotly

🔹 Dev Practices

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

DB_HOST=localhost
DB_PORT=3306
DB_NAME=enterprise_sales_analytics
DB_USER=your_username
DB_PASSWORD=your_password

5️⃣ Run Backend (FastAPI)
uvicorn backend.main:app --reload


API Docs:

http://127.0.0.1:8000/docs

6️⃣ Run Frontend (Streamlit)
streamlit run frontend/app.py

📊 Dashboard Highlights

Executive KPI cards

Time-series revenue analysis

Interactive product & region breakdowns

Discount vs profitability insights

Dark-themed, modern UI
