%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, 'Priya', DATE'2026-01-15'),
    (102, 'Rahul', DATE'2026-03-20'),
    (103, 'Anjali', DATE'2026-02-10'),
    (104, 'Kumar', DATE'2026-04-05'),
    (105, 'Divya', DATE'2026-03-01')
AS orders(order_id, customer_name, order_date);


SELECT MAX(order_date) AS latest_order_date
FROM orders;
