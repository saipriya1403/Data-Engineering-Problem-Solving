# Databricks notebook source
from pyspark.sql import functions as F

existing_data = [
    (1, "Arun", "2026-10-10 10:00:00"),
    (1, "Arun", "2026-10-12 12:00:00"),
    (2, "Priya", "2026-10-11 09:00:00"),
    (3, "Kumar", "2026-10-13 14:00:00")
]

incoming_data = [
   (1, "Arun", "2026-10-11 11:00:00"),
   (2, "Priya", "2026-10-14 10:00:00"),
   (3, "Kumar", "2026-10-12 08:00:00"),
   (4, "Divya", "2026-10-15 09:00:00")
]

columns = ["CustomerId", "CustomerName", "EventTime"]

existing_df = spark.createDataFrame(existing_data, columns)
incoming_df = spark.createDataFrame(incoming_data, columns)

existing_df = existing_df.withColumn(
    "EventTime",
    F.to_timestamp("EventTime")
)

incoming_df = incoming_df.withColumn(
    "EventTime",
    F.to_timestamp("EventTime")
    )

display(existing_df)
display(incoming_df)

# COMMAND ----------

latest_events = (
    existing_df
    .groupBy("CustomerId")
    .agg(
    F.max("EventTime").alias("LatestEventTime")
)
)

display(latest_events)


# COMMAND ----------

late_records = (
    incoming_df.alias("i")
    .join(
    latest_events.alias("e"),
    on="CustomerId",
    how="inner"
)
    .filter(
    F.col("i.EventTime") < F.col("e.LatestEventTime")
    )
    .select(
        "CustomerId",
        "CustomerName",
        "EventTime",
        "LatestEventTime"
)
    .orderBy("CustomerId")
)

display(late_records)


# COMMAND ----------

