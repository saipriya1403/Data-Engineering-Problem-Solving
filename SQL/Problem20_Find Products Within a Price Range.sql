 CREATE OR REPLACE TEMP VIEW products AS
 SELECT * FROM VALUES
     (101, 'Keyboard', 1500),
    (102, 'Mouse', 800),
    (103, 'Monitor', 7000),
   (104, 'Headphones', 2500),
     (105, 'Webcam', 4500),
   (106, 'Laptop', 55000)
 AS products(ProductId, ProductName, Price);

 SELECT
 ProductId,
 ProductName,
 Price
 FROM products
 WHERE Price BETWEEN 1000 AND 5000;
