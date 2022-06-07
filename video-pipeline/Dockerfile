#Deriving the latest base image
FROM python:latest

WORKDIR /Users/HCES/Documents/GitHub/AS2-MLC-Project/app

#to COPY the remote file at working directory in container
COPY yolo_video.py ./

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python
RUN pip install numpy

CMD [ "python", "./yolo_video.py"]

EXPOSE 1234