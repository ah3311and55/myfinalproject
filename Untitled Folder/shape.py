import turtle
from turtle import Turtle


class shape(Turtle):
	def __init__(self,size,color,shape):
		Turtle.__init__(self)
		self.color(color)
		self.shapesize(size)
		self.shape(shape)
class circle(shape):
	def xy(self,x,y):
		self.up()
		self.goto(x,y)
class shape2(shape):
	def xy(self,x,y):
		self.up()
		self.goto(x,y)
		self.down()



circle1 = circle(10,"Red","circle")
circle1.xy(0,200)
turtle1= shape2(10,"red","turtle")
turtle1.xy(10,10)




turtle.exitonclick()