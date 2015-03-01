# Mohammad Saad
# 2/28/2015
# Overall Detection System

import cv2
import numpy as np
import check_space as check
import detect_space as detect
import requests
import time
import json

def takeImage(cam):
	img = cam.read()
	cv2.imwrite("temp_out.png", img[1])
	return img
def cam_setup(camera_port):
	return cv2.VideoCapture(camera_port)

def checkImage(filename):
	diff_vals = check.checkDiff(filename)
	return diff_vals

def update_server(diff_vals):
        url = "http://parkd.abrarsyed.me/api/0.1/cameraPush"
        url2 = "172.17.35.145:12345"
        openArr = []
	closedArr = []
	a = 0
	for i in diff_vals:
            if i == 0:
                openArr.append(a)
            else:
                closedArr.append(a)
            
            a += 1
        
        json_obj = '{"open":'+ str(openArr) + ',"closed":' + str(closedArr) + '}'
        print json_obj
	
        
        r = requests.post(url,data=json_obj)
        print r.status_code
	a = 0


def main():
	cam = cam_setup(0)

	while True:

		img2 = takeImage(cam)
		diff = checkImage(img2)
    
		del(img2)
		update_server(diff)
		#print diff

		time.sleep(10)


def test():
	#change when needing to compare pictures
	
	link = "threecar.jpg"
	img = cv2.imread(link)
    
        

	d = checkImage(link)
	
	update_server(d)
	print d



if __name__ == '__main__':
	test()
