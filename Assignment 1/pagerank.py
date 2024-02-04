import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

lookup = dict()

def filter_lines(line):
    if line.startswith("#"):
        return []
    else:
        return [tuple(line.split("\t"))]
    
def assign_ranks(pair):    
    if pair[0] not in lookup:
        lookup[pair[0]] = True
        return [(pair[0], 1.0)]
    else:
        return []

def pagerank(spark, input_file_path):
    df = sc.textFile(input_file_path)
    
    links = df.flatMap(filter_lines)

    ranks = links.flatMap(assign_ranks)
    print(ranks.count())

    for iteration in range(1):
        links_ranks = links.join(ranks)
        links_r = links_ranks.collect()
        i = 0
        while i < 10:
            print(links_r[i])
            i += 1
        contributions = links_ranks.flatMap(
            lambda page_links_rank: [(link, page_links_rank[1][1] / len(page_links_rank[1][0])) for link in page_links_rank[1][0]])
        
        contributions_r = contributions.collect()
        i = 0
        while i < 10:
            print(contributions_r[i])
            i += 1
        ranks = contributions.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: 0.15 + 0.85 * rank)

    final_ranks = ranks.collect()
    for page, rank in final_ranks:
        print(f"Page: {page}, Rank: {rank}")

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