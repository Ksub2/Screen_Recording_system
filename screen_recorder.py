from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

time_stamp= datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name=f'{time_stamp}.mp4'

# print(width,height)
fourcc=cv2.VideoWriter_fourcc('m','p','4','v')
captured_video=cv2.VideoWriter(file_name,fourcc,20.0,(width,height))


camera=cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH,3000)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT,1500)
if not camera.isOpened():
    print("Error could not open camera")
    exit()

cv2.namedWindow('Your PC has been hacked!!!!!', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Your PC has been hacked!!!!!', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


while True:
    img=ImageGrab.grab(bbox=(0,0,width,height))
    img_np=np.array(img)
    img_final=cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    ret, frame=camera.read()
    if not ret:
        print("Error failed to capture")
        break
    frame_height,frame_width,_=frame.shape
    img_final[0:frame_height,0:frame_width,:]=frame[0:frame_height,0:frame_width,:]
    cv2.imshow('Your PC has been hacked!!!!!',img_final)
    
    
    # cv2.imshow('camera',frame)
    captured_video.write(img_final)
    if cv2.waitKey(10)==ord('q'):
        break
camera.release()
captured_video.release()
cv2.destroyAllWindows()