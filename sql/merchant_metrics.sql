SELECT
    m.merchant_id,
    m.merchant_name,
    m.category,
    COUNT(t.transaction_id) AS total_orders,
    SUM(t.revenue) AS total_gmv,
    AVG(t.revenue) AS avg_order_value
FROM merchants m
LEFT JOIN transactions t
ON m.merchant_id = t.merchant_id
GROUP BY
    m.merchant_id,
    m.merchant_name,
    m.category
ORDER BY total_gmv DESC;
