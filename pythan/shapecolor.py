import turtle
turtle.shape("turtle")
radius=70
def draw_circle(color,radius):
	turtle.fillcolor(color)
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()
	turtle.left(80)
draw_circle("pink",radius)
draw_circle("green",radius)
draw_circle("black",radius)
draw_circle("blue",radius)
draw_circle("orange",radius)
draw_circle("red",radius)
turtle.exitonclick()