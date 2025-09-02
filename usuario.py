# Clase simple para representar a una persona que viaja.
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre.strip()
# Etiqueta legible para mostrar en listas.
    def etiqueta(self):
        return self.nombre
