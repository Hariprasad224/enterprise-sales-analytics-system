-- Yearly Revenue & YoY Growth
WITH yearly_revenue AS (
    SELECT YEAR(order_date) AS year, SUM(sales) AS revenue
    FROM fact_sales
    GROUP BY YEAR(order_date)
)
SELECT 
    *,
    revenue - LAG(revenue) OVER (ORDER BY year) AS revenue_change,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY year)) / LAG(revenue) OVER (ORDER BY year) * 100,2) AS YoY_growth_pct
FROM yearly_revenue;
