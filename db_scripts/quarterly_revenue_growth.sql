-- Quarterly Revenue & QoQ Growth
WITH quarterly_revenue AS (
    SELECT
        YEAR(order_date) AS year,
        QUARTER(order_date) AS quarter,
        SUM(sales) AS revenue
    FROM fact_sales
    GROUP BY
        YEAR(order_date),
        QUARTER(order_date)
)
SELECT 
    *,
    revenue - LAG(revenue) OVER (ORDER BY quarter) AS revenue_change,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY quarter)) / LAG(revenue) OVER (ORDER BY quarter) * 100,2) AS QoQ_growth_pct
FROM quarterly_revenue;
