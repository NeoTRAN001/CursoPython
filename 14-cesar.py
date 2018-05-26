#Encrypted Caesar

# -*- coding: utf-8 -*-

abc = ' abcdefghijklmnopqrstuvwxyz,.?'

def encrypted(value, number):
	
	text = ''

	for i in value:
		sum_i = abc.find(i) + number
		print(sum_i)
		mod = int(sum_i) % len(abc)
		print(mod)
		text += str(abc[mod])
		print (text)

	return text

def show_message(value, number):

	text = ''

	for i in value:
		sum_i = abc.find(i) - number
		mod = int(sum_i) % len(abc)
		text += str(abc[mod])

	return text

def main():
	a = True

	while a:
		option = int(raw_input('Show Message = 0\nEncrypt message = 1\nExit = 2\n :'))

		if option == 1:
		
			value_1 = str(raw_input('Encrypt message: ')).lower()
			number = int(raw_input('Key: '))

			print ('\n\n\nMessage encrypted: {}\n\n'.format(encrypted(value_1, number)))

		elif option == 0:

			value_2 = str(raw_input('Message encrypted: ')).lower()
			number_2 = int(raw_input('key: '))

			print ('\n\n\nMessage: {}\n\n'.format(show_message(value_2, number_2)))

		else:
			a = False

if __name__ == '__main__':
	main()