# pull official base image
FROM python:3

# set work directory
WORKDIR /code

RUN apt update

RUN apt install -y python-pil python3-pil

RUN apt-get update && apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 \ 
    libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 \
    fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
    
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /code

# install dependencies
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

RUN chmod +X /code/run_web.sh
