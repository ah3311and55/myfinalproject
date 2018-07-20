import pygame
import sys
import time
import random
import breakout

from pygame.locals import *
#variables
score1=0
score2=0
WHITE = (255, 255, 255)
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
score1_color=BLUE
score2_color=RED
ball_color=GREEN

ball_radius=25
paddle1_y=225
paddle2_y=225
paddle1_x=12
paddle2_x=868
xdirection="forward"
ydirection="upward"
x=450
y=300
first_x=450
first_y=300
running=False
screen_width=900
screen_height=600
x_velocity=random.randint(1,2)
y_velocity=random.randint(1,2)
#SCREEN
pygame.init()
pygame.display.set_caption("paddles game")
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(BLACK)
 
#FUNCTIONS

def draw_rectangle(x, y, width, height, color):
	pygame.draw.rect(screen, color, (x, y, width, height))
def draw_circle(x, y, radius, color):
	pygame.draw.circle(screen, color, (int(x), int(y)), radius)
ball=draw_circle(x,y,ball_radius,GREEN)
def result():
	myfont = pygame.font.SysFont("monospace", 100)
	label = myfont.render(str(score1),1,score1_color)
	screen.blit(label, (20, 30))
	myfont = pygame.font.SysFont("monospace", 100)
	label = myfont.render(str(score2),1,score2_color)
	screen.blit(label, (830, 30))
def return_ball(x,y,running):
	if x >= screen_width+ball_radius :
		x = first_x
		y = first_y
		running = False
		draw_circle(first_x,first_y,ball_radius,ball_color)
	if x <= 0-ball_radius:
		x = first_x
		y = first_y
		running=False
		draw_circle(first_x,first_y,ball_radius,ball_color)
	return x,y,running
	#if player 1 or player 2 scored return ball to the middle


while True:
	keys = pygame.key.get_pressed()
	screen.fill(BLACK)
	#PADDLE1
	paddle1=draw_rectangle(paddle1_x,paddle1_y,20,150,BLUE)
	#PADDLE2
	paddle2=draw_rectangle(paddle2_x,paddle2_y,20,150,RED)
	#BALL
	if keys[pygame.K_o]:
		running=True

	if keys[pygame.K_i]:
		running=False
	if running==True:
		draw_circle(x,y,ball_radius,ball_color)
		if (ydirection=="upward"):
			y=y-y_velocity
			
			if (y<=ball_radius):
				ydirection="downward"
		if (ydirection=="downward"):
			y=y+y_velocity
			
			if (y>=screen_height-ball_radius):
				ydirection="upward"
		if (xdirection=="forward"):
			x=x+x_velocity
		
			if y>=paddle2_y and y<=paddle2_y+150 and x==paddle2_x:
				xdirection="backward"
				y_velocity = random.randint(1,2)
				x_velocity = random.randint(1,2)
				crash_sound =pygame.mixer.Sound("crash.wav")
				pygame.mixer.Sound.play(crash_sound)
				pygame.mixer.music.load("cartoon130.mp3")
				pygame.mixer.music.play(0)
		if (xdirection=="backward"):
			x=x-x_velocity	
			if y>=paddle1_y and y<=paddle1_y+150 and x==paddle1_x+20:
				xdirection="forward"
				y_velocity = random.randint(1,2)
				x_velocity = random.randint(1,2)
		x,y,running=return_ball(x,y,running)
		#paddle1 bouncing

	if x== screen_width:
		score1+=1
	if x== 0:
		score2+=1
	if score1 ==5:
		score2_color=BLUE
		ball_color=BLUE
		screen.fill(BLUE)
		myfont = pygame.font.SysFont("monospace", 100)
		label = myfont.render("BLUE WINS!",1,WHITE)
		screen.blit(label, (175, 250))
	if score2 == 5:
		score1_color=RED
		ball_color=RED
		screen.fill(RED)
		myfont = pygame.font.SysFont("monospace", 100)
		label = myfont.render("RED WINS!",1,WHITE)
		screen.blit(label, (250, 250))		

	draw_circle(x,y,ball_radius,ball_color)
	if keys[pygame.K_w]:
		if paddle1_y >= 10:
			paddle1_y -=2
	if keys[pygame.K_s]:
		if paddle1_y <= 440:
			paddle1_y +=2
	if keys[pygame.K_UP]:
		if paddle2_y >= 10:
			paddle2_y -=2
	if keys[pygame.K_DOWN]:
		if paddle2_y <= 440:
			paddle2_y +=2
		
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			#### Respond to events
			

	#### Make animations
	
	#### Update display
	if keys[pygame.K_r]:
		score1=0
		score2=0
		ball_color=GREEN
		score1_color=BLUE
		score2_color=RED
	result()
	pygame.display.update()
	time.sleep(0.001)

