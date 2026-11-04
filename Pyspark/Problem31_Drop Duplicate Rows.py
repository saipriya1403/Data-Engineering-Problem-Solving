from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = [
    (101, "Arun", "IT"),
    (102, "Priya", "HR"),
    (101, "Arun", "IT"),
    (103, "Rahul", "Finance"),
    (102, "Priya", "HR")
]

columns = ["emp_id", "emp_name", "department"]

df = spark.createDataFrame(data, columns)

display(df)


df_new = df.dropDuplicates(["emp_id"])

display(df_new)
