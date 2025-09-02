#  este archivo maneja el registro de viajes
#primero llamamos los modulos
from typing import List, Dict, Tuple
from viaje import Viaje
#luego definimos la clase RegistroViajes

class RegistroViajes:
    def __init__(self) -> None:
        self._viajes: List[Viaje] = []
        # lista interna de viajes

    def agregar(self, v: Viaje) -> None:
        """Agregar un viaje al registro."""
        self._viajes.append(v)

    def listar_ordenado(self) -> List[Viaje]:
        """Devolver los viajes ordenados por fecha y luego por ruta."""
        #ordenar por (fecha, ruta.lower()) y devolver la lista ordenada.
        return sorted(self._viajes, key=lambda x: (x.fecha, x.ruta.lower()))

    def resumen_general(self) -> dict:
        """Totales simples: cantidad, minutos y costo."""
        # calcular sumas y redondear costo a 2 decimales.
        total_costo = round(sum(v.costo for v in self._viajes), 2)
        total_tiempo = sum(v.tiempo_min for v in self._viajes)
        return {
            "viajes": len(self._viajes),
            "total_tiempo_min": total_tiempo,
            "total_costo": total_costo,
        }
    
    def resumen_por_semana(self) -> Dict[Tuple[int, int], dict]:
        """Agrupar por semana ISO: clave (año, nro_semana) con totales."""
        # usar v.fecha.isocalendar() → (year, week, weekday).
        res: Dict[Tuple[int, int], dict] = {}
        for v in self._viajes:
            year, week, _ = v.fecha.isocalendar()
            key = (year, week)
            if key not in res:
                res[key] = {"viajes": 0, "total_tiempo_min": 0, "total_costo": 0.0}
            res[key]["viajes"] += 1
            res[key]["total_tiempo_min"] += v.tiempo_min
            res[key]["total_costo"] += v.costo
        for k in res:
            res[k]["total_costo"] = round(res[k]["total_costo"], 2)
        return res