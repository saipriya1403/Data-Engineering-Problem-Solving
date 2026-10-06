# Databricks notebook source
# MAGIC %md
# MAGIC ### Second Largest Unique Number

# COMMAND ----------

numbers = [10, 20, 5, 20, 30, 10, 40, 30]

unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)

second_largest = unique_numbers[1]

print(second_largest)