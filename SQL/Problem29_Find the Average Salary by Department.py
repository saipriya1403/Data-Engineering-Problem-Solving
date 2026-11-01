# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW employees AS
# MAGIC SELECT * FROM VALUES
# MAGIC (101, 'Arun', 'IT', 40000),
# MAGIC (102, 'Priya', 'HR', 50000),
# MAGIC (103, 'Rahul', 'IT', 60000),
# MAGIC (104, 'Sneha', 'HR', 45000),
# MAGIC (105, 'Kiran', 'Finance', 55000)
# MAGIC AS employees(emp_id, emp_name, department, salary);

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC department,
# MAGIC AVG(salary) AS average_salary
# MAGIC FROM employees
# MAGIC GROUP BY department;