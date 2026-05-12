import subprocess

print("STEP 1: Running Spark transformation...")

subprocess.run([
    "python",
    "../scripts/transform_spark.py"
])

print("Pipeline completed successfully ✅")