import pytest
from pyspark.sql import SparkSession
from pyspark_job import clean_data

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[1]").appName("PySparkTesting").getOrCreate()

def test_clean_data(spark):
    sample_data = [
        (1, 100.0, "Ahmed"),
        (2, -50.0, "Sara"),
        (3, 200.0, None),
        (4, 0.0, "Omar")
    ]
    columns = ["order_id", "amount", "name"]
    df = spark.createDataFrame(sample_data, columns)

    cleaned_df = clean_data(df)
    results = cleaned_df.collect()

   
    assert len(results) == 1
    assert results[0]["order_id"] == 1

    assert results[0]["amount_with_tax"] == 120.0