-- 3 joins (inner, left), 2 window functions, 2 aggregations, 1 CTE, 2 date filters
-- Replace schema/table names as needed.
WITH recent_orders AS (
  SELECT *
  FROM orders
  WHERE order_date >= DATEADD(day, -30, CURRENT_DATE)
)
SELECT c.customer_id,
       c.country,
       SUM(o.amount) AS total_amount,
       AVG(o.amount) AS avg_amount,
       ROW_NUMBER() OVER (PARTITION BY c.country ORDER BY SUM(o.amount) DESC) AS rn
FROM customers c
LEFT JOIN recent_orders o ON o.customer_id = c.customer_id
GROUP BY 1,2
HAVING SUM(o.amount) > 0
ORDER BY total_amount DESC;
