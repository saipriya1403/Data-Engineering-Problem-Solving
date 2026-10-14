# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (101, 1, '2026-07-05', 2000),
# MAGIC     (102, 1, '2026-07-15', 3000),
# MAGIC     (103, 1, '2026-08-10', 7000),
# MAGIC     (104, 1, '2026-09-12', 6000),
# MAGIC     (105, 2, '2026-07-08', 4000),
# MAGIC    (106, 2, '2026-08-09', 3000),
# MAGIC    (107, 2, '2026-09-11', 5000),
# MAGIC    (108, 3, '2026-08-01', 2500),
# MAGIC    (109, 3, '2026-09-03', 4500)
# MAGIC AS orders(OrderId, CustomerId, OrderDate, Amount);

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH monthly_spending AS (
# MAGIC     Select
# MAGIC     CustomerId,
# MAGIC     DATE_TRUNC('MONTH', TO_DATE(OrderDate)) AS OrderMonth,
# MAGIC     SUM(Amount) AS TotalSpending
# MAGIC     FROM orders
# MAGIC     GROUP BY
# MAGIC     CustomerId,
# MAGIC     DATE_TRUNC('MONTH', TO_DATE(OrderDate))
# MAGIC ),
# MAGIC previous_month AS (
# MAGIC     SELECT
# MAGIC     CustomerId,
# MAGIC     OrderMonth,
# MAGIC     TotalSpending,
# MAGIC     LAG(TotalSpending) OVER (
# MAGIC     PARTITION BY CustomerId
# MAGIC     ORDER BY OrderMonth
# MAGIC     ) AS PreviousSpending,
# MAGIC     LAG(OrderMonth) OVER (
# MAGIC     PARTITION BY CustomerId
# MAGIC     ORDER BY OrderMonth
# MAGIC     ) AS PreviousOrderMonth
# MAGIC     FROM monthly_spending
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     CustomerId,
# MAGIC     OrderMonth,
# MAGIC     TotalSpending,
# MAGIC     PreviousSpending
# MAGIC FROM previous_month
# MAGIC WHERE TotalSpending > PreviousSpending
# MAGIC  AND OrderMonth = ADD_MONTHS(PreviousOrderMonth, 1)
# MAGIC  ORDER BY CustomerId, OrderMonth