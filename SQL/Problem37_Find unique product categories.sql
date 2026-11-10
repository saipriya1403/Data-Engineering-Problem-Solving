%sql
CREATE OR REPLACE TEMP VIEW products AS
SELECT * FROM VALUES
    (1, 'Laptop', 'Electronics'),
    (2, 'Mobile', 'Electronics'),
    (3, 'Shirt', 'Clothing'),
    (4, 'Jeans', 'Clothing'),
    (5, 'Table', 'Furniture')
AS products(product_id, product_name, category);



SELECT DISTINCT category
FROM products;
