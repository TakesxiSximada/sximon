# -*- coding: utf-8 -*-
FROM ubuntu:latest
MAINTAINER TakesxiSximada @TakesxiSximada

RUN apt-get update
RUN apt-get install -y --force-yes build-essential curl git zlib1g-dev libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev

# set key apt
# RUN add-apt-repository -y ppa:git-core/ppa
# RUN add-apt-repository -y ppa:webupd8team/java

# INSTALL
RUN apt-get install -y build-essential
RUN apt-get install -y software-properties-common
RUN apt-get install -y byobu
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y htop
RUN apt-get install -y man
RUN apt-get install -y unzip
RUN apt-get install -y vim
RUN apt-get install -y wget
RUN apt-get install -y supervisor
RUN apt-get install -y mecab libmecab-dev mecab-ipadic
RUN apt-get install -y libblas-dev
RUN apt-get install -y liblapack-dev
RUN apt-get install -y gfortran
RUN apt-get install -y g++
RUN apt-get install -y libfreetype6-dev
RUN apt-get install -y libpng-dev
RUN apt-get install -y libglib2.0-dev
RUN apt-get install -y libXpm-dev
RUN apt-get install -y libjpeg-dev
RUN apt-get install -y libgif-dev
RUN apt-get install -y libtiff4-dev
RUN apt-get install -y libncurses5-dev
# RUN apt-get install -y python2.7-dev
RUN apt-get install -y python3.4-dev
RUN apt-get install -y libatlas-base-dev
RUN apt-get install -y g++
RUN apt-get install -y gfortran
RUN apt-get install -y libopenblas-dev
RUN apt-get install -y liblapack-dev
RUN apt-get install -y build-essential
RUN apt-get install -y python3-tk
RUN apt-get install -y tk-dev
RUN apt-get install -y libpng12-dev
RUN apt-get install -y clang
RUN apt-get install -y libzmq-dev
RUN apt-get install -y libcv-dev libhighgui-dev libcvaux-dev python-opencv opencv-doc
RUN apt-get install -y libudev-dev
RUN apt-get install -y openjdk-6-jdk
RUN apt-get install -y freeglut3-dev
RUN apt-get install -y doxygen
RUN apt-get install -y graphviz
RUN apt-get install -y libopencv-dev

RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python3
RUN pip3 install -U setuptools
RUN pip3 install virtualenv

RUN mkdir -p /srv/sximada/sximon/current
RUN virtualenv /srv/sximada/sximon/deploy
RUN git clone http://github.com/TakesxiSximada/sximon.git /srv/sximada/sximon/current
RUN /srv/sximada/sximon/deploy/bin/pip install /srv/sximada/sximon/current
EXPOSE 6543:6543
ENTRYPOINT ["/srv/sximada/sximon/deploy/bin/pserve", "/srv/sximada/sximon/current/development.ini", "http_port=6543"]
