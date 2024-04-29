sudo apt-get update
sudo apt install pip
pip install tiktoken
pip install Cython
pip install youtokentome
# to install perfstat
sudo apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`

sudo apt install cpulimit

#limit cpu
cpulimit -l 1 -- python main.py english/base_dataset 10
cpulimit -c 1 -l 1 -- python main.py english/base_dataset 10 # to limit core to 1

cpulimit -l 1 -i -- python main.py english/base_dataset 150000

# command : python3 generate_sentences.py english/base_dataset 128000
# command : python3 main.py english/base_dataset 128000

# to install a new version cpulimit.
$ make
# locate sysctl.h and change the include path (if error comes)
# cp src/cpulimit /usr/bin

# cpu limit running command : (changed in the perf_stat_cpu_limit file)
 python3 main.py english/base_dataset 131072 131072