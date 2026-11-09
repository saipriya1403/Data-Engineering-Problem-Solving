from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "2026-01-15"),
    (2, "2025-06-20"),
    (3, "2024-11-10")
]

df = spark.createDataFrame(
    data,
    ["order_id", "order_date"]
)

df = df.withColumn(
    "order_date",
    col("order_date").cast("date")
)

df.show()

result = df.withColumn(
    "order_year",
    year(col("order_date"))
)

result.show()


