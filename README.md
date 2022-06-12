# AS2-MLC-Project
The aim is to create a probability-matrix / neural-network that can positively identify elements present within a captured video frame with a degree of accuracy by using pattern-matching techniques. The format of this frame will likely be uncompressed 24-bit RGB.

## 👩‍💻 Authors

- [@OussamaMatar](https://github.com/OussamaMatar)
- [@Jana-kabrit](https://github.com/Jana-kabrit)


## 🛠 Requirements

### To download:
- [ffmpeg](https://www.ffmpeg.org/download.html)
- [Numpy](https://numpy.org)
- [MediaPipe](https://google.github.io/mediapipe/getting_started/install.html)
- [opencv-python](https://pypi.org/project/opencv-python/)
- [Gradio](https://www.gradio.app)

## 🎞 Pipelines

Inside our repo, you will find the "Pipelines" directory that includes all of our pipelines for object detection.

`image_pipeline.py` runs the analysis for a single image. <br>
`video_pipeline.py` runs the analysis for a video.

### 🚦 image_pipeline.py

This pipeline includes the built of a web-app made using Gradio (linked above). When deployed, it will host the image pipeline on a local web app which includes the following:

#### 🏃‍♀️ How to run:
 1. You need to clone this repository: `git clone ssh://john@example.com/path/to/my-project.git` 
 2. Go to the Pipelines folder: `cd Pipelines/ImagePipeline`
 3. Download the yolov3.weights from [this link](https://pjreddie.com/media/files/yolov3.weights)
 4. Move the yolov3.weights downloaded to the ImagePipeline directory either through your file manager or through the terminal using `mv path/to/yolov3.weights path/to/ImagePipeline`
 5. Run the python file using the command `python image_pipeline.py`

#### 🕺 Functions Breakdown

| Function  |Libraries Needed: | Input    | Output                            |
| :-------- | :------- | :-------------------------------- | :-------------------------------- |
| `box_yolo(image, only_people)`       | [cv2](https://pypi.org/project/opencv-python/) <br> [numpy](https://numpy.org)| **image** `path`: path to the image <br> **only_people** `bool`: If True only people would be detected | **image** `image`: the image with object detection bounding boxes|
| `pose_mediapipe(image, segmentation)`      |[MediaPipe](https://google.github.io/mediapipe/getting_started/install.html) <br> [Numpy](https://numpy.org)  | **image** `path`: path to the image <br> **segmentation** `bool`: If True the person in the closest proximity to the camera is segmented| **annotated_image** `image`: the image with the pose of person in the closest proximity to the camera detected|
| `both(image_, only_people)`      |[cv2](https://pypi.org/project/opencv-python/) <br> [MediaPipe](https://google.github.io/mediapipe/getting_started/install.html) <br> [cv2](https://pypi.org/project/opencv-python/) |  **image** `path`: path to the image <br> **only_people** `bool`: If True only people would be detected | **annotated_image** `image`: object detection bounding boxes and the with the pose of person in the closest proximity to the camera detected |
| `model_picker(image, model, segmentation, only_people)`       |_none_  | **image** `path`: path to the image <br> **model** `int`: 0 for object detection, 1 for pose estimation, 2 for both <br> **segmentation** `bool`: If True the person in the closest proximity to the camera is segmented <br> **only_people** `bool`: If True only people would be detected | **result** `func`: calls the model chosen to be used in the web app|

### Video Pipeline
