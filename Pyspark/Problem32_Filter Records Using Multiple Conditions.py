from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", "IT", 45000),
    (102, "Priya", "HR", 55000),
    (103, "Rahul", "IT", 35000),
    (104, "Sneha", "IT", 60000),
    (105, "Kiran", "Finance", 50000)
]

columns = ["emp_id", "emp_name", "department", "salary"]

df = spark.createDataFrame(data, columns)

display(df)

df_filtered = df.filter(
    (col("department") == "IT") &
    (col("salary") > 40000)
)

display(df_filtered)
