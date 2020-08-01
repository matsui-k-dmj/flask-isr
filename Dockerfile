FROM isr:latest-gpu

RUN apt update && \
    apt install -y git \
    libcurl4-openssl-dev \
    libssl-dev

RUN python -m pip install -U pip && \
    python -m pip install flask \
    opencv-python \
    yapf mypy pylint

COPY app.py model.py templates ./