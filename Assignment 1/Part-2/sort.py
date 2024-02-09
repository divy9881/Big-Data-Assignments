import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


"""
    Function to read CSV data from input_path, sort it by 'cca2' (Country Code) and 'timestamp' (Timestamp) columns,
    and write the sorted data to output_path.
    
    Args:
        input_path (str): Path to the input CSV file.
        output_path (str): Path to write the sorted CSV file.
"""
def sort_data(input_path, output_path):
    # Read CSV data
    data = spark_app.read.csv(input_path, header=True, inferSchema=True)

    # Sort data by 'cca2' and 'timestamp'
    sorted_data = data.orderBy(col("cca2"), col("timestamp"))

    # Write sorted data to a single output CSV file
    sorted_data.coalesce(1).write.mode('overwrite').csv(output_path, header=True)

if __name__ == "__main__":
    # Setup Spark Application config
    spark_app = SparkSession.builder \
        .appName("Big-Data-Assignment-1-Part-2") \
        .config("spark.driver.memory", "30g") \
        .config("spark.executor.memory", "30g") \
        .config("spark.executor.cores", "5") \
        .config("spark.task.cpus", "1") \
        .getOrCreate()

    # Proper usage check
    if len(sys.argv) != 3:
        print("Usage: spark-submit <script.py> <input_path> <output_path>")
        sys.exit(1)

    # Extract path to input and output CSV files from command-line arguments
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Generate sorted data
    sort_data(input_path, output_path)

    # Stop Spark application
    spark_app.stop()