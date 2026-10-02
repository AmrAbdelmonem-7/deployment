from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def clean_data(df):
    return (
        df.filter((col("amount") > 0) & (col("name").isNotNull()))
        .withColumn("amount_with_tax", col("amount") * 1.20)
    )