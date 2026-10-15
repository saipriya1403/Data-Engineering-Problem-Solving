# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC     (1, 'Arun', 'Data', 90000, NULL),
# MAGIC     (2, 'Priya', 'Data', 95000, 1),
# MAGIC     (3, 'Kumar', 'Data', 70000, 1),
# MAGIC     (4, 'Meena', 'IT', 100000, NULL),
# MAGIC     (5, 'Ravi', 'IT', 110000, 4),
# MAGIC     (6, 'Divya', 'IT', 80000, 4),
# MAGIC     (7, 'Suresh', 'HR', 75000, NULL),
# MAGIC     (8, 'Kavya', 'HR', 85000, 7)
# MAGIC  AS employees(EmployeeId, EmployeeName, Department, Salary, ManagerId);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC e.EmployeeId,
# MAGIC e.EmployeeName,
# MAGIC e.Department,
# MAGIC e.Salary AS EmployeeSalary,
# MAGIC m.EmployeeName AS ManagerName,
# MAGIC m.Salary AS ManagerSalary
# MAGIC FROM employees e
# MAGIC INNER JOIN employees m
# MAGIC ON e.ManagerId = m.EmployeeId
# MAGIC WHERE e.Salary > m.Salary;