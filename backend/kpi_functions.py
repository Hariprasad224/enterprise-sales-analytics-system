import pandas as pd
import numpy as np
from .metric_service import run_sql

def get_monthly_revenue():
    return run_sql("monthly_revenue_growth.sql")

def get_quarterly_revenue():
    return run_sql("quarterly_revenue_growth.sql")

def get_yearly_revenue():
    return run_sql("yearly_revenue_growth.sql")

def get_product_performance():
    return run_sql("product_wise_growth.sql")

def get_region_performance():
    return run_sql("region_wise_growth.sql")

def get_profit_margin_discount():
    return run_sql("discount_ranges.sql")
