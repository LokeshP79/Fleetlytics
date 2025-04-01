import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Load trip data
trip_df = spark.read.csv("s3://fleetlytics-data/trip_logs.csv", header=True, inferSchema=True)

# Transformations
trip_df = trip_df.withColumnRenamed("start_time", "trip_start_time") \
                 .withColumnRenamed("end_time", "trip_end_time")

# Save curated data
trip_df.write.mode("overwrite").parquet("s3://fleetlytics-curated/trips/")
