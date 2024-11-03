# MagicMouse

Welcome to **MagicMouse**! This project uses computer vision and hand-tracking to control your mouse movements with gestures, making it a unique way to interact with your computer.

### Project URL
[GitHub Repository - MagicMouse](https://github.com/Osank31/MagicMouse.git)

---

## Overview

MagicMouse is an AI-based virtual mouse controller using OpenCV and MediaPipe. By tracking hand landmarks, it moves the mouse and performs clicks based on hand gestures. This project is an innovative approach to control devices using only hand gestures, providing an intuitive and touch-free interaction experience.

## Features

- Tracks hand movements to control the mouse pointer on the screen
- Clicks by detecting gestures (e.g., bringing the index finger and thumb together)
- Real-time hand tracking with minimal latency
- Customizable sensitivity to adapt to different screen resolutions

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- pynput

Install dependencies using:
```bash
pip install opencv-python mediapipe pynput
```

## Modules

### HandDetectorModule.py
This module contains the `HandDetector` class, which:
- Initializes MediaPipe for hand tracking
- Finds hands in the video feed
- Extracts coordinates of landmarks for use in gesture recognition

### handtracking.py
This script:
- Captures video from the webcam
- Tracks hand landmarks and translates them to screen coordinates
- Moves the mouse and performs click actions based on gestures

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/Osank31/MagicMouse.git
    ```
2. Run `handtracking.py` to start the hand-tracking:
    ```bash
    python handtracking.py
    ```
3. Use gestures to control the mouse! Move your index finger to move the mouse, and bring your index finger and thumb together to click.

### Example Gesture
- **Click**: Bring the thumb and index finger close together to trigger a left mouse click.

## Future Enhancements

- Add more gestures for right-click and scroll
- Improve detection accuracy in different lighting
- Implement custom sensitivity settings for various resolutions

## Notes

This is my first AI project, designed to make interacting with computers more accessible and engaging.
