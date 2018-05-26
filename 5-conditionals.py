#Conditional in Python

def say_hello(age):

	if age > 18:
		print ('age > 18')
	else:
		print ('age < 18')

if __name__ == '__main__':

	say_hello(20)
	say_hello(15)