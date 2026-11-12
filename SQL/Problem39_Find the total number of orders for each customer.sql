%sql
CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, 'Priya'),
    (102, 'Rahul'),
    (103, 'Priya'),
    (104, 'Anjali'),
    (105, 'Rahul'),
    (106, 'Priya')
AS orders(order_id, customer_name);


SELECT
    customer_name,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_name;
