#Error

countries = {
	'mexico': 122,
	'colombia': 49,
	'argentina': 43,
	'chile': 18,
	'peru': 31
}

def main():
	while True:
		country = str(raw_input('Write a country: ')).lower()

		try:
			print ('The population of {} is {} million'.format(country, countries[country]))
		except KeyError: #error of console
			print("{} isn't here".format(country))

if __name__ == '__main__':
	main()