from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col

spark = SparkSession.builder.getOrCreate()

data = [
    ("Laptop", 2),
    ("Mobile", 3),
    ("Laptop", 1),
    ("Tablet", 4),
    ("Mobile", 2)
]

df = spark.createDataFrame(
    data,
    ["product_name", "quantity"]
)

print("Original Data:")
df.show()

result = df.groupBy("product_name").agg(
    sum("quantity").alias("total_quantity")
)

print("Total Quantity:")
result.show()
