# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC (101, 'Laptop', 1),
# MAGIC (102, 'Mouse', 5),
# MAGIC (103, 'Keyboard', 3),
# MAGIC (104, 'Monitor', 2),
# MAGIC (105, 'USB Cable', 4)
# MAGIC AS orders(order_id, product_name, quantity);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM orders
# MAGIC WHERE quantity > 2;