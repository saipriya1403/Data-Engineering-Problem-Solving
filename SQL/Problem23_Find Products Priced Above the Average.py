# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW products AS
# MAGIC SELECT * FROM VALUES
# MAGIC (1, 'Keyboard', 1000),
# MAGIC (2, 'Mouse', 500),
# MAGIC (3, 'Monitor', 8000),
# MAGIC (4, 'Headphones', 2500),
# MAGIC  (5, 'Laptop', 50000)
# MAGIC  AS products(ProductId, ProductName, Price);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC ProductId,
# MAGIC ProductName,
# MAGIC Price
# MAGIC FROM products
# MAGIC WHERE Price > (
# MAGIC SELECT AVG(Price)
# MAGIC FROM products
# MAGIC );