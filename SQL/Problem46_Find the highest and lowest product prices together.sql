%sql
CREATE OR REPLACE TEMP VIEW products AS
SELECT * FROM VALUES
    (1, 'Laptop', 50000),
    (2, 'Mobile', 30000),
    (3, 'Tablet', 20000),
    (4, 'Keyboard', 5000),
    (5, 'Monitor', 15000)
AS products(product_id, product_name, price);
SELECT
    MAX(price) AS highest_price,
    MIN(price) AS lowest_price
FROM products;
