# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun', 'Data', 60000),
# MAGIC     (2, 'Priya', 'Data', 75000),
# MAGIC     (3, 'Kumar', 'IT', 90000),
# MAGIC     (4, 'Meena', 'HR', 75000),
# MAGIC     (5, 'Ravi', 'IT', 85000),
# MAGIC     (6, 'Divya', 'Data', 60000)
# MAGIC AS employees(EmployeeId, EmployeeName, Department, Salary);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC   EmployeeId,
# MAGIC   EmployeeName,
# MAGIC   Department,
# MAGIC   Salary
# MAGIC FROM employees
# MAGIC WHERE Salary = (
# MAGIC       SELECT MAX(Salary)
# MAGIC       FROM employees
# MAGIC       WHERE Salary < (
# MAGIC       SELECT MAX(Salary)
# MAGIC FROM employees
# MAGIC )
# MAGIC );