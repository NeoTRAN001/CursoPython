#Decoradores

# -*- coding: utf-8 -*-

def protected(func): #function
	
	def wrapper (password):

		if password == 'platzi':
			return func()
		else:
			print("Your password isn't correct")

	return wrapper

@protected
def protected_func():
	print ('Your password is correct')

def main():
	password = str(raw_input('Write your password: '))
	protected_func(password)

if __name__ == '__main__':
	main()