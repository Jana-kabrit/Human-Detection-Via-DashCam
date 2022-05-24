import statistics
import glob
import cv2
import datetime
from moviepy.editor import *
import os
from pathlib import Path
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"


def video_paths(video_dir):
    video_paths = []
    for filename in os.listdir(video_dir):
        if not filename.startswith('.'):
            video_paths.append(os.path.join(video_dir, filename))
    return video_paths


def video_format(video_path):
    split_tup = os.path.splitext(video_path)
    format = (split_tup[-1])
    return format


def video_resolution(video_path):
    vid = cv2.VideoCapture(video_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    resolution = str(width) + " x " + str(height)
    return resolution


def extract_audios(video_path):
    video_name = str(Path(video_path).stem)
    videoclip = VideoFileClip(video_path)
    audioclip = videoclip.audio
    audio_name = (video_name + "_Audio.mp3")
    audioclip.write_audiofile(audio_name)
    audioclip.close()
    videoclip.close()


def audio_paths(audio_dir):
    audio_paths = []
    for filename in os.listdir(audio_dir):
        if not filename.startswith('.'):
            audio_paths.append(str(os.path.join(audio_dir, filename)))
    return audio_paths


def length_and_fps(video_path):
    video_data = cv2.VideoCapture(video_path)
    frames = video_data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps_vid = int(video_data.get(cv2.CAP_PROP_FPS))
    video_length = int(frames / fps_vid)
    return video_length, fps_vid


def bitrate(video_path, audio_path):
    video = VideoFileClip(video_path)
    mp3_size = os.path.getsize(audio_path)
    vid_size = os.path.getsize(video_path)
    duration = video.duration
    bit_rate = int((((vid_size - mp3_size)/duration)/1024*8))
    return bit_rate
