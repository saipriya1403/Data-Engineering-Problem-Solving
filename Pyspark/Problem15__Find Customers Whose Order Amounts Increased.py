# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.window import Window

orders = [
(101, "Arun", "2026-10-01", 2000),
(102, "Arun", "2026-10-03", 3500),
(103, "Arun", "2026-10-05", 5000),
(104, "Priya", "2026-10-01", 4000),
(105, "Priya", "2026-10-04", 3000),
(106, "Priya", "2026-10-06", 4500),
(107, "Kumar", "2026-10-02", 5000),
(108, "Kumar", "2026-10-05", 4000)
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

previous_orders = (
    df
    .withColumn(
    "PreviousAmount",
    F.lag("Amount").over(window_spec)
)
)

display(previous_orders)


# COMMAND ----------

increased_orders = (
    previous_orders
    .filter(
    F.col("Amount") > F.col("PreviousAmount")
)
    .withColumn(
    "IncreaseAmount",
    F.col("Amount") - F.col("PreviousAmount")
    )
    .orderBy("CustomerName", "OrderDate")
)

display(increased_orders)
