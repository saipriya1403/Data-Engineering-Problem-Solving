from pyspark.sql import SparkSession
from pyspark.sql.functions import min, max

spark = SparkSession.builder.getOrCreate()

data = [
    (1, "Arun", "IT", 60000),
    (2, "Priya", "IT", 80000),
    (3, "Rahul", "IT", 70000),
    (4, "Divya", "HR", 50000),
    (5, "Kumar", "HR", 65000),
    (6, "Meena", "HR", 45000)
]

df = spark.createDataFrame(
    data,
    ["emp_id", "emp_name", "department", "salary"]
)

df.show()

from pyspark.sql.functions import min, max

result = (
    df.groupBy("department")
      .agg(
          min("salary").alias("minimum_salary"),
          max("salary").alias("maximum_salary")
      )
)

result.show()
