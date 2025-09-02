# Módulo para pedir entradas de usuario con validación.

#importamos date y time para manejar fechas
from datetime import datetime, date
#solicitamos una fecha en formato YYYY-MM-DD y devolver date
def pedir_fecha(msg: str = "Fecha (YYYY-MM-DD): ") -> date:
    """Pedir una fecha en formato YYYY-MM-DD y devolver date."""
    while True:
        s = input(msg).strip()
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("Formato inválido.Necesitas poner año, mes, dia ejemplo: 2025-09-01")
#creamos la funcion pedir_int
def pedir_int(msg: str) -> int:
    """Pedir un entero y reintentar si no es válido."""
    while True:
        s = input(msg).strip()
        try:
            return int(s)
        except ValueError:
            print("Debe ser un número entero.")
#creamos la funcion pedir_float
def pedir_float(msg: str) -> float:
    """Pedir un número decimal. Aceptar coma o punto."""
    while True:
        s = input(msg).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Debe ser un número (usa punto o coma para decimales).")
