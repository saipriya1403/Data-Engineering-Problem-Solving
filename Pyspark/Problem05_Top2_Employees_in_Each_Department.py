# Databricks notebook source
from pyspark.sql import functions as F
from pyspark.sql.window import Window

employees = [
    (1, "Arun", "Data", 60000),
    (2, "Priya", "Data", 75000),
    (3, "Kumar", "IT", 90000),
    (4, "Meena", "HR", 75000),
    (5, "Ravi", "IT", 85000),
    (6, "Divya", "Data", 80000),
    (7, "Suresh", "IT", 70000),
    (8, "Kavya", "HR", 65000)
                                ]

columns = [
    "EmployeeId",
    "EmployeeName",
    "Department",
    "Salary"
]

df = spark.createDataFrame(employees, columns)

display(df)

# COMMAND ----------

window_spec = (
    Window
    .partitionBy("Department")
    .orderBy(F.col("Salary").desc())
)

top_2 = (
    df
    .withColumn(
    "rank",
    F.row_number().over(window_spec)
   )
    .filter(F.col("rank") <= 2)
    .drop("rank")
)

display(top_2)
