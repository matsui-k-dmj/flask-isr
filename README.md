# Install

## Docker

ISR の gpu 向けイメージをビルドしておく

普通にやると CuDNN のバージョンがおかしい。tf2.0 使ってるのにイメージは tf1.13 だから

Dockerfile.gpu を FROM tensorflow/tensorflow:latest-gpu-py3 に書き換えて,

```zsh
docker build -t isr:latest-gpu . -f Dockerfile.gpu
```

[Docker \- Image Super\-Resolution](https://idealo.github.io/image-super-resolution/tutorials/docker/)

# Usage

## docker build

.devcontainer/Dockerfile をビルド

```
docker build -t flask-isr . -f .devcontainer/Dockerfile
```

起動

```
docker run -it --rm --gpus=all --memory=8g --memory-swappiness=0 -p=5000:5000 --entrypoint '' flask-isr bash

python app.py
```
