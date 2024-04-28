sudo apt update
sudo apt install pip
pip install tiktoken
pip install Cython
pip install youtokentome
# to install perfstat
sudo apt-get install linux-tools-common linux-tools-generic linux-tools-`uname -r`

#limit cpu
cpulimit -l 1 -- python main.py english/base_dataset 10
cpulimit -c 1 -l 1 -- python main.py english/base_dataset 10 # to limit core to 1
