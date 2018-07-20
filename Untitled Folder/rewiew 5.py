class Animal(object):
	def __init__(self,name,species,age,favorite_color):
		self.name=name
		self.species = species
		self.age = age
		self.favorite_color = favorite_color

# class Cat(Animal):
# 	def meow(self, sound):
# 		print(sound+"!"+ " hello, my name is " + self.name)
class bird(Animal):
	def intro(self,kind):
		print("iam a "+ kind)

	# def fly(self,abillity):
	# 	print(abillity+"!"+"i can" + abillity)
b=bird("bob","bird","2","blue")
b.intro("bird")
class dave(bird):
	def sound(self,sound):
		print("sound"+"!"+"my name is "+self.name)


	


# tommy = Cat(name ="tommy",species ="cat",age = "17",favorite_color= "blue")
# tommy.meow("meow")

