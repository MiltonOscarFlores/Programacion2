"""Se desea crear un programa que simule el funcionamiento basico de un vehiculo.


-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo."""

class Vehiculo:
    def __init__(self, marca, ruedas, color, enMarcha=False):
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.enMarcha = enMarcha
    
    def arrancar(self):
        self.enMarcha = True

    def tipoVehiculo(self):
        if self.ruedas == 4:
            return "Automovil"
        elif self.ruedas == 2:
            return "Motocicleta"
        else:
            return "Desconocido"
        
    def mostrar(self):
        print("Marca:", self.marca)
        print("Ruedas:", self.ruedas)
        print("Color:", self.color)
        print("En marcha:", self.enMarcha)
