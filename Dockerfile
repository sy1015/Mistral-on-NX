# FROM nvcr.io/nvidia/l4t-jetpack:r35.4.1
# FROM nvcr.io/nvidia/l4t-base:r36.2.0
FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3


# dev dependency 
RUN apt-get update && apt-get install -y vim

WORKDIR /app

COPY . /app/

RUN bash setup.sh
