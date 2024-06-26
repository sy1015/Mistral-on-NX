# MAAL-on-Jetson

This repository contains a demo application that runs [MAAL](https://huggingface.co/maum-ai/Llama-3-MAAL-8B-Instruct-v0.1) on NVIDIA Jetson AGX orin hardware. The app has been developed on NVIDIA Jetson AGX orin developer kit.

## Prerequisites on Host device
### Software
 * [NVIDIA JetPack SDK](https://developer.nvidia.com/embedded/jetpack) >= 5.1.2
   * To install, `sudo apt install nvidia-jetpack`
### Hardware
#### Tested
 * Jetson AGX Orin 64GB module
#### To be tested
 * Jetson AGX Orin 32GB module
 * Jetson Orin NX 16GB module
 * Jetson Orin NX 8GB module


## Getting started
First, clone this repo and cd into the directory
```
git clone https://github.com/phgcha/MAAL-on-Jetson.git
cd MAAL-on-Jetson
```

### Using HF transformers
Build the docker image that contains dependency
```
sudo docker build -f Dockerfile -t maal-on-jetson .
```
Exec into the container

```
sudo docker run -it --rm --runtime nvidia --network host -v ~/MAAL-on-Jetson/:/MAAL-on-Jetson maal-on-jetson
```
 * It is important to specify `--runtime nvidia` for the container to detect the NVIDIA hardware.

**Inside the container,** run the python application
```
python3 main.py
```

### Using MLC
Build the docker image that contains dependency
```
sudo docker build -f Dockerfile.mlc -t maal-on-jetson-mlc .
```

Exec into the container
```
sudo docker run --runtime nvidia -it --rm --network host -v ~/MAAL-on-Jetson/:/MAAL-on-Jetson maal-on-jetson-mlc
```
 * It is important to specify `--runtime nvidia` for the container to detect the NVIDIA hardware.

Inside the container, run the python application
```
# Inside the container
python3 mlc.py
```


## Dev dependency on Host device
### jtop
Make sure you're in python venv before installing. Once installed, Start the jtop service and reboot.
```
source {your venv dir}/bin/activate
pip3 install jetson-stats
sudo systemctl restart jtop.service
sudo reboot
```


