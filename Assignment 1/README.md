# Assignment-1

## Directory tree structure
- `./Part-2`
- `./Part-3`
- `./Troubleshooting.md`

## Part-2

### Run sort.py Pyspark script

#### Directory tree structure
- `./Part-2/run.sh`
- `./Part-2/sort.py`


```
$ SPARK_HOME=~/spark-3.3.4-bin-hadoop3
$ git clone https://github.com/divy9881/big-data-assignments
$ wget http://pages.cs.wisc.edu/~shivaram/cs744-fa18/assets/export.csv
$ export PATH=$PATH:hadoop-3.3.6/bin
$ export PATH=$PATH:hadoop-3.3.6/sbin
$ export PATH=$PATH:spark-3.3.4-bin-hadoop3/bin
$ hdfs dfs -copyFromLocal ./export.csv /export.csv
$ $SPARK_HOME/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/Part-2/sort.py hdfs://10.10.1.1:9000/export.csv hdfs://10.10.1.1:9000/final-result
```

## Part-3

### Run PageRank on web-BerkStan data

#### Directory tree structure
- `./Part-3/web-BerkStan`
- `./Part-3/web-BerkStan/run.sh`
- `./Part-3/web-BerkStan/pagerank.py`

```
$ SPARK_HOME=~/spark-3.3.4-bin-hadoop3
$ cd ~
$ git clone https://github.com/divy9881/big-data-assignments
$ wget https://snap.stanford.edu/data/web-BerkStan.txt.gz
$ gunzip web-BerkStan.txt.gz
$ export PATH=$PATH:hadoop-3.3.6/bin
$ export PATH=$PATH:hadoop-3.3.6/sbin
$ export PATH=$PATH:spark-3.3.4-bin-hadoop3/bin
$ hdfs dfs -mkdir /part-3
$ hdfs dfs -copyFromLocal ./web-BerkStan.txt /part-3/web-BerkStan.txt
$ $SPARK_HOME/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/pagerank.py hdfs://10.10.1.1:9000/part-3/web-BerkStan.txt
```

### Run PageRank on enwiki articles data

#### Directory tree structure
- `./Part-3/enwiki-articles`
- `./Part-3/enwiki-articles/Task-1`
- `./Part-3/enwiki-articles/Task-1/run.sh`
- `./Part-3/enwiki-articles/Task-1/pagerank.py`
- `./Part-3/enwiki-articles/Task-2`
- `./Part-3/enwiki-articles/Task-2/run.sh`
- `./Part-3/enwiki-articles/Task-2/pagerank.py`
- `./Part-3/enwiki-articles/Task-3`
- `./Part-3/enwiki-articles/Task-3/run.sh`
- `./Part-3/enwiki-articles/Task-3/pagerank.py`
- `./Part-3/enwiki-articles/Task-4`
- `./Part-3/enwiki-articles/Task-4/run.sh`
- `./Part-3/enwiki-articles/Task-4/kill-worker.sh`
- `./Part-3/enwiki-articles/Task-4/pagerank.py`

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
$ $SPARK_HOME/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/pagerank.py hdfs://10.10.1.1:9000/part-3/enwiki/*
```