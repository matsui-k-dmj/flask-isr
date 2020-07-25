FROM isr:gpu

RUN apt update && \
    apt install -y git

COPY requirements.txt .

RUN python -m pip install -U pip && python -m pip install -r requirements.txt