-- Product-wise Revenue & Profit
SELECT 
    dp.category,
    dp.sub_category,
    SUM(fs.sales) AS total_sales,
    SUM(fs.profit) AS total_profit
FROM fact_sales fs
JOIN dim_product dp ON fs.product_id = dp.product_id
GROUP BY dp.category, dp.sub_category
ORDER BY total_sales DESC;