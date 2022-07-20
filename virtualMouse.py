import cv2
import pyautogui
from cv2 import imshow
from matplotlib.pyplot import pink
import mediapipe as mp
cap = cv2.VideoCapture(0)
hand_detector =mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width,screen_height= pyautogui.size()
index_y=0
while True:
    _,frame = cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_widht,_ =frame.shape
    rgd_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgd_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
               x=int(landmark.x*frame_widht)
               y =int(landmark.y*frame_height)
              # print(x,y)
               if id==8:
                   cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                   index_x= screen_width/frame_widht*x
                   index_y= screen_height/frame_height*y
                   pyautogui.moveTo(index_x,index_y)
               if id==4:
                   cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                   thumb_x= screen_width/frame_widht*x
                   thumb_y= screen_height/frame_height*y   
                   print('outside',abs(index_y-thumb_y))
                   if abs(index_y-thumb_y)<50:
                        #print('Click')
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow('Virtual Mouse',frame)
    cv2.waitKey(1)
    