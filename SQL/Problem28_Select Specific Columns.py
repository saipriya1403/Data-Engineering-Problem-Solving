# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", "IT", 45000),
    (102, "Priya", "HR", 55000),
    (103, "Rahul", "Finance", 40000),
    (104, "Sneha", "IT", 60000)
]

columns = ["emp_id", "emp_name", "department", "salary"]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

df_selected = df.select("emp_name", "salary")

display(df_selected)