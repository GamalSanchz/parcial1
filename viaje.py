# Módulo que define la clase Viaje
from dataclasses import dataclass
from datetime import date
# Conjunto de tipos de viaje válidos
TIPOS_VALIDOS = {"urbana", "rural", "otro"}
# Clase que representa un viaje
@dataclass
class Viaje:
    fecha: date
    ruta: str
    tipo: str          # "urbana" / "rural" / "otro"
    tiempo_min: int    # duración en minutos
    costo: float       # USD
    notas: str = ""

    def __post_init__(self):
        # Normaliza y valida tipo
        self.tipo = self.tipo.strip().lower()
        if self.tipo not in TIPOS_VALIDOS:
            raise ValueError(f"tipo inválido: {self.tipo}. Debe ser uno de {', '.join(TIPOS_VALIDOS)}")
    # Representación legible del viaje
    def __str__(self):
        return (f"Fecha: {self.fecha}, Ruta: {self.ruta}, Tipo: {self.tipo}, "
                f"Tiempo: {self.tiempo_min} min, Costo: ${self.costo:.2f}, Notas: {self.notas}")
