# -*- coding: utf-8 -*-

from poo import Lamp

def main():
	lamp = Lamp(is_turned_on= False)

	while True:
		command = str(raw_input('What are you want to do? \n [o] = on\n [f] = off\n [e] = exit'))

		if command == 'o':
			lamp.turn_on()
		elif command == 'f':
			lamp.turn_off()
		else:
			break

if __name__ == '__main__':
	main()