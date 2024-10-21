import serial
import time
import numpy as np
import cv2

arduinoData = serial.Serial('COM11', 9600)  # Use your actual COM port here

def send_fire_detection_signal():
    # Send a signal to Arduino when fire is detected
    arduinoData.write(b'1\r')  # Sending '1' to indicate fire detected
    print("Fire detected!")

# Start capturing video from the camera
capture = cv2.VideoCapture(0)  # Change the number for the camera that you are using

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("Failed to capture frame.")
        break

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range for detecting fire color in the HSV space
    lower_fire = np.array([0, 100, 100])  # Lower bound of fire color in HSV
    upper_fire = np.array([10, 255, 255])  # Upper bound of fire color in HSV

    # Create a mask to extract the fire regions
    fire_mask = cv2.inRange(hsv, lower_fire, upper_fire)

    # Find contours of the detected fire areas
    contours, _ = cv2.findContours(fire_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fire_detected = False  # Flag to check if fire is detected
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter out small areas
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)  # Draw rectangle around fire
            send_fire_detection_signal()  # Send signal to Arduino
            fire_detected = True

    # Show the video feed with detection boxes
    cv2.imshow('Video', frame)

    # Stop the program when 'd' is pressed
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# Release resources
capture.release()
cv2.destroyAllWindows()
