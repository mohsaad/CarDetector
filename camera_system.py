# Mohammad Saad
# 2/28/2015
# Overall Detection System

import cv2
import numpy as np
import check_space as check
import detect_space as detect
import requests
import time

def takeImage(cam):
	return cam.read()

def cam_setup(camera_port):
	return cv2.VideoCapture(camera_port)

def checkImage(image):
	diff_vals = check.checkDiff(image)
	return diff_vals

def update_server(diff_vals):
	# do stuff...
	a = 0

def main():
	cam = cam_setup(0)

	while True:
		img = takeImage(cam)
		diff = checkImage(img)
		update_server(diff)
		print diff

		time.sleep(60)


def test():
	#change when needing to compare pictures
	link = "twocar.jpg"
	img = cv2.imread(link)
	d = checkImage(img)
	print d

if __name__ == '__main__':
	main()
