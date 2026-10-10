# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.window import Window

customers = [
    (1, "Arun", "Chennai", "2026-10-01 09:00:00"),
    (1, "Arun Kumar", "Coimbatore", "2026-10-05 10:00:00"),
    (2, "Priya", "Bangalore", "2026-10-02 11:00:00"),
    (2, "Priya", "Chennai", "2026-10-06 12:00:00"),
    (3, "Kumar", "Salem", "2026-10-03 08:00:00")
]

columns = ["CustomerId", "CustomerName", "City", "UpdatedAt"]

df = spark.createDataFrame(customers, columns)

df = df.withColumn(
    "UpdatedAt",
    F.to_timestamp("UpdatedAt")
)

display(df)

# COMMAND ----------

window_spec = (
    Window
    .partitionBy("CustomerId")
    .orderBy(F.col("UpdatedAt").desc())
)

latest_customers = (
    df
    .withColumn("rn", F.row_number().over(window_spec))
    .filter(F.col("rn") == 1)
    .drop("rn")
)

display(latest_customers)
