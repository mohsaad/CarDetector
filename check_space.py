# Mohammad Saad
# 2/28/2015
# Checks an image against a reference image to see if a car is in the spot

import cv2
import numpy as np
import detect_space
import math

def checkDiff(image):

	arr = detect_space.loadCoords("coords.txt")
	img_list = []
	i = 0
	for a in arr:
		pts = np.array(arr[i], dtype = "float32")
		warped = detect_space.persp_transform(image, arr[i])
		img_list.append(warped)
		i += 1

	total_img = i
	i = 0

	img2 = cv2.imread("0.png")
	img3 = diffImage(img_list[0], img2)
	cv2.imshow("img3", img3)

def diffImage(img1, img2):
	grey1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	grey2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

	hist1 = cv2.calcHist([grey1], [0], None, [256], [0,256])
	hist2 = cv2.calcHist([grey2], [0], None, [256], [0,256])
	
	diff = cv2.compareHist(hist1,hist2,0)
	print diff
	return diff

def isOccupied(diff):
	if(abs(diff) < 0.7):
		return 1
	
	return 0





