#!/bin/bash

# Update and Install necessary packages
apt update -y && apt install unzip git wget nano libzstd-dev libzstd1 vim python3 cuda-cudart-12-8 joe zip screen curl libcurl4 libcudart12 build-essential gcc make -y

# # Clone the repository
# git clone https://github.com/Mariajian88/240.git



# # Navigate to the cloned repository
cd 240

# Make the vanitysearch executable
chmod 777 /root/240/vanitysearch

# create Screen
screen -S vanity

# Run the python script with arguments
#python3 /root/240/start_prefix_vanity.py "$@"