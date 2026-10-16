# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (101, 1, 2000),
# MAGIC     (102, 1, 3000),
# MAGIC     (103, 1, 1500),
# MAGIC     (104, 2, 4000),
# MAGIC     (105, 2, 2000),
# MAGIC     (106, 3, 5000),
# MAGIC     (107, 3, 3000),
# MAGIC     (108, 3, 2500),
# MAGIC     (109, 4, 6000)
# MAGIC AS orders(OrderId, CustomerId, Amount)

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC CustomerId,
# MAGIC COUNT(OrderId) AS TotalOrders,
# MAGIC SUM(Amount) AS TotalSpending
# MAGIC FROM orders
# MAGIC  GROUP BY CustomerId
# MAGIC HAVING COUNT(OrderId) > 2;