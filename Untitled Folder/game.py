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
  
    location = breakout.get_mouse_location()
    mouse_x = location[0]
    if mouse_x >constants.SCREEN_WIDTH-constants.PADDLE_WIDTH:
        breakout.set_x(paddle,constants.SCREEN_WIDTH-constants.PADDLE_WIDTH)
        
    else: 
      breakout.set_x(paddle, mouse_x)

  
"""
Ball: Methods
"""

# This function must update the coordinates of the ball and changes the 
# direction of the ball bounces of either the left, top, or right walls 
def ball_update_position(ball):
    x=breakout.get_x(ball)
    y=breakout.get_y(ball)

    x_velocity=breakout.get_x_velocity(ball)
    y_velocity=breakout.get_y_velocity(ball)
    x = x + x_velocity
    y = y + y_velocity
    breakout.set_x(ball, x)
    breakout.set_y(ball, y)
    breakout.set_x_velocity(ball, x_velocity)
    breakout.set_y_velocity(ball, y_velocity)


    new_y_velocity=y_velocity
    new_x_velocity=x_velocity

    if x < 0 :
        x_velocity=breakout.get_x_velocity(ball)
        new_x_velocity=-1*x_velocity
    if y < 0 :
        y_velocity=breakout.get_y_velocity(ball)
        new_y_velocity=-1*y_velocity
    if x > constants.SCREEN_WIDTH:
        x_velocity=breakout.get_x_velocity(ball)
        new_x_velocity=-1*x_velocity
    
    breakout.set_x_velocity(ball, new_x_velocity)
    breakout.set_y_velocity(ball,new_y_velocity)
    breakout.set_x(ball, x)
    breakout.set_y(ball, y)
   #TODO

# This function must change the direction of the ball when it hits an 
# object 
def ball_bounce_off(ball):
  new_y_velocity = -1 * breakout.get_y_velocity(ball)
  breakout.set_y_velocity(ball, new_y_velocity)


"""
Screen Update: Methods
"""
# This function must render all objects on screen using breakout.py draw 
# methods. No objects should be created in this method. 
def draw_objects():
  breakout.clear_screen()
  x = breakout.get_x(paddle)
  y = breakout.get_y(paddle)
  width = breakout.get_width(paddle)
  height = breakout.get_height(paddle)
  color = breakout.get_color(paddle)
  breakout.draw_rectangle(x, y, width, height, color)

   # Draw the paddle, ball, and wall of bricks
   # TODO
  for brick in bricks:
    x = breakout.get_x(brick)
    y = breakout.get_y(brick)
    width = breakout.get_width(brick)
    height = breakout.get_height(brick)
    color = breakout.get_color(brick)
    breakout.draw_rectangle(x, y, width, height, color)



    x = breakout.get_x(ball)
    y = breakout.get_y(ball)
    radius = breakout.get_radius(ball)
    color = breakout.get_color(ball)
    breakout.draw_circle(x, y, radius, color)

   # Tell pygame to actually redraw everything (DON'T CHANGE)
  pygame.display.flip()


# This function must create the set of bricks to be drawn at the top of 
# the screen. 
# This function returns a list of bricks created. 
def build_bricks():
       # Create an empty list
       bricks = []
       for r in range (6):
         for i in range(constants.BRICKS_PER_ROW):
             x = (i+1)*(constants.GAP) + (i*constants.BRICK_WIDTH)
       # TODO
             brick = breakout.create_new_brick()
             breakout.set_x(brick, x)
             breakout.set_y(brick, (r)*25)
             breakout.set_color(brick, constants.RED)
             bricks.append(brick)
       return bricks


   # Create the bricks and add them to list
   # Hint: You need a double for loop to draw the set of bricks on top of the screen.
   # Set the brick color based on row number by using the colors in the constants.py
   # file. (You can add other colors if you wish). When you create a new brick and
   # set the x,y, and color using breakout.py methods, add your brick to the list.
   # TODO
   # for i in range():


   



# Creating the screen 
breakout.build_screen(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

# Create the ball, paddle, and bricks here using breakout.py functions.
# TODO
bricks = build_bricks()



# These are variables used to detect the state of the game. 
running = True
start = False
ball = breakout.create_new_ball()
paddle = breakout.create_new_paddle()
clock = pygame.time.Clock()
draw_objects()

pygame.display.update()
while running:
    

    for brick in bricks:

        if(breakout.ball_did_collide_with(ball,brick,breakout.get_width(brick),breakout.get_height(brick))):
            ball_bounce_off(ball)
            bricks.remove(brick)

        if len(bricks) == 0:
            print "win !"
        if (breakout.get_y(ball)> constants.SCREEN_HEIGHT - 5 and constants.NUM_LIVES < 0):
            print "lose !"
            running = False
        if (breakout.get_y(ball)> constants.SCREEN_HEIGHT - 5 and constants.NUM_LIVES > 0):
            breakout.set_y(ball, constants.SCREEN_HEIGHT/2)
            breakout.set_x(ball, constants.SCREEN_WIDTH/2)
            constants.NUM_LIVES = constants.NUM_LIVES - 1
            start = False




    # bricks = build_bricks()
    # If number of lives left is 0, break out of the while loop
    # TODO
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
        
        if(breakout.ball_did_collide_with(ball,paddle,breakout.get_width(paddle),breakout.get_height(paddle))):
            ball_bounce_off(ball)



        paddle_update_position(paddle)
        ball_update_position(ball)

    # Update the position of the paddle based on the mouse
    # TODO 
        
    # Check for collisions using ball_did_collide_with(ball, obj, width, height) 
    # TODO 

    # If ball hits the bottom wall, we lose.
    # TODO 

    # If bricks are over, you won! 
    # TODO 
  
    # Else, loop through the entire bricks array to see if the ball collided with any brick 
    # TODO 

    # Redraw everything at the end of the while loop
    clock.tick(50)
    draw_objects()

pygame.display.update()


