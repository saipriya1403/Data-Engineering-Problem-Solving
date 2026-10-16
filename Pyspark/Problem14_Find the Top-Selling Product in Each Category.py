# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.window import Window

sales = [
    (101, "Laptop", "Electronics", 5),
    (102, "Mobile", "Electronics", 10),
    (101, "Laptop", "Electronics", 8),
    (102, "Mobile", "Electronics", 6),
    (103, "Shirt", "Clothing", 15),
    (104, "Jeans", "Clothing", 12),
    (103, "Shirt", "Clothing", 10),
    (105, "Chair", "Furniture", 7),
    (106, "Table", "Furniture", 9)
                                    ]

columns = [
    "ProductId",
    "ProductName",
    "Category",
    "Quantity"
 ]

df = spark.createDataFrame(sales, columns)

display(df)

# COMMAND ----------

product_sales = (
    df
    .groupBy(
    "ProductId",
    "ProductName",
    "Category"
)
   .agg(
    F.sum("Quantity").alias("TotalQuantity")
    )
    )

display(product_sales)


# COMMAND ----------

window_spec = (
    Window
   .partitionBy("Category")
   .orderBy(F.col("TotalQuantity").desc())
)

ranked_products = (
    product_sales
   .withColumn(
    "rank",
    F.dense_rank().over(window_spec)
)
)

display(ranked_products)


# COMMAND ----------

top_products = (
    ranked_products
    .filter(F.col("rank") == 1)
    .drop("rank")
    .orderBy("Category")
)

display(top_products)
