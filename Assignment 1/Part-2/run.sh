SPARK_HOME=~/spark-3.3.4-bin-hadoop3
git clone https://github.com/divy9881/big-data-assignments
wget http://pages.cs.wisc.edu/~shivaram/cs744-fa18/assets/export.csv
export PATH=$PATH:hadoop-3.3.6/bin
export PATH=$PATH:hadoop-3.3.6/sbin
export PATH=$PATH:spark-3.3.4-bin-hadoop3/bin
hdfs dfs -copyFromLocal ./export.csv /export.csv
$SPARK_HOME/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/Part-2/sort.py hdfs://10.10.1.1:9000/export.csv hdfs://10.10.1.1:9000/final-result