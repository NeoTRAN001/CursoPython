#Strings

def method_upper(value):

	print ('.......................................Method upper')
	print (value.upper())

def method_lower(value):
	print ('.......................................Method lower')
	print (value.lower())

def method_find(value):
	print ('.......................................Method find')
	print (value.find('z')) #Search specific index of one character

def method_split(value):
	print ('.......................................Method split')
	print (value.split())

def method_join(value):
	print ('.......................................Method join')
	print (value.join)

def slices(value):
	print ('.......................................Slices (rebanadas)')
	print ('Cut the first character: {}'.format(value[1:])) #cut a character specific
	print ('Go index one to three: {}'.format(value[1:3]))
	print ('Go index one to six, but skip two by two: {}'.format(value[1:6:2]))
	print ('Starting at the end: {}'.format(value[::-1]))

def main():
	my_string = 'prueba'

	String_length = len(my_string)

	print ('This string have {} characters'.format(String_length))

	for i in range(0, String_length):

		print (my_string[i])

	method_upper(my_string)
	method_lower(my_string)
	method_find(my_string)
	method_split(my_string)
	method_join(my_string)

	slices(my_string)


if __name__ == '__main__':
	main()
