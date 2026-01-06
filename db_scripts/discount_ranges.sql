WITH discount_buckets AS (
    SELECT
        CASE 
            WHEN discount >= 0 AND discount < 0.05 THEN '0-5%%'
            WHEN discount >= 0.05 AND discount < 0.1 THEN '5-10%%'
            WHEN discount >= 0.1 AND discount < 0.2 THEN '10-20%%'
            ELSE '>20%%'
        END AS discount_range,
        sales,
        profit,
        quantity
    FROM fact_sales
)
SELECT
    discount_range,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM discount_buckets
GROUP BY discount_range
ORDER BY discount_range;
