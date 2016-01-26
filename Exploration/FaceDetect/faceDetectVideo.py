import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/david/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)



while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
    		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)



	cv2.imshow('Video', frame)
	cv2.imshow('Video_gray', gray)
	cv2.imshow('Video_HSV', HSV)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
