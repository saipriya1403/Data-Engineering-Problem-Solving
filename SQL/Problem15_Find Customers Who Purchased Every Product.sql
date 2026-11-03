 CREATE OR REPLACE TEMP VIEW products AS
 SELECT * FROM VALUES
(1, 'Laptop'),
(2, 'Mobile'),
 (3, 'Tablet')
AS products(ProductId, ProductName);

 CREATE OR REPLACE TEMP VIEW orders AS
 SELECT * FROM VALUES
 (101, 1, 1),
 (102, 1, 2),
 (103, 1, 3),
 (104, 2, 1),
(105, 2, 2),
 (106, 3, 1),
 (107, 3, 2),
 (108, 3, 3),
 (109, 3, 3)
AS orders(OrderId, CustomerId, ProductId);

 SELECT
 CustomerId
 FROM orders
 WHERE ProductId IN (
SELECT ProductId
 FROM products
 )
 GROUP BY CustomerId
 HAVING COUNT(DISTINCT ProductId) = (
 SELECT COUNT(DISTINCT ProductId)
 FROM products
 );
