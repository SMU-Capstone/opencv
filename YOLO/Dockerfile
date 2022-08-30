FROM python:3.7
LABEL MAINTAINER "Yunho Yun yunho_yun@naver.com"
RUN mkdir /app
WORKDIR /app
copy . .
RUN apt-get update -y && \
	apt-get install -y libx11-xcb1 libgl1-mesa-glx && \
	apt-get install -y  python3 python3-pip && \
	pip install --upgrade pip && \
	pip install -r requirements.txt --no-cache
