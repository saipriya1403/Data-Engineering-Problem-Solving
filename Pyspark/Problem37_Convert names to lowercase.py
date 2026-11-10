from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "PRIYA"),
    (2, "RAHUL"),
    (3, "ANJALI")
]

df = spark.createDataFrame(
    data,
    ["customer_id", "customer_name"]
)

print("Original Data:")
df.show()

result = df.withColumn(
    "customer_name",
    lower(col("customer_name"))
)

print("Updated Data:")
result.show()
