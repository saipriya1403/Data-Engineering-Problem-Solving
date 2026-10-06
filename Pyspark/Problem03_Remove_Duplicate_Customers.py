# Databricks notebook source
# MAGIC %md
# MAGIC ### Remove Duplicate Customers

# COMMAND ----------

from pyspark.sql import functions as F

customers = [
    (1, "Arun", "Chennai"),
    (2, "Priya", "Bangalore"),
    (1, "Arun", "Chennai"),
    (3, "Kumar", "Salem"),
    (2, "Priya", "Bangalore")
]

columns = ["CustomerId", "CustomerName", "City"]

df = spark.createDataFrame(customers, columns)

display(df)

# COMMAND ----------

unique_customers = df.dropDuplicates(["CustomerId"])

display(unique_customers)