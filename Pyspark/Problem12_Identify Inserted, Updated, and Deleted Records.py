# Databricks notebook source
from pyspark.sql import functions as F

target_data = [
    (1, "Arun", "Chennai"),
    (2, "Priya", "Bangalore"),
    (3, "Kumar", "Salem"),
    (4, "Meena", "Madurai")
]

source_data = [
    (1, "Arun", "Chennai"),
    (2, "Priya", "Coimbatore"),
    (3, "Kumar", "Salem"),
    (5, "Divya", "Trichy")
]

columns = ["CustomerId", "CustomerName", "City"]

target_df = spark.createDataFrame(target_data, columns)
source_df = spark.createDataFrame(source_data, columns)

display(target_df)
display(source_df)

# COMMAND ----------

changes_df = (
    source_df.alias("s")
    .join(
       target_df.alias("t"),
       F.col("s.CustomerId") == F.col("t.CustomerId"),
       "full_outer"
)

    .select(
       F.coalesce(
       F.col("s.CustomerId"),
       F.col("t.CustomerId")
    ).alias("CustomerId"),

    F.coalesce(
        F.col("s.CustomerName"),
        F.col("t.CustomerName")
       ).alias("CustomerName"),
    F.coalesce(
        F.col("s.City"),
        F.col("t.City")
       ).alias("City"),
    F.when(
        F.col("t.CustomerId").isNull(),
       "INSERT"
     ).when(
        F.col("s.CustomerId").isNull(),
        "DELETE"
     ).when(
        ~F.col("s.CustomerName").eqNullSafe(F.col("t.CustomerName")) |
        ~F.col("s.City").eqNullSafe(F.col("t.City")),
        "UPDATE"
     ).otherwise("NO CHANGE").alias("ChangeType")

    )       
)
display(changes_df.orderBy("CustomerId"))
    
    