# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .kpi_functions import (
    get_monthly_revenue,
    get_quarterly_revenue,
    get_yearly_revenue,
    get_product_performance,
    get_region_performance,
    get_profit_margin_discount,
)
from .kpi_summary import get_kpi_summary

app = FastAPI(title="Enterprise Sales Analytics API")

# Allow Streamlit frontend and others
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Revenue Growth
# -----------------------------
@app.get("/monthly-revenue")
def monthly_revenue():
    return get_monthly_revenue().to_dict(orient="records")

@app.get("/quarterly-revenue")
def quarterly_revenue():
    return get_quarterly_revenue().to_dict(orient="records")

@app.get("/yearly-revenue")
def yearly_revenue():
    return get_yearly_revenue().to_dict(orient="records")

# -----------------------------
# Product & Region Performance
# -----------------------------
@app.get("/product-performance")
def product_performance():
    return get_product_performance().to_dict(orient="records")

@app.get("/region-performance")
def region_performance():
    return get_region_performance().to_dict(orient="records")

# -----------------------------
# Profit Margin & Discount Impact
# -----------------------------
@app.get("/profit-margin-discount")
def profit_margin_discount():
    return get_profit_margin_discount().to_dict(orient="records")
# -----------------------------
# KPI Summary
@app.get("/kpi-summary")
def kpi_summary():
    return get_kpi_summary()