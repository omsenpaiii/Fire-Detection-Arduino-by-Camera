
# Fire Detection with Arduino and Camera

## Overview

**Fire-Detection-Arduino-by-Camera** is a project that uses a camera to detect flames based on brightness changes and color characteristics. When a flame is detected, a bounding box is drawn around it in the video feed, and a signal is sent to an Arduino to activate a buzzer as an alarm.

## Features

- Real-time fire detection using computer vision.
- Sends a signal to an Arduino to activate a buzzer when fire is detected.
- Visual representation of detected flames with bounding boxes.

## Getting Started

Follow the instructions below to set up the project on your local machine.

### Hardware Requirements

- Arduino board (e.g., Arduino Uno)
- Buzzer
- Camera (USB webcam or built-in laptop camera)
- Jumper wires for connections

### Software Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- PySerial (`pyserial`)
- PyFirmata (`pyfirmata`)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/omsenpaiii/Fire-Detection-Arduino-by-Camera.git
   cd Fire-Detection-Arduino-by-Camera
   ```

2. **Install required Python packages**:
   Make sure you have Python installed, then run:
   ```bash
   pip install opencv-python pyserial numpy pyfirmata
   ```

3. **Set up Arduino**:
   - Connect the buzzer to a digital pin on the Arduino (e.g., pin 4).
   - Upload the Arduino sketch included in this repository (see Arduino code section below).

4. **Edit Arduino Library Code (if necessary)**:
   - If you're using the PyFirmata library to interface with the Arduino, ensure that the Firmata firmware is uploaded to your Arduino board. This can be done via the Arduino IDE:
     - Open the Arduino IDE.
     - Go to **File > Examples > Firmata > StandardFirmata**.
     - Upload the **StandardFirmata** sketch to your Arduino.

## Usage

1. **Run the Python script**:
   - Ensure your camera is connected and recognized by your operating system.
   - Modify the line in the Python code to specify the correct COM port for your Arduino in the `buzzer.ino` file:
   ```python
   arduinoData = serial.Serial('COM11', 9600)  # Change to your actual COM port
   ```

2. **Run the script provided in the repository as `main.py`**.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- OpenCV for the computer vision functionalities.
- Arduino for the microcontroller platform.
- PyFirmata for interfacing with the Arduino board.
