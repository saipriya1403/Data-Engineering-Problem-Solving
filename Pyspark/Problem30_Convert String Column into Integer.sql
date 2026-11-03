from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", "45000"),
    (102, "Priya", "55000"),
    (103, "Rahul", "65000"),
    (104, "Sneha", "50000")
]

columns = ["emp_id", "emp_name", "salary"]

df = spark.createDataFrame(data, columns)

df.printSchema()
display(df)

df_new = df.withColumn(
    "salary",
    col("salary").cast("int")
)

df_new.printSchema()
display(df_new)
