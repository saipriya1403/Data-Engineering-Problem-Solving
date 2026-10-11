# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.window import Window

orders = [
    (101, "Arun", "2026-10-01", 2000),
    (102, "Arun", "2026-10-03", 3000),
    (103, "Arun", "2026-10-05", 1500),
    (104, "Priya", "2026-10-01", 4000),
    (105, "Priya", "2026-10-04", 2000),
    (106, "Kumar", "2026-10-02", 5000),
    (107, "Kumar", "2026-10-06", 3000)
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
    .rowsBetween(
        Window.unboundedPreceding,
        Window.currentRow
    )
    )

running_total_df = (
        df
        .withColumn(
        "RunningTotal",
        F.sum("Amount").over(window_spec)
    )
.orderBy("CustomerName", "OrderDate", "OrderId")
)

display(running_total_df)
