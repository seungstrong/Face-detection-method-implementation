import numpy as np
import os
import cv2
import time

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('test.mp4')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('Haar_result.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width,height))
start = time.time()
cnt = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret :
        print("CAM NOT OPEND")
        break
    
    now_time = time.time() - start
    text = "Running Time :"+str(int(now_time))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.2, 7)
    for (x,y,w,h) in faces:
        save_img = frame[y:y+h, x:x+w]
        #save_img = save_img + 50
        really_save_img = cv2.resize(save_img, dsize=(112,112),interpolation=cv2.INTER_AREA)
        cv2.imwrite('saved/{0}.jpg'.format(cnt), really_save_img)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cnt += 1
    cv2.putText(frame, text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0), 1)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
out.release()
cap.relase()



