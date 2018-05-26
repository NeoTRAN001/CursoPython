# -*- coding: utf-8 -*-

def main():
	counter = 0
	c = 0
	with open('celos.txt') as f:
		#print(f.readlines()) View File
		for line in f:
			counter += line.count('viejo')
			c += line.count('también')


	print ('El viejo se encuenta {} en el texto y la palabra también se encuentra {} veces'.format(counter, c))


if __name__ == '__main__':
	main()