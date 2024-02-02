### Make myself owner and give all users permissions to namenode and datanode directories
```
sudo chown -R dspatel6 /mnt/data/datanode
sudo chown -R dspatel6 /mnt/data/namenode
sudo chmod ugo+rwx /mnt/data/namenode
sudo chmod ugo+rwx /mnt/data/datanode
```

Follow the instructions given on [Assignment Page](https://pages.cs.wisc.edu/~shivaram/cs744-sp24/assignment1.html)