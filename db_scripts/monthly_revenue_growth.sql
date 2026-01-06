-- Monthly Revenue & MoM Growth
WITH monthly_revenue AS (
    SELECT 
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(sales) AS revenue
    FROM fact_sales
    GROUP BY YEAR(order_date), MONTH(order_date)
    ORDER BY year, month
)
SELECT 
    *,
    revenue - LAG(revenue) OVER (ORDER BY year, month) AS revenue_change,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY year, month)) / LAG(revenue) OVER (ORDER BY year, month) * 100,2) AS MoM_growth_pct
FROM monthly_revenue;
