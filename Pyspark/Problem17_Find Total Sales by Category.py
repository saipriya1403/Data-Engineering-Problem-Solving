# Databricks notebook source
from pyspark.sql import functions as F

sales = [
    (1, "Laptop", "Electronics", 50000),
    (2, "Mobile", "Electronics", 20000),
    (3, "Shirt", "Clothing", 1500),
    (4, "Jeans", "Clothing", 2500),
    (5, "Chair", "Furniture", 5000)
]

columns = ["ProductId", "ProductName", "Category", "Amount"]

df = spark.createDataFrame(sales, columns)

display(df)

# COMMAND ----------

total_sales = (
    df.groupBy("Category")
    .agg(F.sum("Amount").alias("TotalSales"))
)

display(total_sales)
