# creamos funciones para manejar la entrada del usuario
def pedir_entero_en_rango(msg, minimo, maximo):
    while True:
        s = input(msg).strip()
        if s.isdigit():
            n = int(s)
            if minimo <= n <= maximo:
                return n
        print("Opción inválida.")
#funcion para elegir un usuario
def elegir_usuario(reg):
    usuarios = reg.listar_usuarios()
    if not usuarios:
        print("No hay usuarios. Crea uno nuevo.")
        nombre = input("Nombre del usuario: ").strip()
        return reg.agregar_usuario(nombre)

    print("\nUsuarios:")
    for i, u in enumerate(usuarios, start=1):
        print(f"  {i}) {u.etiqueta()}")
    print(f"  {len(usuarios)+1}) [Nuevo usuario]")
    idx = pedir_entero_en_rango("> Elige: ", 1, len(usuarios)+1)
    if idx == len(usuarios)+1:
        nombre = input("Nombre del nuevo usuario: ").strip()
        return reg.agregar_usuario(nombre)
    return usuarios[idx-1]
#funcion para elegir una ruta
def elegir_ruta(rutas):
    print("\nRutas disponibles:")
    for i, r in enumerate(rutas, start=1):
        print(f"  {i}) {r.etiqueta()}")
    idx = pedir_entero_en_rango(f"> Elige ruta (1..{len(rutas)}): ", 1, len(rutas))
    return rutas[idx-1]
