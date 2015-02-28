# Mohammad Saad
# 2/28/2015
# A graphical application for manually calibrating the points at which the 
# camera sees a parking space
# Created for HackIllinois 2015


import pygame
import cv2
import numpy as np
import os



def loadImage(string):
	screen = pygame.image.load(string)
	return screen

def sizeImage(string):
	img = cv2.imread(string)
	(width, height, depth) = img.shape
	del(img)
	return (width, height, depth)


def writeCoords(x,y,nline = False,reset = False):
	if(reset == True):
		os.remove("coords.txt")	
		return

	coords = open("coords.txt", 'a')
	if(nline):
		coords.write("-\n")
	else:
		c1 = str(x) + "," + str(y) +"\n"
		coords.write(c1)
	
	coords.close()




def main():
	pygame.init()
	image = loadImage("calibrate.png")
	(x,y,z) = sizeImage("calibrate.png")

	pygame.display.set_caption("Stuff")
	screen = pygame.display.set_mode((y,x))


	clock = pygame.time.Clock()
	keepGoing = True
	cColor = (0,0,255)

	screen.blit(image, (0, 0))
	while keepGoing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				keepGoing = False
			elif pygame.mouse.get_pressed() == (1,0,0):
				(xn, yn) = pygame.mouse.get_pos()
				print (xn,yn)
				writeCoords(xn,yn,False, False)
				pygame.draw.circle(screen, cColor,(xn,yn), 10,0)

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					# define new parking space
					print "-"
					writeCoords(0,0,True, False)
				elif event.key == pygame.K_r:
					writeCoords(0,0,False, True)

		

		pygame.display.flip()
		clock.tick(100)

if __name__ == '__main__':
	main()
