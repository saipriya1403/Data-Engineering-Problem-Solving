from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", "IT"),
    (102, "Priya", "HR"),
    (103, "Rahul", "IT"),
    (104, "Sneha", "Finance"),
    (105, "Kiran", "IT"),
    (106, "Meena", "HR")
]

columns = ["emp_id", "emp_name", "department"]

df = spark.createDataFrame(data, columns)

display(df)

df_result = df.groupBy("department").agg(
    count("*").alias("employee_count")
)

display(df_result)
