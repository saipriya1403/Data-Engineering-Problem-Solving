%sql

#CREATE OR REPLACE TEMP VIEW orders AS
 SELECT * FROM VALUES
    (1001, 1, 5000),
    (1002, 2, 3000),
    (1003, 1, 4000),
   (1004, 3, 7000),
   (1005, 2, 2000),
    (1006, 1, 600)
 AS orders(OrderId, CustomerId, Amount);

# COMMAND ----------

 %sql

 SELECT
 CustomerId,
SUM(Amount) AS TotalAmount
 FROM orders
GROUP BY CustomerId
 HAVING SUM(Amount) > 8000;
