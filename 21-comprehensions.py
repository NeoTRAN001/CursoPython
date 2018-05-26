#List comprehensions and Dictionary comprehensions


#List
	#pares = []
	#for num in range(1, 31):
	#	if num % 2 == 0:
	#		pares.append(num)

	#print (pares)

# Dictionary
	#cuadrados = {}

	#for num in range (1, 31):
	#	cuadrados[num] = num**2
	#print (cuadrados)

def list():
	even = [num for num in range(1, 31) if num % 2 == 0]
	print (even)
	print ('\n\n\n')

def dictionary():
	squares = {num: num **2 for num in range(1, 31)}
	print (squares)

def main():
	list()
	dictionary()

if __name__ == '__main__':
	main()