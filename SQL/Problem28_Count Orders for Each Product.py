# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC (101, 'Laptop'),
# MAGIC (102, 'Mouse'),
# MAGIC (103, 'Laptop'),
# MAGIC (104, 'Keyboard'),
# MAGIC (105, 'Mouse'),
# MAGIC (106, 'Laptop')
# MAGIC AS orders(order_id, product_name);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC product_name,
# MAGIC COUNT(*) AS order_count
# MAGIC FROM orders
# MAGIC GROUP BY product_name
# MAGIC ORDER BY order_count DESC;