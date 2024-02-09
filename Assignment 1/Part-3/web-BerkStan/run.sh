SPARK_HOME=~/spark-3.3.4-bin-hadoop3
cd ~
git clone https://github.com/divy9881/big-data-assignments
wget https://snap.stanford.edu/data/web-BerkStan.txt.gz
gunzip web-BerkStan.txt.gz
export PATH=$PATH:hadoop-3.3.6/bin
export PATH=$PATH:hadoop-3.3.6/sbin
export PATH=$PATH:spark-3.3.4-bin-hadoop3/bin
hdfs dfs -mkdir /part-3
hdfs dfs -copyFromLocal ./web-BerkStan.txt /part-3/web-BerkStan.txt
$SPARK_HOME/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/Part-3/web-BerkStan/pagerank.py hdfs://10.10.1.1:9000/part-3/web-BerkStan.txt