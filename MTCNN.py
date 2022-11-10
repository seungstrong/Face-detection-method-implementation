from mtcnn import MTCNN
import cv2
import numpy as np
import time

detector = MTCNN()

cap = cv2.VideoCapture('20221109_172346.mp4')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width,height))
start = time.time()

cnt = 0
while cap.isOpened():
  ret,frame = cap.read()
  if not ret :
        print("CAM NOT OPEND") 
        break
  
  now_time = time.time() - start
  text = "Running Time :"+str(int(now_time))
  faces = detector.detect_faces(frame)
  for face in faces:
        score = face["confidence"]
        x, y, w, h = face["box"]
        save_img = frame[y:y+h, x:x+w]
        save_img = cv2.resize(save_img, dsize=(112,112),interpolation=cv2.INTER_AREA)

        cv2.imwrite('saved/{0}.jpg'.format(cnt),save_img)
        cnt+=1
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
      
  cv2.putText(frame, text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0), 1)
  out.write(frame)
  cv2.imshow('camera',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break
out.release()
cap.release()