#Deriving the latest base image
FROM python:latest

WORKDIR /Users/HCES/Documents/GitHub/AS2-MLC-Project/app

#to COPY the remote file at working directory in container
COPY pose_video.py ./
COPY yolo_video.py ./
COPY yolov3.cfg ./
COPY yolov3.txt ./
COPY yolov3.weights ./
COPY original_video.mp4 ./

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN pip install numpy

CMD [ "python", "./yolo_video.py"]

EXPOSE 1234