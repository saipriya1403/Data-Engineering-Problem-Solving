from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, max

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Priya", "IT", 50000),
    (2, "Rahul", "HR", 40000),
    (3, "Anjali", "IT", 60000),
    (4, "Kumar", "HR", 35000),
    (5, "Divya", "Finance", 45000)
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "department", "salary"]
)

print("Original Data:")
df.show()

result = df.groupBy("department").agg(
    sum("salary").alias("total_salary"),
    max("salary").alias("maximum_salary")
)

print("Department Salary Summary:")
result.show()
