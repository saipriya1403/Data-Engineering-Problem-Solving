 CREATE OR REPLACE TEMP VIEW products AS
 SELECT * FROM VALUES
 (1, 'Keyboard', 1000),
 (2, 'Mouse', 500),
(3, 'Monitor', 8000),
(4, 'Headphones', 2500),
  (5, 'Laptop', 50000)
 AS products(ProductId, ProductName, Price);

 SELECT
ProductId,
ProductName,
 Price
FROM products
 WHERE Price > (
 SELECT AVG(Price)
FROM products
);
