# Databricks notebook source
# MAGIC %md
# MAGIC ## Find the top 2 highest-spending customers

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window

orders = [
    (1, "Arun", 2000),
    (2, "Priya", 5000),
    (3, "Arun", 4000),
    (4, "Kumar", 3000),
    (5, "Priya", 2000),
    (6, "Kumar", 6000),
    (7, "Divya", 7000)
]

columns = ["OrderId", "CustomerName", "Amount"]

df = spark.createDataFrame(orders, columns)
display(df)

# COMMAND ----------

customer_totals = (
    df.groupBy("CustomerName")
    .agg(F.sum("Amount").alias("TotalSpending"))
)

window_spec = Window.orderBy(F.col("TotalSpending").desc())

top_customers = (
    customer_totals
    .withColumn("rank", F.row_number().over(window_spec))
    .filter(F.col("rank") <= 2)
    .drop("rank")
)

display(top_customers)
