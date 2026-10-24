# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun', '2024-06-15'),
# MAGIC     (2, 'Priya', '2025-01-10'),
# MAGIC     (3, 'Kumar', '2025-08-20'),
# MAGIC     (4, 'Divya', '2026-02-05'),
# MAGIC     (5, 'Meena', '2025-11-12')
# MAGIC AS employees(EmployeeId, EmployeeName, JoiningDate);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC EmployeeId,
# MAGIC EmployeeName,
# MAGIC JoiningDate
# MAGIC FROM employees
# MAGIC WHERE YEAR(TO_DATE(JoiningDate)) = 2025;