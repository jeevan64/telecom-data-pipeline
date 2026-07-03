from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os

# Fix for Windows Hadoop warning
os.environ["HADOOP_HOME"] = "C:\\Users\\Admin\\hadoop"

# Start Spark session
spark = SparkSession.builder \
    .appName("TelecomPipeline") \
    .getOrCreate()

print("Loading data...")

customers = spark.read.csv(
    "C:/Users/Admin/OneDrive/Desktop/telecom_data_pipeline/data/processed/customers_clean.csv",
    header=True, inferSchema=True
)

usage = spark.read.csv(
    "C:/Users/Admin/OneDrive/Desktop/telecom_data_pipeline/data/processed/usage_clean.csv",
    header=True, inferSchema=True
)

recharge = spark.read.csv(
    "C:/Users/Admin/OneDrive/Desktop/telecom_data_pipeline/data/processed/recharge_clean.csv",
    header=True, inferSchema=True
)

print("Transforming data...")

# Join datasets
df = customers.join(usage, "customer_id") \
              .join(recharge, "customer_id")

# Add calculated columns
df = df.withColumn("total_usage", col("call_minutes") + col("data_mb")) \
       .withColumn("revenue", col("amount"))

print("Saving output...")

# Save as SINGLE CSV (important)
output_path = "C:/Users/Admin/OneDrive/Desktop/telecom_data_pipeline/data/processed/final_spark_output.csv"
df.toPandas().to_csv(output_path, index=False)

print("Saved to:", output_path)
print("Done")

spark.stop()