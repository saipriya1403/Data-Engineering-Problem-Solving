CREATE OR REPLACE TEMP VIEW orders AS
SELECT * FROM VALUES
     (101, 1, '2026-07-05', 2000),
    (102, 1, '2026-07-15', 3000),
   (103, 1, '2026-08-10', 7000),
     (104, 1, '2026-09-12', 6000),
     (105, 2, '2026-07-08', 4000),
   (106, 2, '2026-08-09', 3000),
   (107, 2, '2026-09-11', 5000),
  (108, 3, '2026-08-01', 2500),
   (109, 3, '2026-09-03', 4500)
 AS orders(OrderId, CustomerId, OrderDate, Amount);

 WITH monthly_spending AS (
    Select
    CustomerId,
   DATE_TRUNC('MONTH', TO_DATE(OrderDate)) AS OrderMonth,
    SUM(Amount) AS TotalSpending
    FROM orders
    GROUP BY
    CustomerId,
     DATE_TRUNC('MONTH', TO_DATE(OrderDate))
 ),
 previous_month AS (
     SELECT
     CustomerId,
    OrderMonth,
   TotalSpending,
     LAG(TotalSpending) OVER (
    PARTITION BY CustomerId
     ORDER BY OrderMonth
     ) AS PreviousSpending,
     LAG(OrderMonth) OVER (
     PARTITION BY CustomerId
    ORDER BY OrderMonth
     ) AS PreviousOrderMonth
    FROM monthly_spending
)

 SELECT
     CustomerId,
   OrderMonth,
     TotalSpending,
   PreviousSpending
 FROM previous_month
 WHERE TotalSpending > PreviousSpending
  AND OrderMonth = ADD_MONTHS(PreviousOrderMonth, 1)
 ORDER BY CustomerId, OrderMonth
