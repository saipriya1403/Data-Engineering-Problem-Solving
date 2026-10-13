# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.window import Window

orders = [
    (101, "Arun", "2026-10-01", 2000),
    (102, "Arun", "2026-10-03", 3500),
    (103, "Arun", "2026-10-05", 2500),
    (104, "Priya", "2026-10-01", 4000),
    (105, "Priya", "2026-10-04", 6000),
    (106, "Kumar", "2026-10-02", 3000),
    (107, "Kumar", "2026-10-06", 4500)
]

columns = ["OrderId", "CustomerName", "OrderDate", "Amount"]

df = spark.createDataFrame(orders, columns)

df = df.withColumn(
    "OrderDate",
    F.to_date("OrderDate")
    )

display(df)

# COMMAND ----------

window_spec = (
    Window
    .partitionBy("CustomerName")
    .orderBy("OrderDate", "OrderId")
)

result_df = (
    df
    .withColumn(
    "PreviousAmount",
    F.lag("Amount").over(window_spec)
)
    .withColumn(
    "AmountDifference",
    F.col("Amount") - F.col("PreviousAmount")
    )
    .orderBy("CustomerName", "OrderDate", "OrderId")
    )

display(result_df)
