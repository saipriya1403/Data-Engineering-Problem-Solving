# Databricks notebook source
from pyspark.sql import functions as F

employees = [
    (1, "Arun", 30000),
    (2, "Priya", 40000),
    (3, "Kumar", 50000),
    (4, "Divya", 60000)
 ]

columns = ["EmployeeId", "EmployeeName", "Salary"]

df = spark.createDataFrame(employees, columns)

display(df)

# COMMAND ----------

bonus_df = df.withColumn(
        "Bonus",
            F.col("Salary") * 0.10
            )

display(bonus_df)
