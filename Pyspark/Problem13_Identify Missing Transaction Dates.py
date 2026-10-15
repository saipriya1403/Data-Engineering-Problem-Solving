# Databricks notebook source
from pyspark.sql import functions as F

transactions = [
    (1, "Arun", "2026-10-01"),
    (2, "Arun", "2026-10-04"),
    (3, "Arun", "2026-10-06"),
    (4, "Priya", "2026-10-02"),
    (5, "Priya", "2026-10-05"),
    (6, "Kumar", "2026-10-01"),
    (7, "Kumar", "2026-10-02")
]

columns = ["TransactionId", "CustomerName", "TransactionDate"]

df = spark.createDataFrame(transactions, columns)

df = df.withColumn(
   "TransactionDate",
    F.to_date("TransactionDate")
)

display(df)

# COMMAND ----------

date_range_df = (
    df.groupBy("CustomerName")
    .agg(
    F.min("TransactionDate").alias("StartDate"),
    F.max("TransactionDate").alias("EndDate")
 )
)

display(date_range_df)


# COMMAND ----------

all_dates_df = (
    date_range_df
    .withColumn(
    "TransactionDate",
    F.explode(
    F.sequence("StartDate", "EndDate")
)
)
.select("CustomerName", "TransactionDate")
)

display(all_dates_df)
                                                        


# COMMAND ----------

missing_dates_df = (
    all_dates_df
    .join(
    df.select(
    "CustomerName",
    "TransactionDate"
    ).distinct(),
    on=["CustomerName", "TransactionDate"],
    how="left_anti"
    )
    .orderBy("CustomerName", "TransactionDate")
)

display(missing_dates_df)
