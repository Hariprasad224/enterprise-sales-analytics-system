-- Profit Margin per order
SELECT 
    order_id,
    sales,
    profit,
    ROUND(profit / sales * 100,2) AS profit_margin_pct,
    discount
FROM fact_sales;