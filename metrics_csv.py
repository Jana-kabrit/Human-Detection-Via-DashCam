from EDA import *
import csv
import pandas as pd


def metrics_csv(video_dir, audio_dir):

    vid_paths = video_paths(video_dir)

    with open('video_metrics.csv', 'w') as file:
        header = ['Video Name', 'Format', 'Length', 'FPS', 'Resolution']
        writer = csv.writer(file)
        writer.writerow(header)

    curr_path = str(os.getcwd())
    csv_path = curr_path + '/video_metrics.csv'
    metrics = pd.read_csv(csv_path)

    for video in vid_paths:
        data_row = []

        video_name = str(Path(video).stem)
        format_vid = video_format(video)
        length, fps = length_and_fps(video)
        resolution = video_resolution(video)
        data_row = [video_name, format_vid, length, fps, resolution]

        data_series = pd.Series(data_row, index=metrics.columns)
        metrics = metrics.append(data_series, ignore_index=True)

        os.chdir(audio_dir)
        extract_audios(video)

    aud_paths = audio_paths(audio_dir)

    bit_rate = []
    for index in range(0, len(vid_paths)):
        bit_rate.append(bitrate(vid_paths[index], aud_paths[index]))

    metrics['Bitrate'] = bit_rate
    print(metrics.head())

    os.chdir(curr_path)
    metrics.to_csv('video_metrics.csv', index=False)


video_dir = '/Users/jana/Documents/GitHub/BUMP_Study_VideoDiary_Analysis/Videos'
audio_dir = '/Users/jana/Documents/GitHub/BUMP_Study_VideoDiary_Analysis/Audios'
metrics_csv(video_dir, audio_dir)
