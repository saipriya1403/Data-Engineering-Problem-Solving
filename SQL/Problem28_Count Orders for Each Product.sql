 CREATE OR REPLACE TEMP VIEW orders AS
 SELECT * FROM VALUES
 (101, 'Laptop'),
(102, 'Mouse'),
 (103, 'Laptop'),
(104, 'Keyboard'),
 (105, 'Mouse'),
(106, 'Laptop')
 AS orders(order_id, product_name);

 SELECT
product_name,
 COUNT(*) AS order_count
 FROM orders
 GROUP BY product_name
 ORDER BY order_count DESC;
