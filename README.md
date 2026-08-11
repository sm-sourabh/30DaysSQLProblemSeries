🚀 30 Days of PySpark & Spark SQL
Welcome to my 30-Day Data Engineering Challenge! This repository contains daily real-world data engineering scenarios patterns, performance optimization techniques, and analytical problems solved using both PySpark DataFrame API and Spark SQL.

Every daily folder includes:

solution.py: The PySpark API implementation.

query.sql: The equivalent Spark SQL query.

Sample Dataset: Located in the centralized data/ folder.

☁️ How to Run These Notebooks on Azure Databricks
Since these examples are built to run on distributed cluster environments, here is how you can quickly set them up and execute them in Azure Databricks (Free Edition):

Step 1: Upload the Datasets to Databricks File System (DBFS) or Unity Catalog or Volume
Log into your Azure Databricks workspace.

Go to Catalog or New > Table (depending on your workspace setup).

Upload the CSV files from the local data/ folder (e.g., day01_employees.csv) to your DBFS or volume path.
(Alternatively, you can read them directly using cloud storage paths if mounted).

Step 2: Import the Solutions into a Databricks Notebook
    Create a new Python/Scala/SQL notebook in Databricks and attach it to an active cluster (e.g., Databricks Runtime 13.3 LTS or higher).

To run the PySpark solutions (solution.py):

Copy the code into a Python cell.

Update the file path to point to your Databricks storage path, for example:
    df = spark.read.option("header", "true").option("inferSchema", "true").csv("/FileStore/tables/day01_employees.csv")

Step 3: To run the Spark SQL solutions (query.sql):

Ensure your DataFrame is registered as a temp view in a Python cell first:
    df.createOrReplaceTempView("employees")

Create a new cell, change its language type to %sql, and paste your SQL query directly!

===========================================

📂 Challenge IndexDayChallenge TopicPySpark SolutionSpark SQL SolutionDataset01The Nth Highest SalaryPython ScriptSQL QueryView Data02Top 3 Earners per DepartmentPython ScriptSQL QueryView Data03Coming Soon...


===========================================

🛠️ Tech Stack

Language: Python, SQL

Big Data Framework: Apache Spark, PySpark, Spark SQL

Cloud Platform: Azure Databricks (Free Edition)