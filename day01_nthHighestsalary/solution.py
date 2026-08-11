from pyspark.sql import Window
from pyspark.sql.functions import col, dense_rank

# Load CSV using PySpark DataFrame API
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv("data/day01_employees.csv")

# Register as a temporary SQL view
df.createOrReplaceTempView("employees")

#define window specification
windowSpec = Window.orderBy(col("salary").desc())

#Find Nth Highest Salary
n = 2
nth_salary_df = df \
        .withCOlumn("rank",dense_rank().over(windowSpec)) \
        .filter(col("rank") == 2) \
        .drop("rank")