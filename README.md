
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
git clone https://github.com/Aaacurse/Video-Scene-Change-Detection.git
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



## Project Images
![Home Page](https://github.com/Aaacurse/Video-Scene-Change-Detection/blob/13042a48fd85cf55eb5dee46b1bdb7bc2f4761c7/demo_photos/Home%20Page.png)
![Browse Video](https://github.com/Aaacurse/Video-Scene-Change-Detection/blob/13042a48fd85cf55eb5dee46b1bdb7bc2f4761c7/demo_photos/Browse%20Video.png)
![Video Processing](https://github.com/Aaacurse/Video-Scene-Change-Detection/blob/13042a48fd85cf55eb5dee46b1bdb7bc2f4761c7/demo_photos/Video%20Processing.png)
![Output](https://github.com/Aaacurse/Video-Scene-Change-Detection/blob/13042a48fd85cf55eb5dee46b1bdb7bc2f4761c7/demo_photos/Output.png)
![Download Result](https://github.com/Aaacurse/Video-Scene-Change-Detection/blob/13042a48fd85cf55eb5dee46b1bdb7bc2f4761c7/demo_photos/Download%20Result.png)

