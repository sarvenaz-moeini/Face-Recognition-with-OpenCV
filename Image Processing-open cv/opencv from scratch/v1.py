import cv2
cap=cv2.VideoCapture(0)
while(True):
  ret,frame=cap.read()
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  cv2.imshow('webcam',gray)
  if cv2.waitKey(1) & 0XFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()
  
