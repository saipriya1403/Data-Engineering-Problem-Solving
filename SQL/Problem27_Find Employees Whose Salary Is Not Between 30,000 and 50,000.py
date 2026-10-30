# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC (101, 'Arun', 25000),
# MAGIC (102, 'Priya', 45000),
# MAGIC (103, 'Rahul', 55000),
# MAGIC (104, 'Sneha', 35000),
# MAGIC (105, 'Kiran', 60000)
# MAGIC AS employees(emp_id, emp_name, salary);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM employees
# MAGIC WHERE salary NOT BETWEEN 30000 AND 50000;