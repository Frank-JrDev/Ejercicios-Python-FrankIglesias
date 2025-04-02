class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # Atributos privados
        self.__titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        # Método para depositar dinero
        if monto > 0:
            self.__saldo += monto
            print(f"Se ha depositado {monto}. Nuevo saldo: {self.__saldo}.")
        else:
            raise ValueError("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        # Método para retirar dinero
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Se ha retirado {monto}. Nuevo saldo: {self.__saldo}.")
        elif monto > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        else:
            raise ValueError("El monto a retirar debe ser mayor que cero.")

    def consultar_saldo(self):
        # Consultar el saldo actual
        return self.__saldo

    def obtener_titular(self):
        # Consultar el titular de la cuenta
        return self.__titular


class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, interes_anual):
        # Inicializar la clase base (CuentaBancaria) con los atributos
        super().__init__(titular, saldo_inicial)
        
        # Atributo privado para el porcentaje de interés anual
        if 0 <= interes_anual <= 100:
            self.__interes_anual = interes_anual
        else:
            raise ValueError("El porcentaje de interés debe estar entre 0 y 100.")

    def aplicar_interes(self):
        # Aplica el interés anual al saldo actual
        interes = self.consultar_saldo() * (self.__interes_anual / 100)
        nuevo_saldo = self.consultar_saldo() + interes
        print(f"Interés anual aplicado: {interes}. Nuevo saldo: {nuevo_saldo}.")
        return nuevo_saldo

    def consultar_interes(self):
        # Consultar el porcentaje de interés actual
        return self.__interes_anual


# Ejemplo de uso de la clase CuentaAhorro:

# Crear una cuenta de ahorro con un interés anual del 5%
cuenta_ahorro = CuentaAhorro("Carlos", 1000, 5)

# Consultar información de la cuenta
print(f"Titular de la cuenta: {cuenta_ahorro.obtener_titular()}")
print(f"Saldo actual: {cuenta_ahorro.consultar_saldo()}")
print(f"Interés anual: {cuenta_ahorro.consultar_interes()}%")

# Realizar un depósito
cuenta_ahorro.depositar(500)

# Aplicar el interés anual
cuenta_ahorro.aplicar_interes()

# Intentar retirar dinero
cuenta_ahorro.retirar(200)

# Consultar el saldo final
print(f"Saldo final: {cuenta_ahorro.consultar_saldo()}")