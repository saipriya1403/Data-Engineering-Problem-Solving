# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC (101, 'Arun', 201),
# MAGIC (102, 'Priya', NULL),
# MAGIC (103, 'Rahul', 202),
# MAGIC (104, 'Sneha', NULL),
# MAGIC (105, 'Kiran', 201)
# MAGIC AS employees(emp_id, emp_name, manager_id);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM employees
# MAGIC WHERE manager_id IS NULL;