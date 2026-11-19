%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, 'Priya', DATE'2026-01-10'),
    (102, 'Rahul', DATE'2026-02-15'),
    (103, 'Anjali', DATE'2026-01-25'),
    (104, 'Kumar', DATE'2026-03-05'),
    (105, 'Divya', DATE'2026-01-30')
AS orders(order_id, customer_name, order_date);

SELECT *
FROM orders
WHERE order_date >= DATE'2026-01-01'
AND order_date < DATE'2026-02-01';
