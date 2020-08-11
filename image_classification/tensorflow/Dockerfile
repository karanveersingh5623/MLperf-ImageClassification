FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04


WORKDIR /research

RUN apt-get update

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    libc-dev \
    build-essential \
    git \
    python-pip \
    python3-pip

RUN apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update

RUN apt-get install -y build-essential python3.7 python3.7-dev python3-pip python3.7-venv
RUN apt-get install -y git

# update pip
RUN python3.7 -m pip install pip --upgrade
RUN python3.7 -m pip install wheel



ENV HOME /research
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH


RUN apt-get install -y python-setuptools

RUN apt-get install -y python-pip python3-pip virtualenv htop
RUN pip3 install setuptools
#RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade numpy==1.19.0
RUN pip3 install --upgrade scipy sklearn tf-nightly-gpu
#RUN pip3 install --upgrade numpy
#RUN pip3 install scipy
#RUN pip3 install sklearn 
#RUN pip install tf-nightly-gpu


# Mount data into the docker
ADD . /research/resnet


WORKDIR /research/resnet
RUN pip3 install -r official/requirements.txt


ENTRYPOINT ["/bin/bash"]

