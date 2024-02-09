```
$ SPARK_HOME=~/spark-3.3.4-bin-hadoop3
$ cd ~
$ git clone https://github.com/divy9881/big-data-assignments
$ export PATH=$PATH:hadoop-3.3.6/bin
$ export PATH=$PATH:hadoop-3.3.6/sbin
$ export PATH=$PATH:spark-3.3.4-bin-hadoop3/bin
$ hdfs dfs -mkdir /part-3
$ hdfs dfs -mkdir /part-3/enwiki
$ hdfs dfs -put /proj/uwmadison744-s24-PG0/data-part3/enwiki-pages-articles/* /part-3/enwiki/
$ $SPARK_HOME/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/Part-3/enwiki-articles/Task-4/pagerank.py hdfs://10.10.1.1:9000/part-3/enwiki/*
```