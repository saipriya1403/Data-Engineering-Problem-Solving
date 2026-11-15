%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, 'Priya', DATE'2026-01-15'),
    (102, 'Rahul', DATE'2026-02-10'),
    (103, 'Priya', DATE'2026-01-05'),
    (104, 'Rahul', DATE'2026-01-20'),
    (105, 'Anjali', DATE'2026-03-12')
AS orders(order_id, customer_name, order_date);

SELECT
    customer_name,
    MIN(order_date) AS first_order_date
FROM orders
GROUP BY customer_name;
