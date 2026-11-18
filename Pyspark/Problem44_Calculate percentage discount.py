from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Laptop", 50000),
    (2, "Mobile", 30000),
    (3, "Tablet", 20000)
]

df = spark.createDataFrame(
    data,
    ["product_id", "product_name", "price"]
)

print("Original Data:")
df.show()

result = df.withColumn(
    "discount",
    col("price") * 0.10
)

result.show()
