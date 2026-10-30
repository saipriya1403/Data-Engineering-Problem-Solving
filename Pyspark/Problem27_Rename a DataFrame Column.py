# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", "IT"),
    (102, "Priya", "HR"),
    (103, "Rahul", "Finance"),
    (104, "Sneha", "IT")
]

columns = ["emp_id", "emp_name", "department"]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

df_new = df.withColumnRenamed("emp_name", "employee_name")

display(df_new)