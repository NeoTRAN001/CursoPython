#Dictionary

def main():

	resul = 0
	
	calificaciones = {}
	calificaciones ['algoritmos'] = 9
	calificaciones ['matematicas'] = 10
	calificaciones ['web'] = 8
	calificaciones ['Bases_de_datos'] = 10

	#for key in calificaciones:
		#print (key)

	#for value in calificaciones.values():
		#print (value)

	for key, value in calificaciones.iteritems():
		print ('llave: {}, valor: {}'.format(key, value))
		resul += value

	print ('Promedio: {}'.format(resul / 4))

if __name__ == '__main__':
	main()