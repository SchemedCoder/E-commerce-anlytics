SELECT
    COUNT(session_id) AS total_sessions,
    SUM(CASE WHEN add_to_cart = 'Yes' THEN 1 ELSE 0 END) AS add_to_cart_sessions,
    SUM(CASE WHEN checkout_initiated = 'Yes' THEN 1 ELSE 0 END) AS checkout_sessions,
    (SELECT COUNT(*) FROM transactions) AS total_orders
FROM sessions;
