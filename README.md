# AS2-MLC-Project
The aim is to create a probability-matrix / neural-network that can positively identify elements present within a captured video frame with a degree of accuracy by using pattern-matching techniques. The format of this frame will likely be uncompressed 24-bit RGB.

## 👩‍💻 Authors

- [@OussamaMatar](https://github.com/OussamaMatar)
- [@Jana-kabrit](https://github.com/Jana-kabrit)


## 🏃🏻‍♀️ Pipelines

`image_pipeline.py` runs the analysis for a single image.
`video_pipeline.py` runs the analysis for a video.

## 🛠 Requirements

### To download:
- [ffmpeg](https://www.ffmpeg.org/download.html)

#### Installation:

**MAC**

```bash
pip3 install ffprobe
```

**WINDOWS**

```bash
pip install ffprobe
```

**LINUX**

```bash
pip install ffprobe


## 🚦 EDA.py

In this file, we have 7 functions that are for exploring the videos and the data that we have. The table below explains what each function is by its input and output.

### Functions

| Function  |Libraries Needed: | Input    | Output                            |
| :-------- | :------- | :-------------------------------- | :-------------------------------- |
| `video_paths(video_dir)`       | [os](https://docs.python.org/3/library/os.html) | **video_dir** `str`: path to the directory that contains all the videos | **video_paths** `list`: a list containing the paths of all the videos|
| `video_format(video_path)`      |[os](https://docs.python.org/3/library/os.html)  | **video_path** `str`: path to specific video| **format** `str`: video format _ex ".mp4", ".mov",..._|
| `video_resolution(video_path)`      |[cv2](https://pypi.org/project/opencv-python/) |  **video_path** `str`: path to specific video | **resolution** `str`: string containing width x height of the video |
| `extract_audios(video_path)`       |[os](https://docs.python.org/3/library/os.html)  | **video_path** `str`: path to specific video  | **None**. Extracts audio from video and saves it in the working directory.|
| `audio_paths(audio_dir)`       |[pathlib](https://docs.python.org/3/library/pathlib.html), [moviepy](https://zulko.github.io/moviepy/) |**audio_dir** `str`: path to the directory that contains all the audios| **audio_paths** `list`: a list containing the paths of all the audios|
| `length_and_fps(video_path)`     |[cv2](https://pypi.org/project/opencv-python/) | **video_path** `str`: path to specific video  | **video_length** `int`: length of the video  **fps_vid** `int`: the frames per second count of the video|
|`bitrate(video_path, audio_path)`|[moviepy](https://zulko.github.io/moviepy/), [os](https://docs.python.org/3/library/os.html)  | **video_path** `str`: path to specific video **audio_path** `str`: path to specific audio corresponding to the same video |**bit_rate** `int`: the bitrate of the video|

# 📈 metrics_csv.py

The function of metrics_csv is to loop over a directory containing all the videos, extract their audios, and make a CSV file that contains the information about each video. The name of the CSV file is video_metrics.csv and the image below is an example output of when the script is run using 2 example videos.
This file includes one function only 

| Function  |Libraries Needed: | Input    | Output                            |
| :-------- | :------- | :-------------------------------- | :-------------------------------- |
|`metrics_csv(video_dir, audio_dir)`| csv, pandas, and (all libraries from EDA file)|**video_dir** `str`: path to the directory that contains all the videos **audio_dir** `str`: path to the directory that contains all the audios| **"video_csv.csv"** `csv` : csv file containing outline |

An example of the csv file is:
<img width="445" alt="Screen Shot 2022-05-20 at 4 41 43 PM" src="https://user-images.githubusercontent.com/63118072/169992260-7f3e828b-22e2-4472-9a7d-3ae76bb30491.png">
