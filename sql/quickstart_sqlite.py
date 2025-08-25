import sqlite3, os

db_path = os.path.join(os.path.dirname(__file__), "sample_shop.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

# Make demo tables
cur.executescript("""
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_items;

CREATE TABLE customers(customer_id INTEGER PRIMARY KEY, customer_name TEXT, country TEXT);
CREATE TABLE products(product_id INTEGER PRIMARY KEY, product_name TEXT);
CREATE TABLE orders(order_id INTEGER PRIMARY KEY, customer_id INTEGER, order_date TEXT, amount REAL);
CREATE TABLE order_items(order_id INTEGER, product_id INTEGER, quantity INTEGER, price REAL);

INSERT INTO customers VALUES
  (1,'Aisha','UK'),(2,'Ben','UK'),(3,'Caro','IN'),(4,'Drew','IN');

INSERT INTO products VALUES
  (1,'Phone'),(2,'Case'),(3,'Charger');

INSERT INTO orders VALUES
  (1,1,'2025-08-18',300.0),
  (2,1,'2025-08-19',50.0),
  (3,2,'2025-08-19',120.0),
  (4,3,'2025-08-22',200.0),
  (5,4,'2025-08-23',0.0);

INSERT INTO order_items VALUES
  (1,1,1,300.0),
  (2,2,2,25.0),
  (3,1,1,120.0),
  (4,3,2,100.0);
""")
con.commit()

print("\n1) Total spend per customer")
for row in cur.execute("""
SELECT c.customer_id, c.customer_name, SUM(o.amount) AS total_spend
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spend DESC;
"""):
    print(row)

print("\n2) Products never sold")
for row in cur.execute("""
SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.product_id IS NULL;
"""):
    print(row)

print("\n3) Last 30 days sales by country")
for row in cur.execute("""
WITH recent_orders AS (
  SELECT * FROM orders
  WHERE order_date >= date('now','-30 day')
)
SELECT c.country, SUM(r.amount) AS last_30d_sales
FROM customers c
JOIN recent_orders r ON r.customer_id = c.customer_id
GROUP BY c.country
ORDER BY last_30d_sales DESC;
"""):
    print(row)

con.close()
print(f"\nCreated demo DB at: {db_path}")
