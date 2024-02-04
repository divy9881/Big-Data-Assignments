import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def generate_sorted_data(input_path, output_path):
    data = spark.read.csv(input_path, header=True, inferSchema=True)

    sorted_data = data.orderBy(col("cca2"), col("timestamp"))
    sorted_data.show()

    sorted_data.coalesce(1).write.mode('overwrite').csv(output_path, header=True)

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Big-Data-Assignment-1") \
        .config("spark.driver.memory", "30g") \
        .config("spark.executor.memory", "30g") \
        .config("spark.executor.cores", "5") \
        .config("spark.task.cpus", "1") \
        .getOrCreate()

    if len(sys.argv) != 3:
        print("Usage: spark-submit <script.py> <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    generate_sorted_data(input_path, output_path)
    spark.stop()