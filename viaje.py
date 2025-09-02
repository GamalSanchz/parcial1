# viaje.py
# Un viaje: fecha (texto), usuario (objeto), ruta (objeto), notas.

class Viaje:
    def __init__(self, fecha_texto, usuario, ruta, notas=""):
        self.fecha = fecha_texto.strip()   # "YYYY-MM-DD" como texto
        self.usuario = usuario             # objeto Usuario
        self.ruta = ruta                   # objeto Ruta
        self.costo = float(ruta.tarifa)    # costo sale de la ruta
        self.notas = notas.strip()

    def __str__(self):
        return (f"{self.fecha} | {self.usuario.nombre} | "
                f"{self.ruta.origen} → {self.ruta.destino} ({self.ruta.codigo}) | "
                f"${self.costo:.2f} | {self.notas}")
