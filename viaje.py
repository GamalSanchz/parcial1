
class Viaje:
    def __init__(self, fecha_texto: str, usuario, ruta, notas: str = ""):
        self.fecha = fecha_texto.strip()    # texto "YYYY-MM-DD"
        self.usuario = usuario              # objeto Usuario
        self.ruta = ruta                    # objeto Ruta
        self.costo = float(ruta.tarifa)     # costo sale de la ruta
        self.notas = notas.strip()

    def __str__(self) -> str:
        return (f"{self.fecha} | {self.usuario.nombre} | "
                f"{self.ruta.origen} → {self.ruta.destino} ({self.ruta.codigo}) | "
                f"${self.costo:.2f} | {self.notas}")
