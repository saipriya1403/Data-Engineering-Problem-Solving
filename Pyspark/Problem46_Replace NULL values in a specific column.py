from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Priya", "IT"),
    (2, "Rahul", None),
    (3, "Anjali", "HR"),
    (4, "Kumar", None)
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "department"]
)

print("Original Data:")
df.show()

result = df.fillna(
    {"department": "Not Assigned"}
)

print("Updated Data:")
result.show()
