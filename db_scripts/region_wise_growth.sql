-- Region-wise Revenue & Profit
SELECT 
    dc.region,
    SUM(fs.sales) AS total_sales,
    SUM(fs.profit) AS total_profit
FROM fact_sales fs
JOIN dim_customer dc ON fs.customer_id = dc.customer_id
GROUP BY dc.region
ORDER BY total_sales DESC;
