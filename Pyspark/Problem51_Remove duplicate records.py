from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Arun", "IT"),
    (2, "Priya", "HR"),
    (1, "Arun", "IT"),
    (3, "Rahul", "IT"),
    (2, "Priya", "HR")
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "department"]
)

df.show()

result = df.dropDuplicates(["emp_id"])

result.show()
