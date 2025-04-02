class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializamos los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        # Verifica si hay suficiente stock para la cantidad solicitada
        if self.stock >= cantidad:
            print(f"Hay {self.stock} unidades disponibles de {self.nombre}.")
            return True
        else:
            print(f"No hay suficiente stock para {cantidad} unidades de {self.nombre}. Solo hay {self.stock}.")
            return False

    def vender(self, cantidad):
        # Intenta vender la cantidad solicitada, si hay stock suficiente
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Quedan {self.stock} unidades en stock.")
        else:
            print("Venta no realizada debido a falta de stock.")

    def reabastecer(self, cantidad):
        # Aumenta el stock del producto
        self.stock += cantidad
        print(f"Se han reabastecido {cantidad} unidades de {self.nombre}. Ahora hay {self.stock} unidades.")

# Crear un objeto de la clase Producto
producto = Producto("Laptop", 1200, 10)

# Operaciones solicitadas
producto.verificar_disponibilidad(5)  # metodo para verificar si hay 5 unidades disponibles
producto.vender(3)  # Vender 3 unidades
producto.verificar_disponibilidad(8)  # metodo para ve|rificar si hay 8 unidades disponibles
producto.vender(8)  # Intentar vender 8 unidades (no debería ser posible)
producto.reabastecer(10)  # Reabastecer con 10 unidades adicionales
producto.verificar_disponibilidad(8)  # Verificar nuevamente si hay 8 unidades disponibles
producto.vender(8)  # Vender 8 unidades después del reabastecimiento