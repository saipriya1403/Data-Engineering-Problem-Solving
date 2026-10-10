# Databricks notebook source
# MAGIC %md
# MAGIC ## Find the missing number

# COMMAND ----------

numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]

n = 10

expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum

print(missing_number)