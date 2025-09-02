# Clase simple para representar a una persona que viaja.
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre.strip()

    def etiqueta(self):
        return self.nombre
