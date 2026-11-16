from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Priya", 30000),
    (2, None, 40000),
    (3, "Rahul", 35000),
    (4, None, 45000),
    (5, "Anjali", 50000)
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "salary"]
)

print("Original Data:")
df.show()

result = df.dropna(subset=["emp_name"])

print("Updated Data:")
result.show()
