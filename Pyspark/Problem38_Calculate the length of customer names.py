from pyspark.sql import SparkSession
from pyspark.sql.functions import length, col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Priya"),
    (2, "Rahul"),
    (3, "Anjali"),
    (4, "Kumar")
]

df = spark.createDataFrame(
    data,
    ["customer_id", "customer_name"]
)

print("Original Data:")
df.show()

result = df.withColumn(
    "name_length",
    length(col("customer_name"))
)

print("Updated Data:")
result.show()
