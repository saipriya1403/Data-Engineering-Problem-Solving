%sql
CREATE OR REPLACE TEMP VIEW customers AS
SELECT * FROM VALUES
    (1, 'Arun'),
    (2, 'Priya'),
    (3, 'Rahul'),
    (4, 'Divya')
AS customers(customer_id, customer_name);

CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, 1, 5000),
    (102, 2, 3000),
    (103, 1, 2000)
AS orders(order_id, customer_id, amount);

SELECT
    c.customer_id,
    c.customer_name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
