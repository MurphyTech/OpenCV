import numpy as np 
import cv2



face_cascade = cv2.CascadeClassifier('/home/david/opencv/data/haarcascades/haarcascade_frontalface_default.xml')

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while(cap1.isOpened() and cap2.isOpened()):
	ret1, frame1 = cap1.read()
	ret2, frame2 = cap2.read()

	gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

	faces1 = face_cascade.detectMultiScale(gray1, 1.1, 5)
	faces2 = face_cascade.detectMultiScale(gray2, 1.1, 5)

	for (x,y,w,h) in faces1:
    		cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),2)

    	for (x,y,w,h) in faces2:
    			cv2.rectangle(frame2,(x,y),(x+w,y+h),(255,0,0),2)


	
	cv2.imshow('Cap1', frame1)
	cv2.imshow('Cap2', frame2)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap1.release()
cap2.release()
cv2.destroyAllWindows()
