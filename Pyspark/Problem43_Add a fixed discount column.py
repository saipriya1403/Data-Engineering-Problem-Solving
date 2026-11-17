from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

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
    lit(10)
)

print("Updated Data:")
result.show()
