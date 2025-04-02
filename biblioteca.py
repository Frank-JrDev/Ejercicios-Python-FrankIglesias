class Libro:
    def __init__(self, titulo, autor, num_paginas):
        # Aquí se definen los atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        # Método para mostrar la información del libro
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        # Método para actualizar el número de páginas
        self.num_paginas = nuevas_paginas
        print(f"El número de páginas ha sido actualizado a: {self.num_paginas}")

# Ejemplo de uso:
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)

# Mostrar la información del libro
libro1.mostrar_informacion()

# Actualizar el número de páginas
libro1.actualizar_paginas(450)

# Mostrar la información actualizada del libro
libro1.mostrar_informacion()
