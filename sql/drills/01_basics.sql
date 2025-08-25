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
-- 1) Total spend per customer
SELECT c.customer_id,
       c.customer_name,
       SUM(o.amount) AS total_spend
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spend DESC;

-- 2) Products never sold
SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.product_id IS NULL;

-- 3) Rank customers inside each country
SELECT country,
       customer_id,
       total_spend,
       ROW_NUMBER() OVER (PARTITION BY country ORDER BY total_spend DESC) AS country_rank
FROM (
  SELECT c.country, c.customer_id, SUM(o.amount) AS total_spend
  FROM customers c
  JOIN orders o ON o.customer_id = c.customer_id
  GROUP BY c.country, c.customer_id
) t;

-- 4) 7-day moving average of daily sales (idea)
SELECT order_date,
       SUM(amount) AS daily_sales,
       AVG(SUM(amount)) OVER (
         ORDER BY order_date
         ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
       ) AS movavg_7d
FROM orders
GROUP BY order_date
ORDER BY order_date;

-- 5) Last 30 days using a CTE, then country totals
WITH recent_orders AS (
  SELECT *
  FROM orders
  WHERE order_date >= DATE('now','-30 day') -- example for SQLite
)
SELECT c.country,
       SUM(r.amount) AS last_30d_sales
FROM customers c
JOIN recent_orders r ON r.customer_id = c.customer_id
GROUP BY c.country
ORDER BY last_30d_sales DESC;
