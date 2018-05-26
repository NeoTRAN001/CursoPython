# -*- coding: utf-8 -*-

import random

IMAGES = ['''

	+---+
	|   |
	    |
	    |
	    |
	    |
	    ==========''', '''

	+---+
	|   |
	O   |
	    |
	    |
	    |
	    ==========''', '''

	+---+
	|   |
	O   |
	|   |
	    |
	    |
	    ==========''', '''

	 +---+
	 |   |
	 O   |
	/|   |
   	     |
   	     |
   	     ==========''', '''

   	 +---+
   	 |   |
   	 O   |
	/|\  |
   	     |
   	     |
   	     ==========''', '''

   	 +---+
   	 |   |
   	 O   |
	/|\  |
	/    |
   	     |
   	     ==========''', '''

   	 +---+
   	 |   |
   	 O   |
	/|\  |
	/ \  |
   	     |
   	     =========='''
]

WORDS = [
	'lavadora', 'secadora', 'sofa', 'gobierno', 'diputado', 'democracia', 'computadora', 'teclado', 'usb', 'laboratorio'
]

def random_word():
	idx = random.randint(0, len(WORDS) - 1)
	return WORDS[idx]

def display_board(hidden_word, tries):
	print (IMAGES[tries])
	print ('')
	print (hidden_word)
	print ('---- * ---- * ---- * ---- * ---- * ---- * ---- * ')

def main():
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_word, tries)
		current_letter = str(raw_input('Escoge una letra: '))

		letter_indexes = []

		for i in range(len(word)):
			if word[i] == current_letter:
				letter_indexes.append(i)

		if len(letter_indexes) == 0:
			tries += 1

			if tries == 7:
				
				print ('\n\n\n\n\n\n\n')
				print ('.............Game over............\n\n\n\n\n\n\n')
				break	
		else:
			for i in letter_indexes:
				hidden_word[i] = current_letter

			letter_indexes = []

			try:
				hidden_word.index('-')
			except ValueError:
				print ('\n\n\n\n\n\n\n\n')
				print('................You win !................\n\n\n\n\n\n\n\n\n')
				break

if __name__ == '__main__':
	print ('W E L C O M E   T O   H A N G E D')
	main()