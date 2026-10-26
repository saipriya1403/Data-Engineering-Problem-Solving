# Databricks notebook source
from pyspark.sql import functions as F

customers = [
    (1, " Arun "),
    (2, "Priya  "),
    (3, "  Kumar"),
    (4, " Divya ")
]

columns = ["CustomerId", "CustomerName"]

df = spark.createDataFrame(customers, columns)

display(df)

# COMMAND ----------

cleaned_df = df.withColumn(
        "CustomerName",
            F.trim(F.col("CustomerName"))
            )

display(cleaned_df)
