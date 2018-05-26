#Encrypted Vigenere

# -*- coding: utf-8 -*-

abc = ' abcdefghijklmnopqrstuvwxyz,.?!'

def encrypted(chain, key):
	text = ''
	j = 0

	for i in chain:
		sum1 = abc.find(i) + abc.find(key[j % len(key)])
		mod = int(sum1) % len(abc)
		text += str(abc[mod])
		j += 1

	return text

def show_message(chain, key):
	text = ''
	j = 0

	for i in chain:
		sum1 = abc.find(i) - abc.find(key[j % len(key)])
		mod = int(sum1) % len(abc)
		text += str(abc[mod])
		j += 1

	return text

def main():
	a = True

	while a:
		option = int(raw_input('Show Message = 0\nEncrypt message = 1\nExit = 2\n :'))

		if option == 0:
			chain_m = str(raw_input('Write a text: ')).lower()
			key_m = str(raw_input('Write a key: ')).lower()

			print ('\n\n\nMessage: {}\n\n\n'.format(show_message(chain_m, key_m)))

		elif option == 1:
			chain = str(raw_input('Write a text: ')).lower()
			key = str(raw_input('Write a key: ')).lower()

			print ('\n\n\nMessage: {}\n\n\n'.format(encrypted(chain, key)))

		else:
			a = False

if __name__ == '__main__':
	main()