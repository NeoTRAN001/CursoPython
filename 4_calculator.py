# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):

	mex_to_col_rate = 145.97

	return mex_to_col_rate * ammount

def run():

	print ('C U R R E N C Y   C A L C U L A T O R')
	print ('Convert Mexican money into Colombian money.')
	print ('')

	ammount = float(raw_input('Enter an amount of money Mexican you want to convert into money Colombian: ')) # Entry of values

	result = foreign_exchange_calculator(ammount) # To call to function foreign_exchange_calculator and match it to the result variable

	print ('${} Mexican coin is ${} Colombian coin'.format(ammount, result)) # new way to concatenate print ('${} blablabla ${}'.format(value1, value2))
	print ('')

if __name__ == '__main__':
	
	run() # To call to function run