import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

lookup = dict()

def filter_lines(line):
    if line.startswith("#"):
        return []
    else:
        return [tuple(line.split("\t", 1))]
    
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

    # f = open("counts.txt", "w+")
    # f.write(str(ranks.count()))
    # f.close()

    links = links.groupByKey().mapValues(list)

    for iteration in range(10):
        links_ranks = links.join(ranks)

        # links_r = links_ranks.top(100)
        # f = open("links.txt", "w+")
        # for l in links_r:
        #     f.write("{} \n".format(str(l)))
        # f.close()

        contributions = links_ranks.flatMap(lambda page_links_rank: [(link, page_links_rank[1][1] / len(page_links_rank[1][0])) for link in page_links_rank[1][0]])
        
        # contributions_r = contributions.top(100)
        # f = open("contributions.txt", "w+")
        # for l in contributions_r:
        #     f.write("{} \n".format(str(l)))
        # f.close()

        ranks = contributions.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: 0.15 + 0.85 * rank)

    final_ranks = ranks.top(10000)
    f = open("final_ranks.txt", "w+")
    for page, rank in final_ranks:
        f.write("Page: {page}, Rank: {rank} \n".format(page=page, rank=rank))
    f.close()
    

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