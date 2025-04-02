class Producto:
    def __init__(self, nombre, precio):
        # Atributos privados
        self.__nombre = nombre
        self.__precio = precio

    def cambiar_precio(self, nuevo_precio):
        # Cambiar el precio solo si el nuevo precio es mayor que cero
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print(f"El precio de {self.__nombre} ha sido actualizado a {self.__precio}.")
        else:
            raise ValueError("El precio debe ser mayor que cero.")

    def consultar_precio(self):
        # Consultar el precio actual
        return self.__precio

    def obtener_nombre(self):
        # Obtener el nombre del producto
        return self.__nombre

    def aplicar_descuento(self, porcentaje_descuento):
        # Aplicar descuento si el porcentaje es válido (entre 0 y 100)
        if 0 <= porcentaje_descuento <= 100:
            descuento = self.__precio * (porcentaje_descuento / 100)
            nuevo_precio = self.__precio - descuento
            self.__precio = nuevo_precio
            print(f"Descuento aplicado: {porcentaje_descuento}%. El nuevo precio de {self.__nombre} es {self.__precio}.")
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

# Ejemplo de uso de la clase Producto:
producto = Producto("Laptop", 1500)

# Consultar el nombre y el precio del producto
print(f"Nombre del producto: {producto.obtener_nombre()}")
print(f"Precio actual: {producto.consultar_precio()}")

# Cambiar el precio del producto
producto.cambiar_precio(1200)

# Aplicar un descuento al producto
producto.aplicar_descuento(10)

# Intentar cambiar el precio a un valor no válido
try:
    producto.cambiar_precio(-100)
except ValueError as e:
    print(e)

# Intentar aplicar un descuento fuera del rango
try:
    producto.aplicar_descuento(150)
except ValueError as e:
    print(e)