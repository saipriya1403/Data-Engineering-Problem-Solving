# Databricks notebook source
# MAGIC %md
# MAGIC # Find the first non-repeating character

# COMMAND ----------

text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char in text:
    if frequency[char] == 1:
        print(char)
        break