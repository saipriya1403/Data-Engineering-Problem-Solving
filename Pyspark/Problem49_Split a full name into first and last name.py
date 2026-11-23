from pyspark.sql import SparkSession
from pyspark.sql.functions import split, col

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Arun Kumar"),
    (2, "Priya Sharma"),
    (3, "Rahul Verma")
]

df = spark.createDataFrame(
    data,
    ["emp_id", "full_name"]
)

df.show()
