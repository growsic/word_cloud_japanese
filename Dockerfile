FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN apt install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file swig
RUN apt-get install mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
RUN apt install -y fonts-ipaexfont
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install wordcloud
RUN pip install matplotlib
RUN pip install mecab-python3