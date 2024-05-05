## Steps to memory limit the process
```
# First make sure whether cgexec is being installed and is working

# Setup cgroup for our purpose
$ bash setup_cgroup.sh

# Now, run python process with memory limit(for ex. 40 MB)
$ bash memory_limit.sh $((40 * 1024 * 1024)) python3 ../main.py english/base_dataset 128000
```