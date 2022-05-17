import statistics
import glob
import cv2
import datetime
from moviepy.editor import *
import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

video_dir = input("Enter Video Folder Path: ")
audio_dir = input("Enter Audio Folder Path: ")


def video_paths(folder_path):
    video_paths = []
    for filename in os.listdir(folder_path):
        if not filename.startswith('.'):
            video_paths.append(str(os.path.join(folder_path, filename)))
    return video_paths


def video_format(video_paths):
    formats = []
    for video in video_paths:
        split_tup = os.path.splitext(video)
        formats.append(split_tup[-1])
    return(print("The video formats are: {}".format(formats)))


def video_resolution(video_paths):
    resolutions = []
    for video in video_paths:
        vid = cv2.VideoCapture(video)
        height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        resolutions.append(str(width) + " x " + str(height))


def extract_audios(video_paths, audio_dir):
    vid_idex = 0
    for video in video_paths:
        videoclip = VideoFileClip(video)
        audioclip = videoclip.audio
        audio_name = ("Audio_{}.mp3".format(vid_idex))
        os.chdir(audio_dir)
        audioclip.write_audiofile(audio_name)
        audioclip.close()
        videoclip.close()
        vid_idex += 1


def audio_paths(folder_path):
    audio_paths = []
    for filename in os.listdir(folder_path):
        if not filename.startswith('.'):
            audio_paths.append(str(os.path.join(folder_path, filename)))
    return audio_paths


def length_and_fps(video_paths):
    video_lengths = []
    fps = []
    for video_path in video_paths:
        video_data = cv2.VideoCapture(video_path)
        frames = video_data.get(cv2.CAP_PROP_FRAME_COUNT)
        fps_vid = int(video_data.get(cv2.CAP_PROP_FPS))
        video_lengths.append(int(frames / fps_vid))
        fps.append(fps_vid)
    average_dur = float(statistics.mean(video_lengths))
    average_fps = float(statistics.mean(fps))
    if average_dur > 60:
        return(print('Avarage Video Length is {} minutes and {} FPS'.format(float(average_dur/60), average_fps)))
    elif average_dur > 3600:
        return(print('Avarage Video Length is {} hours and {} FPS'.format(float(average_dur/3600), average_fps)))
    else:
        return(print('Avarage Video Length is {} seconds and {} FPS'.format(average_dur, average_fps)))


def avarage_bitrate(video_paths, audio_paths):
    bitrate = []
    for index in range(0, len(video_paths)):
        video = VideoFileClip(video_paths[index])
        mp3_size = os.path.getsize(audio_paths[index])
        vid_size = os.path.getsize(video_paths[index])
        duration = video.duration
        bitrate.append(int((((vid_size - mp3_size)/duration)/1024*8)))
    return(print("Avarage Bitrate is {}".format(float(statistics.mean(bitrate)))))


# get the paths for the videos from the video directory
vid_paths = video_paths(video_dir)
video_format(vid_paths)  # get the formats for the videos
# extract the audios from videos and save them in the audio directory
extract_audios(vid_paths, audio_dir)
# get the paths of the extracted audio phones
aud_paths = audio_paths(audio_dir)
length_and_fps(vid_paths)  # get the avarage lengths and fps of the videos
avarage_bitrate(vid_paths, aud_paths)  # get the avarage bitrate of the videos
video_resolution(vid_paths)
