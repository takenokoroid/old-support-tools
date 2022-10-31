FROM python:3.10.7-slim-buster

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# pycacheを作らないようにする
ENV PYTHONDONTWRITEBYTECODE 1
# エラーや標準出力はバッファリングしない
ENV PYTHONUNBUFFERED 1
COPY . /usr/src/app/