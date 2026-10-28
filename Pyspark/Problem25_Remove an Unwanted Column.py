# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", "IT", "9876543210"),
    (102, "Priya", "HR", "9876543211"),
    (103, "Rahul", "Finance", "9876543212"),
    (104, "Sneha", "IT", "9876543213")
]

columns = ["emp_id", "emp_name", "department", "phone_number"]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

df_new = df.drop("phone_number")

display(df_new)