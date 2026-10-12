# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (101, 1, '2026-10-01'),
# MAGIC     (102, 1, '2026-10-02'),
# MAGIC     (103, 1, '2026-10-05'),
# MAGIC     (104, 2, '2026-10-01'),
# MAGIC     (105, 2, '2026-10-04'),
# MAGIC     (106, 3, '2026-10-03'),
# MAGIC     (107, 3, '2026-10-04')
# MAGIC AS orders(OrderId, CustomerId, OrderDate);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC WITH customer_orders AS (
# MAGIC     SELECT DISTINCT
# MAGIC      CustomerId,
# MAGIC      TO_DATE(OrderDate) AS OrderDate
# MAGIC FROM orders
# MAGIC ),
# MAGIC
# MAGIC previous_orders AS (
# MAGIC   SELECT
# MAGIC   CustomerId,
# MAGIC   OrderDate,
# MAGIC   LAG(OrderDate) OVER (
# MAGIC   PARTITION BY CustomerId
# MAGIC   ORDER BY OrderDate
# MAGIC   ) AS PreviousOrderDate
# MAGIC FROM customer_orders
# MAGIC )
# MAGIC
# MAGIC SELECT DISTINCT
# MAGIC    CustomerId
# MAGIC FROM previous_orders
# MAGIC WHERE DATEDIFF(OrderDate, PreviousOrderDate) = 1;