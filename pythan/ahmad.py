import pygame
import sys
import time
from pygame.locals import *
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_s = 500
SCREEN_HEIGHT = 400
SQUARE_SIDE_LEN = 200
pygame.init()
pygame.display.set_caption("Animated Square")
screen = pygame.display.set_mode((SCREEN_s, SCREEN_HEIGHT))
x = 40
y=170
pygame.draw.circle(screen,WHITE,(x,y),40,0)
ydirection = "upward"
direction = "forward"
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	screen.fill(BLACK)
	if direction == "forward":
		x = x + 3
		if (x >= 450):
			direction = "backward"
	elif direction == "backward":
		x= x - 5
		if x <= 50:
			direction ="forward"
	if ydirection==  "up":
		y = y-5
		if y <= 50:
			ydirection = "down"
	elif ydirection=="down":
		y=y+5
		if y >= 350:
			ydirection = "up"



	pygame.draw.circle(screen,WHITE,(x,y),40,0)
	#### Update display
	pygame.display.update()
	time.sleep(0.01)