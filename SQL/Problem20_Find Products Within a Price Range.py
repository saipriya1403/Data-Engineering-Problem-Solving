# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW products AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (101, 'Keyboard', 1500),
# MAGIC     (102, 'Mouse', 800),
# MAGIC     (103, 'Monitor', 7000),
# MAGIC     (104, 'Headphones', 2500),
# MAGIC     (105, 'Webcam', 4500),
# MAGIC     (106, 'Laptop', 55000)
# MAGIC AS products(ProductId, ProductName, Price);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC ProductId,
# MAGIC ProductName,
# MAGIC Price
# MAGIC FROM products
# MAGIC WHERE Price BETWEEN 1000 AND 5000;