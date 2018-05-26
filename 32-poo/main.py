# Un objeto puede entenderse como una copia de nuestra clase
from player import Player # Para el archivo player, importar la clase Player

def imprimir_mensaje(objeto, mensaje, a = True): # Está función imprimirá los valores de un objeto
    print('------------------------------------------')
    print('\n{}\n\nHit point: {} || Mana: {} || Vocation: {} || Hechizo: {} \n'
    .format(mensaje, objeto.hit_point, objeto.mana, objeto.vocation, objeto.hechizo))
    print('Lanzar hechizo: {}\n'.format(objeto.lanzar_hechizo()))
    print('------------------------------------------')

valor_por_defecto = Player() # Creamos un nuevo objeto de la clase Player, sin mandar parámetros
imprimir_mensaje(valor_por_defecto, 'Valores por defecto de la clase Player')

sorcerer = Player(hit_point = 40, mana = 80, vocation = 'Sorcerer', hechizo = 'Utevo lux',) # Creamos un nuevo objeto de la clase player
imprimir_mensaje(sorcerer, 'Valores de la clase al crear el objeto sorcerer')

knight = Player(hit_point = 80, mana = 20, vocation = 'Knight', hechizo = 'Exori') # Creamos un nuevo objeto de la clase player
imprimir_mensaje(knight, 'Valores de la clase al crear el objeto knight')

paladin = Player(hit_point = 60, mana = 40, vocation = 'Paladin', hechizo = 'Vairon') # Creamos un nuevo objeto de la clase player
imprimir_mensaje(paladin, 'Valores de la clase al crear el objeto Paladin')

druid = Player (hit_point = 90, mana = 30, vocation ='Druid', hechizo = 'Xmachine') # Creamos un nuevo objeto de la clase player
imprimir_mensaje(druid, 'Valores de la clase al crear el objeto Druid')
