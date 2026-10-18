# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (101, 1, '2026-07-05', 3000),
# MAGIC     (102, 1, '2026-07-15', 4000),
# MAGIC     (103, 2, '2026-07-10', 9000),
# MAGIC     (104, 3, '2026-07-20', 5000),
# MAGIC     (105, 1, '2026-08-05', 6000),
# MAGIC     (106, 2, '2026-08-10', 4000),
# MAGIC     (107, 2, '2026-08-15', 5000),
# MAGIC     (108, 3, '2026-08-20', 7000),
# MAGIC     (109, 1, '2026-09-05', 8000),
# MAGIC     (110, 2, '2026-09-10', 8000),
# MAGIC     (111, 3, '2026-09-15', 6000)
# MAGIC AS orders(OrderId, CustomerId, OrderDate, Amount);

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH monthly_spending AS (
# MAGIC     SELECT
# MAGIC     CustomerId,
# MAGIC     DATE_TRUNC('MONTH', TO_DATE(OrderDate)) AS OrderMonth,
# MAGIC     SUM(Amount) AS TotalSpending
# MAGIC     FROM orders
# MAGIC     GROUP BY
# MAGIC     CustomerId,
# MAGIC     DATE_TRUNC('MONTH', TO_DATE(OrderDate))
# MAGIC ),
# MAGIC ranked_customers AS (
# MAGIC     SELECT
# MAGIC     CustomerId,
# MAGIC     OrderMonth,
# MAGIC     TotalSpending,
# MAGIC     DENSE_RANK() OVER (
# MAGIC     PARTITION BY OrderMonth
# MAGIC ORDER BY TotalSpending DESC
# MAGIC ) AS spending_rank
# MAGIC FROM monthly_spending
# MAGIC )
# MAGIC SELECT
# MAGIC     CustomerId,
# MAGIC         OrderMonth,
# MAGIC             TotalSpending
# MAGIC             FROM ranked_customers
# MAGIC             WHERE spending_rank = 1
# MAGIC             ORDER BY OrderMonth, CustomerId;