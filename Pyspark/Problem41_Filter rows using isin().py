from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Priya", "IT"),
    (2, "Rahul", "HR"),
    (3, "Anjali", "Finance"),
    (4, "Kumar", "IT"),
    (5, "Divya", "Sales")
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "department"]
)

print("Original Data:")
df.show()

result = df.filter(
    col("department").isin("IT", "HR")
)

print("Filtered Data:")
result.show()
