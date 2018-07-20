import pygame
import sys
import time
from pygame.locals import *


# Define Constant Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

circle_WIDTH = 500
circle_WIDTH = 400
circle_WIDTH = 200

# Setup Screen
pygame.init()
pygame.display.set_caption("Animated Square")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Define Variables
x = 200
direction = "forward"

# Game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			#### Respond to events

	#### Make animation
	screen.fill(BLACK)
	if direction == "forward":
		x = x + 5
		if x >= (SCREEN_WIDTH - SQUARE_SIDE_LEN):
			direction = "backward"
	elif direction == "backward":
		x = x - 5
		if x <= 0:
			direction = "forward"
	pygame.draw.circle(screen, WHITE, (x, 150, SQUARE_SIDE_LEN, SQUARE_SIDE_LEN))

	#### Update display
	pygame.display.update()
	time.sleep(0.01)