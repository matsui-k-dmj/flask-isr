# install

## Docker

ISR の gpu 向けイメージをビルドしておく

普通にやると CuDNNのバージョンがおかしい。tf2.0使ってるのにイメージはtf1.13だから

Dockerfile.gpuをFROM tensorflow/tensorflow:latest-gpu-py3に書き換えて, 
```zsh
docker build -t isr:latest-gpu . -f Dockerfile.gpu
```

[Docker \- Image Super\-Resolution](https://idealo.github.io/image-super-resolution/tutorials/docker/)