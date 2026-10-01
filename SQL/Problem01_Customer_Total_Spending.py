# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1001, 1, 5000),
# MAGIC     (1002, 2, 3000),
# MAGIC     (1003, 1, 4000),
# MAGIC     (1004, 3, 7000),
# MAGIC     (1005, 2, 2000),
# MAGIC     (1006, 1, 6000)
# MAGIC AS orders(OrderId, CustomerId, Amount);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC
# MAGIC SELECT
# MAGIC CustomerId,
# MAGIC SUM(Amount) AS TotalAmount
# MAGIC FROM orders
# MAGIC GROUP BY CustomerId
# MAGIC HAVING SUM(Amount) > 8000;
