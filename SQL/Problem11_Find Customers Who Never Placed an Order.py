# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW customers AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun'),
# MAGIC     (2, 'Priya'),
# MAGIC     (3, 'Kumar'),
# MAGIC     (4, 'Divya'),
# MAGIC     (5, 'Meena')
# MAGIC AS customers(CustomerId, CustomerName);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (101, 1, 2000),
# MAGIC     (102, 2, 3000),
# MAGIC     (103, 1, 1500),
# MAGIC     (104, 3, 4000)
# MAGIC AS orders(OrderId, CustomerId, Amount);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC c.CustomerId,
# MAGIC c.CustomerName
# MAGIC FROM customers c
# MAGIC LEFT JOIN orders o
# MAGIC ON c.CustomerId = o.CustomerId
# MAGIC WHERE o.CustomerId IS NULL;