This is a sample Dockerfile you can modify to deploy your own app based on face_recognition
Modificated by Matteo Bianchi to run his project server

FROM python:3.6-slim-stretch
#install necesary package
RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS



#install my app

RUN git clone https://github.com/yuky2020/Face-recognition-with-NOIR-camera-on-RaspberryPi

CMD cd Face-recognition-with-NOIR-camera-on-RaspberryPi/Server && \
    python3 Server.py 
      

