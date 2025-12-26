FROM python:3.12
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    openssh-client \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
RUN python -m pip install -U pip
