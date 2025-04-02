class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        # Atributos del vehículo
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        # Aumenta la velocidad sin superar el límite máximo
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
            print(f"La velocidad máxima de {self.velocidad_maxima} km/h ha sido alcanzada.")
        else:
            self.velocidad_actual += incremento
            print(f"El vehículo ha acelerado. Velocidad actual: {self.velocidad_actual} km/h.")

    def frenar(self, decremento):
        # Reduce la velocidad sin bajar de 0
        if self.velocidad_actual - decremento < 0:
            self.velocidad_actual = 0
            print("El vehículo se ha detenido.")
        else:
            self.velocidad_actual -= decremento
            print(f"El vehículo ha frenado. Velocidad actual: {self.velocidad_actual} km/h.")

    def verificar_limite(self, velocidad_limite):
        # Verifica si el vehículo supera el límite de velocidad dado
        if self.velocidad_actual > velocidad_limite:
            print(f"El vehículo está excediendo el límite de velocidad de {velocidad_limite} km/h.")
        else:
            print(f"El vehículo está dentro del límite de velocidad de {velocidad_limite} km/h.")

def menu():
    # Menú interactivo para controlar el vehículo
    print("\n=== Menú de opciones ===")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar si excede un límite de velocidad")
    print("4. Salir")

def programa():
    # se crea un objeto Vehiculo
    vehiculo = Vehiculo("Toyota", "Corolla", 180)

    while True:
        menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            incremento = int(input("¿Cuánto desea acelerar (en km/h)? "))
            vehiculo.acelerar(incremento)
        elif opcion == "2":
            decremento = int(input("¿Cuánto desea frenar (en km/h)? "))
            vehiculo.frenar(decremento)
        elif opcion == "3":
            velocidad_limite = int(input("¿Qué límite de velocidad desea verificar (en km/h)? "))
            vehiculo.verificar_limite(velocidad_limite)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")

# aquí ejecutamos el programa
programa()