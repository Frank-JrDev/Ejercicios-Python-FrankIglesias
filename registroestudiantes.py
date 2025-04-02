class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        # atributos del estudiante
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def verificar_aprobacion(self):
        # usamos este método para verificar si el estudiante aprobó o reprobó
        if self.calificacion >= 6:
            return f"{self.nombre} ha aprobado con una calificación de {self.calificacion}."
        else:
            return f"{self.nombre} ha reprobado con una calificación de {self.calificacion}."

# ejemplo de uso:
estudiante1 = Estudiante("Juan Pérez", 20, 7.5)
estudiante2 = Estudiante("Ana Gómez", 22, 4.3)

# verificar si los estudiantes aprobaron o reprobaron
print(estudiante1.verificar_aprobacion())
print(estudiante2.verificar_aprobacion())