import datetime
import glob
import math
import os
import statistics
from pathlib import Path
import subprocess
import ast

import cv2
import numpy as np
import torch
import torchvision.transforms as transforms
from moviepy.editor import *
from PIL import Image, ImageStat

os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"



def detect_objects(video_file, model, classes):
    """
    Get the objects present in the video
    This function returns the a set of objects found in the video file
    Parameters
    -----------
    video_file : path to a specific video 
    model : CNN model used for object detection
    classes: labels of the coco dataset
    Returns
    -------
    set
        {'person', 'cell phone', 'chair', 'tv'}
    """

    cap = cv2.VideoCapture(video_file)
    objects = list()
    while True:
        ret, frame = cap.read()
        if ret:
            result = model(frame)
            labels = result.xyxyn[0][:, -1].numpy()
            for index in range(len(labels)):
                objects.append(classes[int(labels[index])])
        else:
            return set(objects)

detect_objects('/Users/jana/Documents/GitHub/AS2-MLC-Project/Videos/example_video_1.mp4', model, classes)