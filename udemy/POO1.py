'''
class Persona:  #asi se crea una clase  class y nombre
    
    def __init__(self):  # Inicializador de la clase como el metodo constructor

        #Aqui creamos los atributos ( no se dan valor si no se envian por parametros)
        self.Nombre = "Andres"
        self.Edad = 28

Persona1 = Persona() # se crea variable donde creamos el objecto persona

print(Persona1.Nombre)

'''

#---------------------------------------------------------
# CLASE CON PARAMETROS 

'''
class Persona:  # creamos la clase llamada Persona

    def __init__(self, Nombre, Apellido, Edad): # Metodo constructor con parametros

        # Creamos los atributos asi se usan realmente
        self.Nombre = Nombre  # El Nombre que esta a la izquierda es el atributo 
        self.Apellido = Apellido # el que esta a la derecha es el parametro 
        self.Edad = Edad

Persona1= Persona("Andres", "Vasquez", 28) #Aqui enviamos los parametros al constructor

print(Persona1.Nombre)

'''

#------------------------------------------------------------
# CREANDO MAS DE UN OBJECTO DE LA CLASE PERSONAS

'''
class Persona:

    def __init__(self, Nombre, Apellido, Edad):

        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad

Persona1 = Persona("Andres", "Vasquez", 28)
print(f"El nombre de la persona es {Persona1.Nombre} {Persona1.Apellido} y su edad es {Persona1.Edad}")

Persona2 = Persona("Yeli", "Mier", 21)
print("El nombre de la persona es {} {} y su edad es {}".format(Persona2.Nombre,Persona2.Apellido,Persona2.Edad))

'''

#------------------------------------------------------------
