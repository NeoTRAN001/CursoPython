# Palindrome

# -*- coding: utf-8 -*-

def palindrome2(word):
	reversed_word = word[::-1]

	if reversed_word == word:
		return True

	return False

def palindrome(word):
	reversed_letters = []

	for letter in word:
		reversed_letters.insert(0, letter)

	reversed_word = ''.join(reversed_letters)

	if reversed_word == word:
		return True

	return False

def main():
	word = str(raw_input('Write a word: '))

	result = palindrome2(word)

	if result == True:
		print ('{} is Palindrome'.format(word))
	else:
		print ("{} isn't Palindrome".format(word))

if __name__ == '__main__':
	main()