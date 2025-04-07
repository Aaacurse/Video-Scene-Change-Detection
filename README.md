
# Video Scene Change Detection

This Streamlit web app detects scene changes in an uploaded video by analyzing the histogram differences between consecutive frames using OpenCV. The app provides:

* Scene change timestamps
* A downloadable .txt file of results
* A simple interface for uploading and processing videos

## Features
* Upload videos (.mp4, .avi, .mov)
* Scene change detection using histogram correlation
* Timestamps formatted as hh:mm:ss.ss
* Downloadable result file (scene_changes.txt)

## Technologies Used
* Python
* OpenCV
* Streamlit


## Installation

#### Clone the Repository

```bash
git clone https://github.com/yourusername/scene-change-detector.git
cd scene-change-detector
```
#### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py

```

