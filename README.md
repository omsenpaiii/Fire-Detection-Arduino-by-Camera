# Fire Detection with Arduino and Camera

## Overview

**Fire-Detection-Arduino-by-Camera** is a project that uses a camera to detect flames based on brightness changes and color characteristics. When a flame is detected, a bounding box is drawn around it in the video feed, and a signal is sent to an Arduino to activate a buzzer as an alarm.

## Features

- Real-time fire detection using computer vision.
- Sends a signal to an Arduino to activate a buzzer when fire is detected.
- Visual representation of detected flames with bounding boxes.

## Requirements

### Hardware

- Arduino board (e.g., Arduino Uno)
- Buzzer
- Camera (USB webcam or built-in laptop camera)
- Jumper wires for connections

### Software

- Python 3.x
- OpenCV (`opencv-python`)
- PySerial (`pyserial`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Fire-Detection-Arduino-by-Camera.git
   cd Fire-Detection-Arduino-by-Camera
