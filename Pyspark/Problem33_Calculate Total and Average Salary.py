from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", 40000),
    (102, "Priya", 50000),
    (103, "Rahul", 60000),
    (104, "Sneha", 45000)
]

columns = ["emp_id", "emp_name", "salary"]

df = spark.createDataFrame(data, columns)

display(df)

df_result = df.agg(
    sum("salary").alias("total_salary"),
    avg("salary").alias("average_salary")
)

display(df_result)
