# Databricks notebook source
from pyspark.sql import functions as F

employees = [
    (1, "Arun", 30000),
    (2, "Priya", 45000),
    (3, "Kumar", 65000),
    (4, "Divya", 55000),
    (5, "Meena", 75000)
]

columns = ["EmployeeId", "EmployeeName", "Salary"]

df = spark.createDataFrame(employees, columns)

display(df)

# COMMAND ----------

result_df = df.withColumn(
    "SalaryCategory",
    F.when(F.col("Salary") >= 60000, "High")
    .when(F.col("Salary") >= 40000, "Medium")
   .otherwise("Low")
)

display(result_df)
