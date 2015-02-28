# Mohammad Saad
# An algorithm for detecting whether the selected parking space has a car in it or not
import cv2
import imutils
import argparse
import numpy as np





ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "path to image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
orig = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
minLineLength = 100
maxLineGap = 10

lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength, maxLineGap)

for x1,y1,x2,y2 in lines[0]:
	cv2.line(image,(x1,y1),(x2,y2), (0,255,0),2)





#sift = cv2.SIFT()
#kp = sift.detect(gray, None)

#img = cv2.drawKeypoints(gray, kp)

cv2.imshow("Keypoints", image)
cv2.waitKey()




#gray = cv2.GaussianBlur(gray, (5,5), 0)
#edged = cv2.Canny(gray, 75, 200)

#cv2.imshow("Edge", edged)
#cv2.waitKey(0)

