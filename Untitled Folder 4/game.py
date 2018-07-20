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
    bricks=[]
    print("hi")
    for i in range(constants.BRICKS_PER_ROW):
        x=(i+1)
        brick = breakout.create_new_brick()
        breakout.set_x(brick, (i+1)*constants.GAP + i * constants.BRICK_WIDTH)
        breakout.set_y(brick, 0)
        breakout.set_color(brick,constants.RED)
        bricks.append(brick)
    return bricks
bricks=build_bricks()



    # Create the bricks and add them to list

    # Hint: You need a double for loop to draw the set of bricks on top of the screen.
    # Set the brick color based on row number by using the colors in the constants.py
    # file. (You can add other colors if you wish). When you create a new brick and
    # set the x,y, and color using breakout.py methods, add your brick to the list.
    # TODO 




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
