# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun', 'IT'),
# MAGIC     (2, 'Priya', 'Data'),
# MAGIC     (3, 'Kumar', 'IT'),
# MAGIC     (4, 'Divya', 'HR'),
# MAGIC     (5, 'Meena', 'Data'),
# MAGIC     (6, 'Rohit', 'HR')
# MAGIC AS employees(EmployeeId, EmployeeName, Department);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC EmployeeId,
# MAGIC EmployeeName,
# MAGIC Department
# MAGIC FROM employees
# MAGIC WHERE LOWER(EmployeeName) LIKE '%a%';