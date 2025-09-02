# ceramos una clase para manejar las rutas
class Ruta:
    def __init__(self, codigo: str, origen: str, destino: str, tarifa: float):
        self.codigo = str(codigo).strip()
        self.origen = origen.strip()
        self.destino = destino.strip()
        self.tarifa = float(tarifa)
# Etiqueta legible para mostrar en listas.
    def etiqueta(self) -> str:
        return f"{self.codigo} | {self.origen} → {self.destino} (${self.tarifa:.2f})"
