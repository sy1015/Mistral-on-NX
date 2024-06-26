# MAAL-on-Jetson

This repository contains a demo application that runs [MAAL](https://huggingface.co/maum-ai/Llama-3-MAAL-8B-Instruct-v0.1) on NVIDIA Jetson AGX orin hardware. The app has been developed on NVIDIA Jetson AGX orin developer kit.

## Prerequisites on Host device
### Software
 * [NVIDIA JetPack SDK](https://developer.nvidia.com/embedded/jetpack) >= 5.1.2
   * To install, `sudo apt install nvidia-jetpack`
 * [NVIDIA container runtime](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
   * make sure that it is a default runtime

```
# Edit /etc/docker/daemon.json
{
    "runtimes": {
        "nvidia": {
            "args": [],
            "path": "nvidia-container-runtime"
        }
    },
    "default-runtime": "nvidia"
}
# Run `sudo systemctl restart docker` after editing the file
```
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
sudo docker run -it --rm --runtime nvidia --network host maal-on-jetson
```

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
sudo docker run --runtime nvidia -it --rm --network host maal-on-jetson-mlc
```

Inside the container, run the python application
```
# Inside the container
python3 mlc.py
```

### Deploying REST server using MLC
Inside the container, run REST server
```
# Inside the container
python3 -m mlc_chat.rest --model dist/Llama-3-MAAL-8B-Instruct-v0.1-q4f32-MLC/ --lib-path dist/libs/Llama-3-MAAL-8B-Instruct-v0.1-q4f32-cuda.so --device cuda
```

Test with a sample client. 
```
# On a separate terminal, run
python3 client.py
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


