 CREATE OR REPLACE TEMP VIEW orders AS
 SELECT * FROM VALUES
   (101, 1, '2026-07-05', 3000),
    (102, 1, '2026-07-15', 4000),
    (103, 2, '2026-07-10', 9000),
    (104, 3, '2026-07-20', 5000),
    (105, 1, '2026-08-05', 6000),
   (106, 2, '2026-08-10', 4000),
   (107, 2, '2026-08-15', 5000),
     (108, 3, '2026-08-20', 7000),
   (109, 1, '2026-09-05', 8000),
   (110, 2, '2026-09-10', 8000),
    (111, 3, '2026-09-15', 6000)
 AS orders(OrderId, CustomerId, OrderDate, Amount);

 WITH monthly_spending AS (
     SELECT
   CustomerId,
    DATE_TRUNC('MONTH', TO_DATE(OrderDate)) AS OrderMonth,
   SUM(Amount) AS TotalSpending
   FROM orders
    GROUP BY
    CustomerId,
    DATE_TRUNC('MONTH', TO_DATE(OrderDate))
 ),
ranked_customers AS (
    SELECT
    CustomerId,
    OrderMonth,
     TotalSpending,
    DENSE_RANK() OVER (
    PARTITION BY OrderMonth
 ORDER BY TotalSpending DESC
 ) AS spending_rank
 FROM monthly_spending
)
 SELECT
     CustomerId,
         OrderMonth,
             TotalSpending
            FROM ranked_customers
            WHERE spending_rank = 1
            ORDER BY OrderMonth, CustomerId;
