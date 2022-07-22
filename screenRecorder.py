from datetime import datetime
from time import strftime
from PIL import ImageGrab
import numpy
import cv2
from win32api import GetSystemMetrics


width = GetSystemMetrics(0)
height = GetSystemMetrics(1) 
time_stamp = datetime.now(),strftime('%Y-%m-%d %H-%M-%S')
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
videoName = f'{time_stamp}.mp4'
captured_video = cv2.VideoWriter(videoName,fourcc,20.0,(width,height))
webcam = cv2.VideoCapture(0)   # if you have another  cam apart from the build in then write 1 in place of 0
while True:
    img=ImageGrab.grab(bbox=(0,0,width,height))
    img_np= numpy.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    _,frame = webcam.read()
    frame_height ,frame_width,_= frame.shape
    img_final[0:frame_height,0:frame_width,:]= frame[0:frame_height,0:frame_width,:]
    
    cv2.imshow('screenRecorder',img_final)
    #cv2.imshow('webcam',frame)
    captured_video.write(img_final)
    
    if cv2.waitKey(10) == ord('q'):
        break
    

