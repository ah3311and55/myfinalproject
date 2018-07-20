# Globals

"""
Breakout game. Implemented using pygame. 

Bouncing and movement functions taken from this particle simulation: http://www.petercollingridge.co.uk/book/export/html/6.
"""

print("hello world")

import pygame
import math
import breakout
import constants

""" 
Paddle: Methods
"""
# Update the position of the paddle. It is confined to the boundaries
# of the screen
def paddle_update_position(paddle):
    pass

"""
Ball: Methods
"""

# This function must update the coordinates of the ball and changes the 
# direction of the ball bounces of either the left, top, or right walls 
def ball_update_position(ball):
    pass
    #TODO

# This function must change the direction of the ball when it hits an 
# object 
def ball_bounce_off(ball):
    pass


"""
Screen Update: Methods
"""
# This function must render all objects on screen using breakout.py draw 
# methods. No objects should be created in this method. 
def draw_objects():
    breakout.clear_screen()

    # Draw the paddle, ball, and wall of bricks
    # TODO

    # Tell pygame to actually redraw everything (DON'T CHANGE)
    pygame.display.flip()


# This function must create the set of bricks to be drawn at the top of 
# the screen. 
# This function returns a list of bricks created. 
def build_bricks():
    # Create an empty list
    # TODO 

    # Create the bricks and add them to list
    # Hint: You need a double for loop to draw the set of bricks on top of the screen. 
    # Set the brick color based on row number by using the colors in the constants.py
    # file. (You can add other colors if you wish). When you create a new brick and 
    # set the x,y, and color using breakout.py methods, add your brick to the list.
    # TODO 

    pass



# Creating the screen 
breakout.build_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

# Create the ball, paddle, and bricks here using breakout.py functions.
# TODO


# These are variables used to detect the state of the game. 
running = True
start = False


while running:

    # Setup the mouse events 
    # DO NOT change this code
    for event in pygame.event.get():
        # If you click the mouse, the ball will start moving 
        if pygame.mouse.get_pressed() == (1, 0, 0):
            start = True 
        if event.type == pygame.QUIT:
            running = False


    if start == True:
        # Make the ball update its position. 
        pass

    # Update the position of the paddle based on the mouse
    # TODO 
        
    # Check for collisions using breakout.ball_did_collide_with(ball, obj, width, height) 
    # TODO 

    # If ball hits the bottom wall, we lose.
    # TODO 

    # If bricks are all broken, you won! 
    # TODO 

    # Else, loop through the entire bricks list to see if the ball collided with any brick 
    # TODO 

    # Redraw everything at the end of the while loop
    draw_objects()

pygame.display.update()






































import pygame
import constants
import random 



"""
Paddle: A class to represent the paddle
"""

class Paddle(object):

    def __init__(self):
        self.x = (constants.SCREEN_WIDTH - constants.PADDLE_WIDTH) / 2
        self.y = constants.SCREEN_HEIGHT - constants.GAP - constants.PADDLE_HEIGHT
        self.width = constants.PADDLE_WIDTH
        self.height = constants.PADDLE_HEIGHT
        self.x_velocity = 0
        self.color = constants.PADDLE_COLOR

"""
Ball: A class to represent the ball
"""
class Ball(object):

    def __init__(self):
        self.radius = constants.BALL_RADIUS
        velocity_list = [10, -10]
        self.x_velocity = random.choice(velocity_list)
        self.y_velocity = 10
        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2
        self.color = constants.BALL_COLOR;


"""
Brick: A class to represent the brick
"""
class Brick(object):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = constants.BRICK_WIDTH
        self.height = constants.BRICK_HEIGHT
        self.color = constants.BRICK_COLOR


def create_new_ball():
	return Ball()

def create_new_paddle():
	return Paddle()

def create_new_brick():
	return Brick()

# Get Methods 

def get_x(self):
    return self.x

def get_y(self):
    return self.y

def get_width(self):
    return self.width

def get_height(self):
    return self.height

def get_x_velocity(self):
    return self.x_velocity

def get_y_velocity(self):
    return self.y_velocity 

def get_radius(self):
    return self.radius 


def get_color(self):
    return self.color 

# Set Methods 

def set_x(self, x):
    self.x = x

def set_y(self, y):
    self.y = y

def set_width(self, w):
    self.width = w

def set_height(self, h):
    self.height = h

def set_x_velocity(self, v):
    self.x_velocity = v

def set_y_velocity(self, v):
    self.y_velocity = v

def set_radius(self, r):
    self.radius = r

def set_color(self, c):
    self.color = c

def clamp(n, min_n, max_n):
    return max(min(max_n, n), min_n)

def draw_rectangle(x, y, width, height, color):
	pygame.draw.rect(screen, color, (x, y, width, height))

def draw_circle(x, y, radius, color):
	pygame.draw.circle(screen, color, (int(x), int(y)), radius)

def draw_image(x, y, filename):
    im = pygame.image.load(filename)
    screen.blit(im, (x, y))

def draw_text(x, y, text, color, size):
    myfont = pygame.font.SysFont("monospace", size)
    # render text
    label = myfont.render(text, 1, color)
    screen.blit(label, (x, y))

def get_mouse_location():
    return pygame.mouse.get_pos();


# This function creates the window for the game. It should be called at
# the beginning of your program.
def build_screen(width, height):
	pygame.init()
	global screen
	screen = pygame.display.set_mode((width, height))


# This function wipes the screen clean by filling it with a color.
# This lets you draw new objects, or make objects look like they've moved.
def clear_screen():
	screen.fill(constants.SCREEN_COLOR)

# Check and see if the ball and another obj collided with each other 
def ball_did_collide_with(ball, obj, width, height):
    dist = 1.41*get_radius(ball)
    if (int(get_x(ball) - dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) - dist) in range(get_y(obj), get_y(obj) + height)) \
    or (int(get_x(ball) + dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) - dist) in range(get_y(obj), get_y(obj) + height)) \
    or (int(get_x(ball) + dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) + dist) in range(get_y(obj), get_y(obj) + height)) \
    or (int(get_x(ball) - dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) + dist) in range(get_y(obj), get_y(obj) + height)): 
        return True 
    return False
