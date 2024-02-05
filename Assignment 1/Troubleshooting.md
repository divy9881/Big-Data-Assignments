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

### Install dep to a particular python version
```
python3.7 -m pip install pyspark
python3.7 -m pyspark
```

### Set default Python version
```
sudo update-alternatives --config python
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7.5 1
sudo update-alternatives --config python
sudo update-alternatives --set python /usr/bin/python3.6
```

### Solve bad magic number issue
```
find . -name '*.pyc' -delete
```

### Workaround for non-routable IPs
```
$ ssh -D 1337 -q -C -N dspatel6@c220g5-111206vm-1.wisc.cloudlab.us
# And then create a Manual Proxy SOCK 5 Entry for localhost:1337 in browser
```

Follow the instructions given on [Assignment Page](https://pages.cs.wisc.edu/~shivaram/cs744-sp24/assignment1.html)