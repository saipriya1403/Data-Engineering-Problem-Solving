%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, DATE'2026-01-05', 2000),
    (102, DATE'2026-01-15', 3000),
    (103, DATE'2026-02-10', 4000),
    (104, DATE'2026-02-20', 1500),
    (105, DATE'2026-03-12', 5000)
AS orders(order_id, order_date, amount);


SELECT
    DATE_FORMAT(order_date, 'yyyy-MM') AS order_month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY DATE_FORMAT(order_date, 'yyyy-MM')
ORDER BY order_month;
