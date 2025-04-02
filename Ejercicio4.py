class Libro:
    def __init__(self, titulo, autor, num_paginas):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__num_paginas = num_paginas
        self.__pagina_actual = 1  # Empezamos desde la página 1

    def avanzar_paginas(self, num_paginas):
        # Avanza un número de páginas sin superar el total de páginas
        if self.__pagina_actual + num_paginas <= self.__num_paginas:
            self.__pagina_actual += num_paginas
            print(f"Avanzaste {num_paginas} páginas. Estás en la página {self.__pagina_actual}.")
        else:
            raise ValueError("No se puede avanzar más allá del número total de páginas.")

    def retroceder_paginas(self, num_paginas):
        # Retrocede un número de páginas sin ir más allá de la página 1
        if self.__pagina_actual - num_paginas >= 1:
            self.__pagina_actual -= num_paginas
            print(f"Retrocediste {num_paginas} páginas. Estás en la página {self.__pagina_actual}.")
        else:
            raise ValueError("No se puede retroceder más allá de la página 1.")

    def consultar_pagina_actual(self):
        # Devuelve la página actual en la que se encuentra el lector
        return self.__pagina_actual

    def obtener_info_libro(self):
        # Devuelve la información completa del libro
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nNúmero de Páginas: {self.__num_paginas}\nPágina Actual: {self.__pagina_actual}"

# Ejemplo de uso de la clase Libro:
libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 400)

# Consultar información del libro
print(libro.obtener_info_libro())

# Avanzar y retroceder páginas
libro.avanzar_paginas(50)
libro.retroceder_paginas(20)

# Intentar avanzar más allá de la última página
try:
    libro.avanzar_paginas(400)
except ValueError as e:
    print("Error:", e)

# Intentar retroceder más allá de la página 1
try:
    libro.retroceder_paginas(100)
except ValueError as e:
    print("Error:", e)