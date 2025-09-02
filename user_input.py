
from datetime import datetime, date

def pedir_fecha(msg: str = "Fecha (YYYY-MM-DD): ") -> date:
    """Pedir una fecha en formato YYYY-MM-DD y devolver date."""
    while True:
        s = input(msg).strip()
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("Formato inválido.Necesitas poner año, mes, dia ejemplo: 2025-09-01")

def pedir_int(msg: str) -> int:
    """Pedir un entero y reintentar si no es válido."""
    while True:
        s = input(msg).strip()
        try:
            return int(s)
        except ValueError:
            print("Debe ser un número entero.")

def pedir_float(msg: str) -> float:
    """Pedir un número decimal. Aceptar coma o punto."""
    while True:
        s = input(msg).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Debe ser un número (usa punto o coma para decimales).")
