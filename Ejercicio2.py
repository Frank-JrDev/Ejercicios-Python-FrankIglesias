class Rectangulo:
    def __init__(self, largo, ancho):
        # Atributos privados
        if largo > 0 and ancho > 0:
            self.__largo = largo
            self.__ancho = ancho
        else:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
    
    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        # Cambiar las dimensiones del rectángulo
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")

    def calcular_area(self):
        # Calcular el área del rectángulo
        return self.__largo * self.__ancho

    def calcular_perimetro(self):
        # Calcular el perímetro del rectángulo
        return 2 * (self.__largo + self.__ancho)

    def consultar_dimensiones(self):
        # Consultar las dimensiones actuales del rectángulo
        return f"Largo: {self.__largo}, Ancho: {self.__ancho}"

# Ejemplo de uso de la clase Rectangulo:
rectangulo = Rectangulo(5, 3)

# Consultar las dimensiones actuales
print("Dimensiones actuales del rectángulo:", rectangulo.consultar_dimensiones())

# Calcular el área y el perímetro
print("Área del rectángulo:", rectangulo.calcular_area())
print("Perímetro del rectángulo:", rectangulo.calcular_perimetro())

# Cambiar las dimensiones
rectangulo.cambiar_dimensiones(8, 4)
print("\nNuevas dimensiones del rectángulo:", rectangulo.consultar_dimensiones())

# Volver a calcular el área y el perímetro con las nuevas dimensiones
print("Nuevo área del rectángulo:", rectangulo.calcular_area())
print("Nuevo perímetro del rectángulo:", rectangulo.calcular_perimetro())

# Intentar cambiar las dimensiones a valores no válidos
try:
    rectangulo.cambiar_dimensiones(-2, 5)
except ValueError as e:
    print("\nError:", e)

try:
    rectangulo.cambiar_dimensiones(4, -3)
except ValueError as e:
    print("Error:", e)