from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Priya", 50000),
    (2, "Rahul", 40000),
    (3, "Anjali", 60000)
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "salary"]
)

print("Original Data:")
df.show()

result = df.withColumn(
    "tax",
    col("salary") * 0.05
)

print("Updated Data:")
result.show()
