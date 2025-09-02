
# Registro simple de usuarios y viajes.

from usuario import Usuario

class Registro:
    def __init__(self):
        self.usuarios = []   # lista de Usuario
        self.viajes = []     # lista de Viaje

    # ---- Usuarios ----
    def agregar_usuario(self, nombre):
        nombre = nombre.strip()
        if not nombre:
            return None
        for u in self.usuarios:
            if u.nombre.lower() == nombre.lower():
                return u
        nuevo = Usuario(nombre)
        self.usuarios.append(nuevo)
        return nuevo

    def listar_usuarios(self):
        return sorted(self.usuarios, key=lambda u: u.nombre.lower())

    # ---- Viajes ----
    def agregar_viaje(self, viaje):
        self.viajes.append(viaje)

    def listar_viajes(self):
        # Orden por fecha (texto), luego usuario y código de ruta
        return sorted(self.viajes, key=lambda v: (v.fecha, v.usuario.nombre.lower(), v.ruta.codigo))

    def viajes_por_usuario(self, nombre):
        k = nombre.strip().lower()
        return [v for v in self.viajes if v.usuario.nombre.lower() == k]
