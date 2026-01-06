import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# -------------------------------
# CONFIG
# -------------------------------
API_BASE = "http://127.0.0.1:8000"

kpi_data = requests.get(f"{API_BASE}/kpi-summary").json()

st.set_page_config(
    page_title="Enterprise Sales Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# CUSTOM CSS (PREMIUM UI)
# -------------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

body {
    background-color: #0E1117;
}

.section-title {
    font-size: 22px;
    font-weight: 600;
    margin: 20px 0 10px 0;
}

.kpi-card {
    background: linear-gradient(135deg, #1f2937, #111827);
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 15px 35px rgba(0,0,0,0.45);
    text-align: center;
}

.kpi-title {
    font-size: 13px;
    color: #9CA3AF;
    letter-spacing: 0.5px;
}

.kpi-value {
    font-size: 30px;
    font-weight: 700;
    margin-top: 6px;
}

.plot-container {
    background-color: #111827;
    padding: 20px;
    border-radius: 18px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------
def fetch_data(endpoint):
    response = requests.get(f"{API_BASE}{endpoint}")
    response.raise_for_status()
    return pd.DataFrame(response.json())

def kpi_card(title, value):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("## 📊 Enterprise Sales Analytics System")
st.caption("Executive-level insights • Revenue-driven decision making")

# -------------------------------
# LOAD DATA
# -------------------------------
monthly_df = fetch_data("/monthly-revenue")
quarterly_df = fetch_data("/quarterly-revenue")
yearly_df = fetch_data("/yearly-revenue")
product_df = fetch_data("/product-performance")
region_df = fetch_data("/region-performance")
discount_df = fetch_data("/profit-margin-discount")

# -------------------------------
# KPI CALCULATIONS
# -------------------------------
# total_revenue = monthly_df["sales"].sum()
# avg_mom_growth = monthly_df["mom_growth_pct"].mean()
# total_profit = product_df["profit"].sum()
# top_region = region_df.sort_values("sales", ascending=False).iloc[0]["region"]

# -------------------------------
# EXECUTIVE KPI CARDS
# -------------------------------
st.markdown("<div class='section-title'>Executive KPIs</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="💰 Total Revenue",
    value=f"${kpi_data['total_revenue']:,.0f}"
)

col2.metric(
    label="📈 Avg MoM Growth",
    value=f"{kpi_data['avg_mom_growth_pct']}%"
)

col3.metric(
    label="💵 Total Profit",
    value=f"${kpi_data['total_profit']:,.0f}"
)

col4.metric(
    label="🌍 Top Region",
    value=kpi_data["top_region"]
)

# -------------------------------
# TABS
# -------------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["📈 Revenue Growth", "🛍️ Products", "🌍 Regions", "💰 Discount Impact"]
)

# -------------------------------
# REVENUE GROWTH
# -------------------------------
with tab1:
    st.markdown("<div class='section-title'>Revenue Growth Trends</div>", unsafe_allow_html=True)

    fig = px.line(
        monthly_df,
        x="month",
        y="revenue",
        color="year",
        markers=True
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E5E7EB"),
        title="Monthly Revenue Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
        yearly_df,
        x="year",
        y="revenue",
        text="revenue"
    )
    fig2.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E5E7EB"),
        title="Yearly Revenue"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# PRODUCT PERFORMANCE
# -------------------------------
with tab2:
    st.markdown("<div class='section-title'>Product Performance</div>", unsafe_allow_html=True)

    fig = px.treemap(
        product_df,
        path=["category", "sub_category"],
        values="total_sales"
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E5E7EB"),
        title="Revenue by Category & Sub-Category"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# REGION PERFORMANCE
# -------------------------------
with tab3:
    st.markdown("<div class='section-title'>Regional Performance</div>", unsafe_allow_html=True)

    fig = px.bar(
        region_df,
        x="region",
        y="total_sales",
        text="total_sales",
        color="region"
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E5E7EB"),
        title="Revenue by Region"
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# DISCOUNT IMPACT
# -------------------------------
with tab4:
    st.markdown(
        "<div class='section-title'>💸 Discount vs Profit Margin</div>",
        unsafe_allow_html=True
    )

    fig = px.bar(
        discount_df,
        x="discount_range",
        y="total_profit",
        text="total_profit"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E5E7EB"),
        xaxis_title="Discount Range",
        yaxis_title="Average Profit Margin (%)",
        title="Impact of Discounts on Profit Margin"
    )

    st.plotly_chart(fig, use_container_width=True)
