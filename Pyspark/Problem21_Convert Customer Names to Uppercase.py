# Databricks notebook source
from pyspark.sql import functions as F

customers = [
    (1, "Arun", "Chennai"),
    (2, "Priya", "Bangalore"),
    (3, "Kumar", "Salem"),
    (4, "Divya", "Trichy")
]

columns = ["CustomerId", "CustomerName", "City"]

df = spark.createDataFrame(customers, columns)

display(df)

# COMMAND ----------

updated_df = df.withColumn(
        "CustomerName",
            F.upper(F.col("CustomerName"))
            )

display(updated_df)
