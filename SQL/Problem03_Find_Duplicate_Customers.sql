
 CREATE OR REPLACE TEMP VIEW customers AS
 SELECT * FROM VALUES
   (1, 'Arun', 'arun@gmail.com'),
    (2, 'Priya', 'priya@gmail.com'),
    (3, 'Arun Kumar', 'arun@gmail.com'),
    (4, 'Kumar', 'kumar@gmail.com'),
    (5, 'Priya S', 'priya@gmail.com')
 AS customers(CustomerId, CustomerName, Email);
select * from customers


 SELECT
 Email,
 COUNT(*) AS EmailCount
 FROM customers
 GROUP BY Email
 HAVING COUNT(*) > 1;
