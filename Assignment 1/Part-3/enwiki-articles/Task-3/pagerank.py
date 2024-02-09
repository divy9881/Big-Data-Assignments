import sys
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Global dictionary to store whether a page has already been visited or not
lookup = dict()

"""
    Function to filter out any comments in the input file and split each line into a tuple of 2 nodes
    
    Args:
        line (str): Line of the input CSV file
"""
def filter_lines(line):
    # Skip lines starting with "#"
    if line.startswith("#"):
        return []
    # Split each line by tab into a tuple of 2 nodes
    else:
        return [tuple(line.split("\t", 1))]

"""
    Function to assign an initial Pagerank of 1.0 to each node of the webgraph
    
    Args:
        line (str): Line of the input CSV file
"""    
def assign_ranks(pair):
    ranks = []
    # Check if the first node of the pair has been visited
    if pair[0] not in lookup:
        # Mark the node to be visited
        lookup[pair[0]] = True
        # Assign initial rank of 1.0 to the node
        ranks.append((pair[0], 1.0))
    # Check if the second node of the pair has been visited
    elif pair[1] not in lookup:
        # Mark the node to be visited
        lookup[pair[1]] = True
        # Assign initial rank of 1.0 to the node
        ranks.append((pair[1], 1.0))
    return ranks

"""
    Function to compute Pageranks by running the Pagerank algorithm for 10 iterations
    
    Args:
        input_file_path (str): Path to the input file containing edges of the webgraph
"""
def pagerank(input_file_path):
    # Read input file as an RDD of lines
    data_frame = spark_context.textFile(input_file_path)
    
    # FlatMap to filter out comments and split each line into a tuple of nodes
    edges = data_frame.flatMap(filter_lines)

    # FlatMap to assign an initial Pagerank of 1.0 to each node
    ranks = edges.flatMap(assign_ranks)
    
    # Persist ranks RDD in-memory
    if persist_option == "persist-all":
        ranks.persist()

    # Group links by node and convert to an adjacency list
    adjacency_list = edges.groupByKey().mapValues(list)

    # Persist adjacency list RDD in-memory
    if persist_option == "persist-all" or persist_option == "persist-adj":
        adjacency_list.persist()

    # Run Pagerank algorithm for 10 iterations
    for iteration in range(10):
        # Join links with current Pageranks
        list_ranks = adjacency_list.join(ranks)

        # Persist joined RDD for adjacency_list and ranks in-memory
        if persist_option == "persist-all":
            list_ranks.persist()

        # Compute contributions of each node to its neighbours' Pageranks
        contributions = list_ranks.flatMap(lambda list_rank: [(node, list_rank[1][1] / len(list_rank[1][0])) for node in list_rank[1][0]])

        # Persist contributions RDD in-memory
        if persist_option == "persist-all":
            contributions.persist()

        # Aggregate contributions per node and then compute the new Pagerank for that node
        ranks = contributions.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: 0.15 + 0.85 * rank)
        
        # Persist ranks RDD in-memory
        if persist_option == "persist-all":
            ranks.persist()

    # Get the top 10000 pages by final Pagerank and write to file
    # final_ranks = ranks.top(10000)
    # f = open("final_ranks.txt", "w+")
    # for page, rank in final_ranks:
    #     f.write("Page: {page}, Rank: {rank} \n".format(page=page, rank=rank))
    # f.close()

if __name__ == "__main__":
    # Proper usage check
    if len(sys.argv) != 3:
        print("Usage: spark-submit <script.py> <input_path>")
        sys.exit(1)

    # Configure Spark context
    conf = SparkConf().setAppName("Big-Data-Assignment-1-Part-3") \
                            .set("spark.driver.memory", "30g") \
                            .set("spark.executor.memory", "30g") \
                            .set("spark.executor.cores", "5") \
                            .set("spark.executor.cpus", "1") \
                            .set("spark.local.dir", "/mnt/data") \

    # Initialize SparkContext and SparkSession
    spark_context = SparkContext(conf=conf)
    spark_app = SparkSession(spark_context)

    # Extract path to input file from command-line arguments
    input_path = sys.argv[1]
    persist_option = sys.argv[2]
    
    # Compute Pageranks
    pagerank(input_path, persist_option)

    # Stop Spark application
    spark_context.stop()