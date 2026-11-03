 CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
(101, 'Laptop', 1),
(102, 'Mouse', 5),
 (103, 'Keyboard', 3),
 (104, 'Monitor', 2),
(105, 'USB Cable', 4)
 AS orders(order_id, product_name, quantity);

SELECT *
 FROM orders
WHERE quantity > 2;
