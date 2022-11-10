import dlib
import cv2
import numpy as np
import time

detector = dlib.get_frontal_face_detector()

cap = cv2.VideoCapture('test.mp4')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('Dlib_result.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width,height))
start = time.time()
cnt = 0
while cap.isOpened():
  ret,frame = cap.read()
  if not ret :
        print("CAM NOT OPEND") 
        break
  
  now_time = time.time() - start
  text = "Running Time :"+str(int(now_time))
  #frame = cv2.flip(frame,0)
  faces = detector(frame)
  for face in faces:
      try:
        save_img = frame[face.top():face.bottom(),face.left():face.right()]
        really_save_img = cv2.resize(save_img, dsize=(112,112),interpolation=cv2.INTER_AREA)
        cv2.imwrite('saved/{0}.jpg'.format(cnt), really_save_img)
        cv2.rectangle(frame,(face.left(),face.top()),(face.right(),face.bottom()),(0,0,255),2)
        cnt += 1
      except Exception as e:
          print(str(e))

  cv2.putText(frame, text, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 0, 0), 1)
  out.write(frame)
  cv2.imshow('camera',frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
          cv2.destroyAllWindows()
          break
out.release()
cap.release()