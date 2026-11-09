%sql
CREATE OR REPLACE TEMP VIEW products AS
SELECT * FROM VALUES
    (1, 'Apple'),
    (2, 'Laptop'),
    (3, 'Orange'),
    (4, 'Mobile'),
    (5, 'Table')
AS products(product_id, product_name);


SELECT *
FROM products
WHERE product_name LIKE '%e';
