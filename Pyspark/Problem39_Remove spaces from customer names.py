from pyspark.sql import SparkSession
from pyspark.sql.functions import trim, col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "  Priya  "),
    (2, " Rahul "),
    (3, "  Anjali")
]

df = spark.createDataFrame(
    data,
    ["customer_id", "customer_name"]
)

print("Original Data:")
df.show()

result = df.withColumn(
    "customer_name",
    trim(col("customer_name"))
)

print("Updated Data:")
result.show()
