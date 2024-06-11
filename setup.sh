#!/bin/bash

set -eux


# # install python3.10
# sudo apt-get update
# sudo apt-get install software-properties-common -y
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt-get update
# sudo apt-get install python3.10 python3.10-venv python3.10-dev -y
# sudo rm /usr/bin/python3
# sudo ln -s python3.10 /usr/bin/python3
# sudo apt-get install curl -y
# curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10


# # # install pytorch
# export TORCH_INSTALL=https://developer.download.nvidia.cn/compute/redist/jp/v511/pytorch/torch-2.0.0+nv23.05-cp38-cp38-linux_aarch64.whl
# python3 -m pip install --upgrade pip
# python3 -m pip install numpy=='1.26.1'
# python3 -m pip install --no-cache $TORCH_INSTALL

# # install dependency
pip install -r requirements.txt