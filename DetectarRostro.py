import cv2
import numpy as np

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image=cv2.imread('kianu.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces= faceClassif.detectMultiScale(image,
	scaleFactor=1.1,
	minNeighbors=8,
	minSize=(40,40),
	maxSize=(250,250))

for (x,y,w,h) in faces:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)


cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
