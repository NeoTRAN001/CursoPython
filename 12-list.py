#List

# -*- coding: utf-8 -*-

my_list = [1]
my_list2 = [2, 4, 5]

def sum_list():

	my_list3 =  my_list + my_list2
	print (my_list3)

def mul_list():
	my_list3 = ['a']
	my_list4 = my_list3 * 10
	print (my_list4)

def main():
	
	sum_list()
	mul_list()

if __name__ == '__main__':
	
	main()