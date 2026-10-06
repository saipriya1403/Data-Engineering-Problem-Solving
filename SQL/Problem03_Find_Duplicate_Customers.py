# Databricks notebook source
# MAGIC %md
# MAGIC ### Find Duplicate Customers

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW customers AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun', 'arun@gmail.com'),
# MAGIC     (2, 'Priya', 'priya@gmail.com'),
# MAGIC     (3, 'Arun Kumar', 'arun@gmail.com'),
# MAGIC     (4, 'Kumar', 'kumar@gmail.com'),
# MAGIC     (5, 'Priya S', 'priya@gmail.com')
# MAGIC AS customers(CustomerId, CustomerName, Email);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from customers

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC Email,
# MAGIC COUNT(*) AS EmailCount
# MAGIC FROM customers
# MAGIC GROUP BY Email
# MAGIC HAVING COUNT(*) > 1;