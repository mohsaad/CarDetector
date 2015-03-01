# Mohammad Saad
# 2/27/2015
# Uses calibrate.png as our reference image. 
# Uses 4-point perspective transform in OpenCV to check whether a car is
# in the specified space or not
# 4-point transform with assistance from Adrian Rosebrock (pyimagesearch.com)
# http://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/

import cv2
import imutils
import argparse
import numpy as np


def loadImageFromCamera(port):
	port = 0 # define method later, will use sample data for now


def loadCoords(filename):
	coordArray = []
	totalArray = []
	with open(filename) as f:
		for line in f:
			#print line
			if line == "-\n" or line == "":
				totalArray.append(coordArray)
				coordArray = []
			else:
				line = line.strip("\n") 
				pair = line.split(",")
				coordArray.append([int(pair[0]), int(pair[1])])
				#print coordArray


	totalArray.append(coordArray)
	return totalArray

def order_points(pts):
	# initialize array of zeros
	rect = np.zeros((4,2),dtype = 'float32')
	
	s = np.sum(pts, axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]


	diff = np.diff(pts, axis=1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	return rect

def persp_transform(image, pts):
	# order points
	rect = order_points(pts)
	(tl, tr, br, bl) = rect

	# get new width
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[0] - bl[0]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[0] - tl[0]) ** 2))
	maxWidth = max(int(widthA), int(widthB))

	# get new height
	heightA = np.sqrt(((tr[1] - br[1]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[1] - bl[1]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))

	# create a bird's eye view of the image
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

	# compute transform
	M = cv2.getPerspectiveTransform(rect, dst)
	#print image
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

	# return
	return warped



# main method, runs every time
def main():
        link = "onecar.jpg"
	img = cv2.imread(link)
	arr = loadCoords("coords.txt")
	i = 0
	for coords in arr:
		pts = np.array(arr[i], dtype = "float32")
		warped = persp_transform(img, pts)
		cv2.imwrite(str(i) +".png", warped)
		i += 1


	print "reference images calculated"


if __name__ == '__main__':
	main()