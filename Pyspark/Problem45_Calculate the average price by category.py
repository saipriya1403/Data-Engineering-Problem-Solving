from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.getOrCreate()

data = [
    ("Laptop", "Electronics", 50000),
    ("Mobile", "Electronics", 30000),
    ("Shirt", "Clothing", 1000),
    ("Jeans", "Clothing", 2000),
    ("Tablet", "Electronics", 20000)
]

df = spark.createDataFrame(
    data,
    ["product_name", "category", "price"]
)

print("Original Data:")
df.show()

result = df.groupBy("category").agg(
    avg("price").alias("average_price")
)

print("Average Price by Category:")
result.show()
