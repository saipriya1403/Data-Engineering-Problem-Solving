
 CREATE OR REPLACE TEMP VIEW orders AS
 SELECT * FROM VALUES
     (1001, 1, 5000),
    (1002, 2, 3000),
    (1003, 1, 4000),
    (1004, 3, 7000),
     (1005, 2, 2000),
   (1006, 3, 6000)
 AS orders(OrderId, CustomerId, Amount);


 WITH customer_totals AS (
   SELECT
   CustomerId,
     SUM(Amount) AS TotalAmount
     FROM orders
    GROUP BY CustomerId
 )

 SELECT
 CustomerId,
 TotalAmount
 FROM customer_totals
 WHERE TotalAmount > (
SELECT AVG(TotalAmount)
 FROM customer_totals );
