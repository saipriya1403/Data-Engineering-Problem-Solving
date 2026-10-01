# Databricks notebook source
from pyspark.sql import functions as F

transactions = [
    ("Arun", 1000),
    ("Priya", 2000),
    ("Arun", 1500),
    ("Kumar", 3000),
    ("Priya", 1000),
    ("Arun", 500)
]

columns = ["CustomerName", "Amount"]

df = spark.createDataFrame(transactions, columns)

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Aggregate by Customer

# COMMAND ----------

customer_total = (
    df
    .groupBy("CustomerName")
    .agg(
    F.sum("Amount").alias("TotalAmount")
    )
    )

display(customer_total)
