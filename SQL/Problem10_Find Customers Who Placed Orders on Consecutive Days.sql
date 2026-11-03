CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
    (101, 1, '2026-10-01'),
     (102, 1, '2026-10-02'),
     (103, 1, '2026-10-05'),
     (104, 2, '2026-10-01'),
     (105, 2, '2026-10-04'),
    (106, 3, '2026-10-03'),
    (107, 3, '2026-10-04')
 AS orders(OrderId, CustomerId, OrderDate);

WITH customer_orders AS (
     SELECT DISTINCT
      CustomerId,
      TO_DATE(OrderDate) AS OrderDate
FROM orders
 ),

 previous_orders AS (
   SELECT
   CustomerId,
   OrderDate,
  LAG(OrderDate) OVER (
   PARTITION BY CustomerId
   ORDER BY OrderDate
   ) AS PreviousOrderDate
 FROM customer_orders
 )

 SELECT DISTINCT
   CustomerId
 FROM previous_orders
 WHERE DATEDIFF(OrderDate, PreviousOrderDate) = 1;
