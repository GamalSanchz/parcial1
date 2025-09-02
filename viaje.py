# viaje.py
# Un viaje realizado por un usuario en una ruta, en una fecha (como texto simple).
#creamos la clase viaje
class Viaje:
    def __init__(self, fecha_texto, usuario, ruta, notas=""):
        self.fecha = fecha_texto.strip()# "YYYY-MM-DD" (texto, para mantenerlo básico)
        self.usuario = usuario# objeto Usuario
        self.ruta = ruta # objeto Ruta
        self.costo = ruta.tarifa # costo = tarifa de la ruta
        self.notas = notas.strip()
    

    def __str__(self):
        return (f"{self.fecha} | {self.usuario.nombre} | "
                f"{self.ruta.origen} → {self.ruta.destino} ({self.ruta.codigo}) | "
                f"${self.costo:.2f} | {self.notas}")
