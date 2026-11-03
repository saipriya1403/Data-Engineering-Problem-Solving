 CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
   (101, 1, 2000),
    (102, 1, 3000),
     (103, 1, 1500),
     (104, 2, 4000),
    (105, 2, 2000),
     (106, 3, 5000),
     (107, 3, 3000),
     (108, 3, 2500),
     (109, 4, 6000)
 AS orders(OrderId, CustomerId, Amount)

 SELECT
 CustomerId,
 COUNT(OrderId) AS TotalOrders,
 SUM(Amount) AS TotalSpending
 FROM orders
  GROUP BY CustomerId
 HAVING COUNT(OrderId) > 2;
