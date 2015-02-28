# Mohammad Saad
# 2/27/2015
# Uses calibrate.png as our reference image. 
# Uses 4-point perspective transform in OpenCV to check whether a car is
# in the specified space or not
# 4-point transform with assistance from Adrian Rosebrock
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
			if line == "-" or line == "":
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
	rect = np.zeros(4,2),dtype = 'float32')
	
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]


	diff = np.diff(pts, axis=1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]

	return rect

