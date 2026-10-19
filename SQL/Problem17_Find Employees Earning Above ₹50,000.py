# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun', 'IT', 45000),
# MAGIC     (2, 'Priya', 'Data', 60000),
# MAGIC     (3, 'Kumar', 'IT', 55000),
# MAGIC     (4, 'Divya', 'HR', 40000),
# MAGIC     (5, 'Meena', 'Data', 70000)
# MAGIC AS employees(EmployeeId, EmployeeName, Department, Salary);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC EmployeeId,
# MAGIC EmployeeName,
# MAGIC Department,
# MAGIC Salary
# MAGIC FROM employees
# MAGIC WHERE Salary > 50000;