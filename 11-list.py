# List

# -*- coding: utf-8 -*-

def list_1():
	friends = list()
	friends.append('Pedro') # .append = Add element
	friends.append('Enrique')
	friends.append('Alberto')

	print (friends)

def average_temps(temps):
	sum_out_temps = 0

	for temp in temps:
		sum_out_temps += float(temp)

	return sum_out_temps / len(temps)

def main():
	#list_1()
	temps = [21, 24, 24, 22, 20, 23, 24]

	average = average_temps(temps)

	print ('The average temperature is: {}'.format(average))

if __name__ == '__main__':
	main()