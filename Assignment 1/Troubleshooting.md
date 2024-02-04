### Make myself owner and give all users permissions to namenode and datanode directories
```
sudo chown -R dspatel6 /mnt/data/datanode
sudo chown -R dspatel6 /mnt/data/namenode
sudo chmod ugo+rwx /mnt/data/namenode
sudo chmod ugo+rwx /mnt/data/datanode
```

### Add hadoop and spark executables to env
```
export PATH=$PATH:hadoop-3.3.6/bin
export PATH=$PATH:hadoop-3.3.6/sbin
export PATH=$PATH:spark-3.3.4-bin-hadoop3/bin
```

Follow the instructions given on [Assignment Page](https://pages.cs.wisc.edu/~shivaram/cs744-sp24/assignment1.html)