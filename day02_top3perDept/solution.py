from pyspark.sql import Window
from pyspark.sql.functions import col, row_number

# define the window specification
windowSpec = Window.partitionBy("department_id") \
    .orderBy(col("salary").desc())

# Apply row_number() and filter for top 3
top_earners_df = (
    employee_df \
    .withColumn("row_num", row_number().over(windowSpec))\
    .filter(col("row_num") <= 3)
    .drop("row_num")
)

top_earners_df.show()