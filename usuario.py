import os
import time

# Muestra la hora actual del sistema
def mostrar_hora():
    print("🕒 Hora actual:", time.ctime(time.time()))

# Limpia la consola según nosotrs querramos
def limpiar_pantalla():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

# Muestra el menú inicial al principio
def mostrar_menu():
    print("══════════════════════════════════════════")
    print("            🎮 JUEGO PREGUNTADOS 🎮")
    print("══════════════════════════════════════════")
    mostrar_hora()
    print("Se te asignará una categoría y dificultad al azar.")
    print("Además, podrás jugar un minijuego de Buscaminas.")
    print("══════════════════════════════════════════\n")

# Pide el nombre del jugador
def pedir_nombre():
    nombre = input("🎮 Ingresá tu nombre: ")
    return nombre

# Pregunta si quiere seguir jugando después de una ronda
def preguntar_si_sigue():
    respuesta = input("¿Querés jugar una nueva ronda? (si/no): ")
    return respuesta
