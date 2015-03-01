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
		print arr[i]
		warped = detect_space.persp_transform(image[1], arr[i])
		img_list.append(warped)
		i += 1

	total_img = i
	i = 0

	diff_vals = []
	while i < total_img:
		img2 = cv2.imread(str(i) + ".png")
		temp = abs(diffImage(img_list[i], img2))
		diff_vals.append(isOccupied(temp))
		i += 1

	return diff_vals

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




