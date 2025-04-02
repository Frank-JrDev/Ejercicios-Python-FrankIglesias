class Empleado:
    # Contador de empleados, es un atributo de clase
    contador_empleados = 0

    def __init__(self, nombre, salario):
        # Atributos de instancia
        self.nombre = nombre
        self.salario = salario

        # Incrementar el contador de empleados al crear un nuevo objeto Empleado
        Empleado.contador_empleados += 1

    @classmethod
    def cantidad_empleados(cls):
        # Método de clase que devuelve el número total de empleados
        return cls.contador_empleados

# Crear empleados
empleado1 = Empleado("Carlos", 50000)
empleado2 = Empleado("Ana", 45000)
empleado3 = Empleado("Luis", 55000)

# Consultar el número total de empleados
print(f"Número total de empleados: {Empleado.cantidad_empleados()}")