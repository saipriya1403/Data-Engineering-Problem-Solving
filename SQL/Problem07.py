# Databricks notebook source
# MAGIC %md
# MAGIC # Find employees earning more than their department's average

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC (1, 'Arun', 'Data', 60000),
# MAGIC (2, 'Priya', 'Data', 80000),
# MAGIC (3, 'Kumar', 'IT', 90000),
# MAGIC (4, 'Meena', 'IT', 70000),
# MAGIC (5, 'Ravi', 'HR', 50000),
# MAGIC (6, 'Divya', 'HR', 65000)
# MAGIC AS employees(EmployeeId, EmployeeName, Department, Salary);

# COMMAND ----------

# MAGIC %sql
# MAGIC select EmployeeId,EmployeeName,Department, Salary
# MAGIC From (
# MAGIC     select * ,avg(Salary) over(partition by 
# MAGIC     Department) as department_avgsalary
# MAGIC     from employees
# MAGIC )
# MAGIC where Salary > department_avgsalary
# MAGIC