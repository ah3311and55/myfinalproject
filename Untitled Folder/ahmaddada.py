def exercise_1():
	numbers=[5,10,15,20,25]
	x=numbers[0]
	n=numbers[-1]
	new=[x,n]
	print new
exercise_1()
def exercise_2():
	a=[1,2,3,4,5,7,13,21,34,55,88]
	b=[]
	length=len (a)
	i=0
	for x in range (length):
		if a[i]<5:
			b.append(a[i])
		i=i+1
	print b
exercise_2()
def exercise_3():
	a=[1,2,3,5,8,13,21,34,55,89]
	b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
	answers=[]
	i=[0]
	for i in a:
		if i in b:
			answers.append(i)
	print answers
exercise_3()
def exercise_4(x):
	if x%2==0:
		print True
	else:
		print False
exercise_4(3)












