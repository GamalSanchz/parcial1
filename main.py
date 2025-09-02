# Menú básico para: usuarios, registrar viajes, listar y consultar por usuario.

from ruta import Ruta
from viaje import Viaje
from registro import Registro
from user_input import elegir_usuario, elegir_ruta

def obtener_rutas_fijas():
    # Edita o agrega las rutas que quieras (incluye tus ejemplos)
    return [
        Ruta("328",  "Osicala",          "San Miguel",       1.50),
        Ruta("328",  "San Miguel",       "Osicala",          1.50),
        Ruta("333B", "San Buenaventura", "San Miguel",       0.65),
        Ruta("333B", "San Miguel",       "San Buenaventura", 0.65),
    ]
# Mostrar las rutas disponibles
def ver_rutas(rutas):
    print("\nRutas y tarifas:")
    for r in rutas:
        print(" -", r.etiqueta())
# Registrar un viaje nuevo
def registrar_viaje(reg, rutas):
    usuario = elegir_usuario(reg)
    if not usuario:
        print("Nombre vacío; no se creó usuario.")
        return
    fecha = input("Fecha (YYYY-MM-DD): ").strip()   # simple, como texto
    ruta = elegir_ruta(rutas)
    notas = input("Notas (opcional): ").strip()
    v = Viaje(fecha, usuario, ruta, notas)
    reg.agregar_viaje(v)
    print("✓ Viaje registrado:", v)
# Listar todos los viajes
def listar_viajes(reg):
    vs = reg.listar_viajes()
    if not vs:
        print("No hay viajes.")
        return
    print("\nFECHA       | USUARIO           | RUTA (COD)                 | COSTO | NOTAS")
    print("-"*85)
    for v in vs:
        print(v)
# Consultar viajes por usuario
def consultar_por_usuario(reg):
    nombre = input("Nombre del usuario: ").strip()
    vs = reg.viajes_por_usuario(nombre)
    if not vs:
        print("Ese usuario no tiene viajes.")
        return
    print(f"\nViajes de {nombre}:")
    print("FECHA       | ORIGEN → DESTINO (COD) | COSTO | NOTAS")
    print("-"*65)
    for v in sorted(vs, key=lambda x: x.fecha):
        print(f"{v.fecha} | {v.ruta.origen} → {v.ruta.destino} ({v.ruta.codigo}) | ${v.costo:.2f} | {v.notas}")
# Menú principal
def menu():
    reg = Registro()
    rutas = obtener_rutas_fijas()
# Bucle del menú
    while True:
        print("\n=== MENU ===")
        print("1) Agregar usuario")
        print("2) Registrar viaje (usuario + ruta)")
        print("3) Listar todos los viajes")
        print("4) Consultar viajes por usuario")
        print("5) Ver rutas y tarifas")
        print("0) Salir")
        op = input("> ").strip()

        if op == "1":
            nombre = input("Nombre del usuario: ").strip()
            u = reg.agregar_usuario(nombre)
            if u:
                print(f"✓ Usuario: {u.nombre}")
            else:
                print("Nombre vacío; no se creó usuario.")
        elif op == "2":
            registrar_viaje(reg, rutas)
        elif op == "3":
            listar_viajes(reg)
        elif op == "4":
            consultar_por_usuario(reg)
        elif op == "5":
            ver_rutas(rutas)
        elif op == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
