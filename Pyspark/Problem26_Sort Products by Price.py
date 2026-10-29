# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Laptop", 55000),
    (102, "Mouse", 800),
    (103, "Keyboard", 1500),
    (104, "Monitor", 12000),
    (105, "USB Cable", 400)
]

columns = ["product_id", "product_name", "price"]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

df_sorted = df.orderBy(F.col("price").asc())

display(df_sorted)