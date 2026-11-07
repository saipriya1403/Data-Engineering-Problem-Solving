%sql
CREATE OR REPLACE TEMP VIEW customers AS
SELECT * FROM VALUES
(1, 'Arun'),
(2, 'Priya'),
(3, 'Rahul'),
(4, 'Sneha'),
(5, 'Kiran')
AS customers(customer_id, customer_name);

%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
(101, 1, 5000),
(102, 2, 3000),
(103, 1, 2000),
(104, 4, 4500)
AS orders(order_id, customer_id, amount);

%sql
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

