# ************************* Media o Promedio *************************
# Datos = 1 ,8, 7, 9, 5
# n = 5
# Sumatoria = 30
# Resultado = 30 / 5 = 6

# -*- coding: utf-8 -*-

def imprimir(texto, valor):
    print('{} {}\n'.format(texto, valor))

def promedio(datos):
    sumatoria = sum(datos)
    imprimir('La sumatoria es: ', sumatoria)

    longitud = float(len(datos))
    imprimir('La longitud es: ', longitud)

    resultado = sumatoria / longitud
    imprimir('El resultado es: ', resultado)

def moda(datos):
    repeticiones = 0
    
    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n

    moda = []
    for i in datos:
        n = datos.count(i)
        if n == repeticiones and i not in moda:
            moda.append(i)

    if len(moda) != len(datos):
        imprimir ('Moda: ', moda)
    else:
        print ('No hay moda')

def media(datos):
    datos.sort()

    if len(datos) % 2 == 0:
        n = len(datos)
        mediana = (datos[n / 2 - 1] + datos[n / 2]) / 2
    else:
        mediana = datos[len(datos) / 2]

    imprimir ('Media: ', mediana)


def main():
    datos = list()

    salir = int(raw_input('Cuantos valores quieres ingresar? : '))

    for i in range(salir):
            number = int(raw_input('Escribe el dato: '))
            datos.append(number)

    promedio(datos)
    moda(datos)
    media(datos)



if __name__ == '__main__':
    main()
