# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Arun", "Kumar"),
    (2, "Priya", "Sharma"),
    (3, "Rahul", "Raj"),
    (4, "Sneha", "Reddy")
]

columns = ["id", "first_name", "last_name"]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

df_new = df.withColumn(
    "full_name",
    F.concat_ws(" ", F.col("first_name"), F.col("last_name"))
)

display(df_new)
