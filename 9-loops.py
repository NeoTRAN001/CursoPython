#loop (bucles)

# -*- coding: utf-8 -*-

import random

def loop_range():
	print (range(20)) #Print numbers in sequence [for 0 to n-1]
	print (range(1, 40, 5)) #range (start, end, Range of n in n)

def loop_for():

	r = 'abcdefghi'

	for i in range(5):
		print ('Loop for {}'.format(i))

	for i in range(30):
		if i % 3 != 0:
			continue
		else:
			print (i**2)

	for i in range(len(r)):
		print (r[i])

def loop_while():
	number_found = False
	random_number = random.randint (0, 20)
	i = 0

	while i < 10:
		print (i)
		i += 1

	print ('\n\n\n\n R A N D O M   N U M B E R')

	while not number_found:
		number = int(raw_input('Guess the number: '))

		if number == random_number:
			print ('Congratulations !')
			number_found = True
		elif number > random_number:
			print ('Your number is > random Number')
		else:
			print ('Your number is < random Number')

def main():

	option = int (raw_input ('Choose a loop  \n1-range\n2-for\n3-while \n'))

	if option == 1:
		loop_range()

	elif option == 2:
		loop_for()

	elif option == 3:
		loop_while()

if __name__ == '__main__':
	main()