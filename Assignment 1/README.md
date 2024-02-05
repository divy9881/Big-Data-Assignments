### Run sort.py Pyspark script
```
$ git clone https://github.com/divy9881/big-data-assignments
$ wget http://pages.cs.wisc.edu/~shivaram/cs744-fa18/assets/export.csv
$ hdfs dfs -copyFromLocal ./export.csv /export.csv
$ ~/spark-3.3.4-bin-hadoop3/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/sort.py hdfs://10.10.1.1:9000/export.csv hdfs://10.10.1.1:9000/final-result
```

### Run PageRank on web-BerkStan data
```
$ git clone https://github.com/divy9881/big-data-assignments
$ wget https://snap.stanford.edu/data/web-BerkStan.txt.gz
$ gunzip web-BerkStan.txt.gz
$ hdfs dfs -mkdir /part-3
$ hdfs dfs -copyFromLocal ./web-BerkStan.txt /part-3/web-BerkStan.txt
$ ~/spark-3.3.4-bin-hadoop3/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/pagerank.py hdfs://10.10.1.1:9000/part-3/web-BerkStan.txt
```

### Run PageRank on enwiki articles data
```
$ git clone https://github.com/divy9881/big-data-assignments
$ hdfs dfs -put /proj/uwmadison744-s24-PG0/data-part3/enwiki-pages-articles/* /part-3/enwiki/
$ ~/spark-3.3.4-bin-hadoop3/bin/spark-submit --master=spark://10.10.1.1:7077 ./Big-Data-Assignments/Assignment\ 1/pagerank.py hdfs://10.10.1.1:9000/part-3/enwiki/*
```