class Estudiante:
    def __init__(self, nombre, edad):
        # Atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def agregar_nota(self, nota):
        # Asegura que la nota esté en el rango de 0 a 100
        if 0 <= nota <= 100:
            self.__notas.append(nota)
            print(f"Nota {nota} agregada correctamente.")
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")

    def calcular_promedio(self):
        # Calcula el promedio de las notas
        if self.__notas:
            return sum(self.__notas) / len(self.__notas)
        else:
            return 0  # Si no hay notas, el promedio es 0

    def consultar_nombre(self):
        # Consulta el nombre del estudiante
        return self.__nombre

    def consultar_edad(self):
        # Consulta la edad del estudiante
        return self.__edad

# Ejemplo de uso de la clase Estudiante:
estudiante = Estudiante("Juan Pérez", 20)

# Consultar nombre y edad
print(f"Nombre del estudiante: {estudiante.consultar_nombre()}")
print(f"Edad del estudiante: {estudiante.consultar_edad()}")

# Agregar notas al estudiante
estudiante.agregar_nota(85)
estudiante.agregar_nota(90)
estudiante.agregar_nota(78)

# Calcular y mostrar el promedio de las notas
promedio = estudiante.calcular_promedio()
print(f"Promedio de las notas: {promedio}")

# Intentar agregar una nota fuera de rango
try:
    estudiante.agregar_nota(110)
except ValueError as e:
    print("Error:", e)

# Intentar agregar una nota negativa
try:
    estudiante.agregar_nota(-5)
except ValueError as e:
    print("Error:", e)