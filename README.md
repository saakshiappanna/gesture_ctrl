# Gesture Control with Hand Tracking

This project uses OpenCV, MediaPipe, and Pycaw to control system volume using hand gestures detected via webcam.

## Dependencies

- opencv-python
- mediapipe
- pycaw
- comtypes
- numpy

Install dependencies with:
```sh
conda activate cv_mediapipe
pip install opencv-python mediapipe pycaw comtypes numpy
```

## Main Files

- **Module:** [`HandTrackingModule.py`](HandTrackingModule.py)
- **Executable:** [`VolumeHandControl.py`](VolumeHandControl.py)

## Usage

Run the main script to control system volume with your hand:
```sh
python VolumeHandControl.py
```

## Notes

- Make sure your webcam is connected.
- For Windows only (uses pycaw for audio control).
