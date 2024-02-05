### Run sort.py Pyspark script
```
~/spark-3.3.4-bin-hadoop3/bin/spark-submit --master=spark://10.10.1.1:7077 ~/Big-Data-Assignments/Assignment\ 1 sort.py hdfs://10.10.1.1:9000/export.csv hdfs://10.10.1.1:9000/final-result
```

### Run web-BerkStan app
```
 ~/spark-3.3.4-bin-hadoop3/bin/spark-submit --master=spark://10.10.1.1:7077 ~/Big-Data-Assignments/Assignment\ 1/pagerank.py hdfs://10.10.1.1:9000/part-3/web-BerkStan.txt
```