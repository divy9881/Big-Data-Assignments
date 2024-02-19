## Get host IP address
```
$ ifconfig
```

## Train and test model
```
# rank 0 for master and rank 1, 2, 3 for workers 
$ python3 main.py --master-ip 172.18.0.2 --num-nodes 4 --rank <rank>
```