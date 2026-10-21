# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun', 'IT'),
# MAGIC     (2, 'Priya', 'Data'),
# MAGIC     (3, 'Anu', 'HR'),
# MAGIC     (4, 'Kumar', 'IT'),
# MAGIC     (5, 'Ajay', 'Data'),
# MAGIC     (6, 'Divya', 'HR')
# MAGIC AS employees(EmployeeId, EmployeeName, Department);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC EmployeeId,
# MAGIC EmployeeName,
# MAGIC Department
# MAGIC FROM employees
# MAGIC WHERE EmployeeName LIKE 'A%';