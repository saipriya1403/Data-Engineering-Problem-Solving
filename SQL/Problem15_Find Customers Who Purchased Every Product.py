# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW products AS
# MAGIC SELECT * FROM VALUES
# MAGIC (1, 'Laptop'),
# MAGIC (2, 'Mobile'),
# MAGIC (3, 'Tablet')
# MAGIC AS products(ProductId, ProductName);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW orders AS
# MAGIC SELECT * FROM VALUES
# MAGIC (101, 1, 1),
# MAGIC (102, 1, 2),
# MAGIC (103, 1, 3),
# MAGIC (104, 2, 1),
# MAGIC (105, 2, 2),
# MAGIC (106, 3, 1),
# MAGIC (107, 3, 2),
# MAGIC (108, 3, 3),
# MAGIC  (109, 3, 3)
# MAGIC AS orders(OrderId, CustomerId, ProductId);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC CustomerId
# MAGIC FROM orders
# MAGIC WHERE ProductId IN (
# MAGIC SELECT ProductId
# MAGIC FROM products
# MAGIC )
# MAGIC GROUP BY CustomerId
# MAGIC HAVING COUNT(DISTINCT ProductId) = (
# MAGIC SELECT COUNT(DISTINCT ProductId)
# MAGIC FROM products
# MAGIC );