class Animal(object):
	def __init__ (self,sound,name,age,favorite_color):
			self.sound =  sound
			self.name = name
			self.age = age
			self.favorite_color = favorite_color
	def eat(self,food):
			print("Yummy!!" +self.name+ " is eating " + food)
	def make_sound(self,x):
			for i in range(x):
				print (self.sound)

	def description(self):
			print(self.name + "is" + self.age + "years old and loves the color" + self.favorite_color)
# d= Animal("bark"," dog "," 2 "," red ")
# d.eat("food")
# d.description()
# d.make_sound(3)
class person(object):
	def __init__ (self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat(self,breakfast):
			print(self.name+ " is eating " + breakfast)
	def play(self,favorite_sport):
			print(self.name+ " is playing "+favorite_sport)
d= person(" ahmad ", " 15 " ," nablus ", " male ")
d.eat("mac")
d.play("football")




