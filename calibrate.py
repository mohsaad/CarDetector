# Mohammad Saad
# 2/28/2015
# TO use, put the camera in the spots you want to track, and then 
# run the script. Then mark the images with the corners of the parking spot, and run 
# 


import cv2
import imutils



def getImage(camera):
	retval, im = camera.read()
	return im


def main():
	camera_port = 0
	cam = cv2.VideoCapture(camera_port)

	img = getImage(cam)
	cv2.imwrite("calibrate.png", img)
	del(cam)

def draw


if __name__ == '__main__':
	main()

