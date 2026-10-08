# Databricks notebook source
# MAGIC %md
# MAGIC ## Find customers whose total spending exceeds ₹5,000

# COMMAND ----------

from pyspark.sql import functions as F

orders = [
    (1, "Arun", 2000),
    (2, "Priya", 3000),
    (3, "Arun", 4000),
    (4, "Kumar", 1500),
    (5, "Priya", 3500),
    (6, "Kumar", 2000)
]

columns = ["OrderId", "CustomerName", "Amount"]

df = spark.createDataFrame(orders, columns)

display(df)

# COMMAND ----------

customer_totals = (
        df.groupBy("CustomerName")
        .agg(F.sum("Amount").alias("TotalSpending"))
        .filter(F.col("TotalSpending") > 5000)
                )

display(customer_totals)
