# Agregar artículos
# Remover artículos
# Ver artículos

lista_articulos = list() #Creamos nuestra lista vacía (variable global)

def agregar_articulo():
    print ('\n----------------------------------------------\n')
    articulo = input ('\nNombre del artículo a agregar: ') # Recibir el artículo
    lista_articulos.append(articulo.capitalize()) # .append sirve para agregar un valor a la lista
    # .capitalize sirve para volver la primera letra de un str en mayúscula
    print ('\n----------------------------------------------\n')

def remover_articulo():
    print ('\n----------------------------------------------\n')
    articulo  = input ('\nNombre del artículo a remover: ') # Recibir el nombre del artículo
    lista_articulos.remove(articulo.capitalize()) # .remove sirve la eliminar un valor de la lista
    # .capitalize sirve para volver la primera letra de un str en mayúscula
    print ('\n----------------------------------------------\n')

def ver_articulo():
    x = 0 # Variable que hará que en nuestro listado, haya un número por cada valor de la lista

    print ('\n-------------- Lista de compras --------------\n')
    for i in lista_articulos: # El ciclo for, recorrerá cada elemento de la lista_articulos
        x = x + 1 # Incrementa por cada iteración que hace el ciclo for
        print ('    {}- {}'.format(x,i)) # e imprimirá cada uno de los valores
    print ('\n----------------------------------------------\n')

def main():

    print ('\n    L I S T A   D E     C O M P R A S\n') # Mensaje de Bienvenida

    while True:
        print ('Operaciones disponibles: \n')
        print ('    1- Agregar artículo') # Crear un menu que se repetirá hasta que
        print ('    2- Remover artículo') # el ciclo while sea False
        print ('    3- Ver artículo')
        print ('    4- Salir')

        operacion = int(input('       : ')) #Recibir valor del usuario

        if operacion == 1:
            agregar_articulo() # La condición evaluará valor que tiene la
        elif operacion == 2: # variable - operacion -, y con eso, llamar a la función correspondiente
            try: # Ejecutar la instrcción qué está dentro del try
                remover_articulo()
            except Exception as e: # Sí, ocurre un error enviar un mensaje en lugar de detener el programa
                print ('\n ______ Artículo no disponible ______\n')
        elif operacion == 3:
            ver_articulo()
        else: break # Romper el ciclo

    print ('\n ¡Adiós!')

if __name__ == '__main__': # Inicio
    main() # Llamar a la función main
