#Clase Player
class Player:
    # __init__ es el primer método que se ejecuta cuando se crea un objeto
    def __init__(self, **kwargs): #Desempaquetamiento de Diccionario
        self.hit_point = kwargs.get("hit_point", 50) # Agregar el nombre de la llave y su valor por defecto
        self.mana = kwargs.get("mana", 50) # self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método
        self.vocation = kwargs.get("vocation", "No vocation")
        self.hechizo = kwargs.get("hechizo", "Puff")
    # Todo método en python recibe un valor por defecto (self)
    def lanzar_hechizo(self): # Método que indicará la acción del hechizo
        return self.hechizo # self será el objeto que llamará a está función
