# Databricks notebook source
# MAGIC %md
# MAGIC ### First Non-Repeating Element

# COMMAND ----------

numbers = [4, 5, 4, 6, 5, 7, 6]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num in numbers:
    if frequency[num] == 1:
        print(num)
        break