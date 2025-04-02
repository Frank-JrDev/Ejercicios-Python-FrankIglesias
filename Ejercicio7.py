class TarjetaCredito:
    def __init__(self, numero):
        self.numero = numero

    @staticmethod
    def validar_tarjeta(numero):
        # Convertimos el número de la tarjeta a una lista de enteros
        numero = [int(digit) for digit in str(numero)]
        
        # Algoritmo de Luhn (comprobación del número de tarjeta)
        # Invertimos la lista para empezar desde el final
        numero.reverse()

        # Doblamos el valor de cada segundo dígito comenzando desde el segundo dígito
        for i in range(1, len(numero), 2):
            numero[i] = numero[i] * 2
            if numero[i] > 9:  # Si el número es mayor a 9, restamos 9
                numero[i] -= 9
        
        # Sumamos todos los dígitos
        suma_total = sum(numero)

        # Si la suma total es un múltiplo de 10, la tarjeta es válida
        return suma_total % 10 == 0


# Ejemplo de uso de la clase TarjetaCredito:
numero_tarjeta = "4532015112830366"

# Validar la tarjeta utilizando el método estático
if TarjetaCredito.validar_tarjeta(numero_tarjeta):
    print("El número de tarjeta es válido.")
else:
    print("El número de tarjeta no es válido.")
    