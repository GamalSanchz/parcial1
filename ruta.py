# Ruta de transporte público con tarifa fija.
#definimos la clase ruta
class Ruta:
    def __init__(self, codigo, origen, destino, tarifa):
        self.codigo = str(codigo).strip()
        self.origen = origen.strip()
        self.destino = destino.strip()
        self.tarifa = float(tarifa)
    
    # Etiqueta legible para mostrar en listas.
    def etiqueta(self):
        # Ej: "328 | Osicala → San Miguel ($1.50)"
        return f"{self.codigo} | {self.origen} → {self.destino} (${self.tarifa:.2f})"
