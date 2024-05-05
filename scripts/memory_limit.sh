# arg1 is the amount of memory to limit on. For ex. $((40 * 1024 * 1024)) which is 40 MB
sudo echo $1 > /sys/fs/cgroup/memory/tokenizer/memory.limit_in_bytes
# arg2 -> python3, arg3 -> <python_file_name>, arg4|arg5 -> <python file arguments>
sudo cgexec -g memory:tokenizer $2 $3 $4 $5

# bash memory_limits.sh $((40 * 1024 * 1024)) python3 main.py english/base_dataset 128000