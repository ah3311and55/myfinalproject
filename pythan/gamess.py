import pygame
import sys
import time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Basics")
screen = pygame.display.set_mode((500,400))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    time.sleep(0.001)