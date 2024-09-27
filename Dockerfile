FROM ubuntu:focal
ENV TZ=Asia/Singapore
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt install -y python3-pip


RUN apt install -y stress-ng
#install dependencies
RUN pip install flask
RUN pip install psutil
RUN pip install requests
RUN pip install numpy==1.19.4
RUN apt install -y python3-opencv
#RUN apt install -y libopencv-dev python3-opencv
#RUN apt install stress
COPY ./vs /vs
WORKDIR /vs

EXPOSE 5006

# Set the default command
CMD ["python3", "vs_rest.py"]
