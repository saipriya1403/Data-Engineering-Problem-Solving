# Databricks notebook source
from pyspark.sql import functions as F

customers = [
    (1, "Arun", 22),
    (2, "Priya", 28),
    (3, "Kumar", 30),
    (4, "Divya", 24),
    (5, "Meena", 35)
]

columns = ["CustomerId", "CustomerName", "Age"]

df = spark.createDataFrame(customers, columns)

display(df)

# COMMAND ----------

filtered_customers = df.filter(F.col("Age") > 25)

display(filtered_customers)