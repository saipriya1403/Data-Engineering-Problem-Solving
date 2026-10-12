# Databricks notebook source
from pyspark.sql import functions as F

target_data = [
    (1, "Arun", "Chennai"),
    (2, "Priya", "Bangalore"),
    (3, "Kumar", "Salem")
]

source_data = [
    (1, "Arun", "Chennai"),
    (2, "Priya", "Coimbatore"),
    (3, "Kumar", "Salem"),
    (4, "Divya", "Trichy")
]

columns = ["CustomerId", "CustomerName", "City"]

target_df = spark.createDataFrame(target_data, columns)
source_df = spark.createDataFrame(source_data, columns)

display(target_df)
display(source_df)

# COMMAND ----------

new_customers = source_df.join(
        target_df,
            on="CustomerId",
                how="left_anti"
                )

display(new_customers)
