from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Laptop", 2, 45000),
    (102, "Mouse", 3, 500),
    (103, "Keyboard", 2, 1200),
    (104, "Monitor", 1, 12000)
]

df = spark.createDataFrame(
    data,
    ["order_id", "product", "quantity", "unit_price"]
)

df.show()
