from .kpi_functions import (
    get_monthly_revenue,
    get_product_performance,
    get_region_performance
)

def get_kpi_summary():
    monthly_df = get_monthly_revenue()
    product_df = get_product_performance()
    region_df = get_region_performance()

    return {
        "total_revenue": round(monthly_df["revenue"].sum(), 2),
        "avg_mom_growth_pct": round(monthly_df["MoM_growth_pct"].mean(), 2),
        "total_profit": round(product_df["total_profit"].sum(), 2),
        "top_region": region_df.sort_values(
            "total_sales", ascending=False
        ).iloc[0]["region"]
    }
