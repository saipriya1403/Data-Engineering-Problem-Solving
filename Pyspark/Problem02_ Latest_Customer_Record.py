# Databricks notebook source
# MAGIC %md
# MAGIC ### Latest Customer Record

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.window import Window

customers = [
    (1, "Arun", "Chennai", "2026-09-01 09:00:00"),
    (1, "Arun Kumar", "Coimbatore", "2026-09-03 10:00:00"),
    (2, "Priya", "Bangalore", "2026-09-02 09:00:00"),
    (2, "Priya", "Chennai", "2026-09-04 11:00:00"),
    (3, "Kumar", "Salem", "2026-09-01 08:00:00")
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
    .withColumn("row_num", F.row_number().over(window_spec))
    .filter(F.col("row_num") == 1)
    .drop("row_num")
)

display(latest_customers)
