from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Arun", "IT", 60000),
    (2, "Priya", "HR", 45000),
    (3, "Rahul", "IT", 75000),
    (4, "Divya", "IT", 40000),
    (5, "Kumar", "Finance", 65000)
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "department", "salary"]
)

df.show()

result = df.filter(
    (col("department") == "IT") &
    (col("salary") > 50000)
)

result.show()
