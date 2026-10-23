# Databricks notebook source
customers = [
    (1, "Arun", "Chennai"),
    (2, "Priya", None),
    (3, "Kumar", "Salem"),
    (4, "Divya", None),
    (5, "Meena", "Madurai")
]

columns = ["CustomerId", "CustomerName", "City"]

df = spark.createDataFrame(customers, columns)

display(df)


# COMMAND ----------

cleaned_df = df.fillna({
        "City": "Unknown"
        })

display(cleaned_df)
