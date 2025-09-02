#main es el archivo principal que maneja el menú y la interacción con el usuario
#primero importamos las clases y funciones necesarias
from viaje import Viaje
from registro import RegistroViajes
from user_input import pedir_fecha, pedir_int, pedir_float
#luego definimos el menú principal
def menu():
    reg = RegistroViajes()
    #bucle principal del menú
    while True:
        print("\n=== MENU ===")
        print("1) Agregar viaje")
        print("2) Listar viajes")
        print("3) Resumen general")
        print("4) Resumen por semana")
        print("0) Salir")
        op = input("> ").strip()
        #procesamos la opción seleccionada, cada opción llama a una función o método correspondiente
        #agregar viaje, listar viajes, mostrar resumen general o por semana
        if op == "1":
            fecha = pedir_fecha("Fecha (YYYY-MM-DD): ")
            km = pedir_float("Kilómetros recorridos: ")
            litros = pedir_float("Litros consumidos: ")
            precio = pedir_float("Precio por litro: ")
            viaje = Viaje(fecha, km, litros, precio)
            reg.agregar_viaje(viaje)
            print("Viaje agregado.")
            #mostrar detalles del viaje agregado
            print(viaje)
            #listar todos los viajes
        elif op == "2":
            print("\n--- Lista de Viajes ---")
            for v in reg.viajes:
                print(v)
                #mostrar resumen general
        elif op == "3":
            print("\n--- Resumen General ---")
            print(reg.resumen_general())
            #mostrar resumen por semana
        elif op == "4":
            semana = pedir_int("Número de semana (1-52): ")
            print(f"\n--- Resumen Semana {semana} ---")
            print(reg.resumen_por_semana(semana))
            #salir del programa
        elif op == "0":
            print("Saliendo... Hasta Luego")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#iniciamos el programa llamando al menú principal
if __name__ == "__main__":
    menu()
            