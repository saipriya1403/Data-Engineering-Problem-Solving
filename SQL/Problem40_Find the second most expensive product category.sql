%sql
CREATE OR REPLACE TEMP VIEW products AS
SELECT * FROM VALUES
    (1, 'Laptop', 60000),
    (2, 'Mobile', 30000),
    (3, 'Tablet', 20000),
    (4, 'Monitor', 15000),
    (5, 'Keyboard', 5000)
AS products(product_id, product_name, price);


SELECT *
FROM products
WHERE price = (
    SELECT MAX(price)
    FROM products
    WHERE price < (
        SELECT MAX(price)
        FROM products
    )
);
