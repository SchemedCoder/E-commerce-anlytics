SELECT
    c.customer_id,
    c.customer_name,
    c.acquisition_channel,
    COUNT(t.transaction_id) AS total_orders,
    SUM(t.revenue) AS total_revenue,
    AVG(t.revenue) AS avg_order_value
FROM customers c
LEFT JOIN transactions t
ON c.customer_id = t.customer_id
GROUP BY
    c.customer_id,
    c.customer_name,
    c.acquisition_channel
ORDER BY total_revenue DESC;
