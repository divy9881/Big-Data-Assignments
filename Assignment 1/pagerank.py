import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

def pagerank(spark, input_file_path):
    df = sc.textFile(input_file_path)
    
    links = df.map(lambda line: tuple(line.split("\t")))
    print(links)
    # links = df.rdd.map(lambda row: (row[0], row[1]))

    # ranks = links.map(lambda pair: (pair[0], 1.0))
    # ranks.foreach(print)
    # ranks = dict()
    # for link in links:
    #     if link[0] not in ranks:
    #         ranks[link[0]] = 1.0

    # for iteration in range(10):
    #     contributions = links.join(ranks).flatMap(
    #         lambda page_links_rank: [(link, page_links_rank[1][1] / len(page_links_rank[1][0])) for link in page_links_rank[1][0]])
        
    #     ranks = contributions.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: 0.15 + 0.85 * rank)

    # final_ranks = ranks.collect()
    # for page, rank in final_ranks:
    #     print(f"Page: {page}, Rank: {rank}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark-submit <script.py> <input_path>")
        sys.exit(1)

    conf = SparkConf().setAppName("Big-Data-Assignment-1-Part-3") \
                            .set("spark.driver.memory", "30g") \
                            .set("spark.executor.memory", "30g") \
                            .set("spark.executor.cores", "5") \
                            .set("spark.executor.cpus", "1")

    sc = SparkContext(conf=conf)
    spark = SparkSession(sc)

    input_path = sys.argv[1]
    
    pagerank(spark, input_path)

    sc.stop()