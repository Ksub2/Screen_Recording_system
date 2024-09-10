from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

#screen dimensions
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

#timestamp for the video file name
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
file_name = f'{time_stamp}.mp4'

# video writer for screen recording
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

#camera capture
camera = cv2.VideoCapture(0)

#camera resolution 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Original camera feed width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Original camera feed height

# Checking if the camera is opened successfully
if not camera.isOpened():
    print("Error: Could not open camera")
    exit()


cv2.namedWindow('Your PC has been hacked!!!!!', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Your PC has been hacked!!!!!', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

resize_width = 300 
resize_height = 200  

while True:
    # Capture screen
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    
    # Capture camera frame
    ret, frame = camera.read()
    

    if not ret:
        print("Error: Failed to capture frame from camera")
        break
    
    resized_frame = cv2.resize(frame, (resize_width, resize_height))
    
    img_final[0:resize_height, 0:resize_width, :] = resized_frame

    cv2.imshow('Your PC has been hacked!!!!!', img_final)
    
    # Write the combined frame to the video file
    captured_video.write(img_final)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(10) == ord('q'):
        break

# Release resources
camera.release()
captured_video.release()
cv2.destroyAllWindows()
