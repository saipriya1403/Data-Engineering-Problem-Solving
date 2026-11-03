 CREATE OR REPLACE TEMP VIEW customers AS
SELECT * FROM VALUES
    (1, 'Arun'),
     (2, 'Priya'),
     (3, 'Kumar'),
   (4, 'Divya'),
   (5, 'Meena')
 AS customers(CustomerId, CustomerName);

 CREATE OR REPLACE TEMP VIEW orders AS
 SELECT * FROM VALUES
   (101, 1, 2000),
    (102, 2, 3000),
    (103, 1, 1500),
    (104, 3, 4000)
 AS orders(OrderId, CustomerId, Amount);

 SELECT
 c.CustomerId,
 c.CustomerName
 FROM customers c
 LEFT JOIN orders o
 ON c.CustomerId = o.CustomerId
 WHERE o.CustomerId IS NULL;
