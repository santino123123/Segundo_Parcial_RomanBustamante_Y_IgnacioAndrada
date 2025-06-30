import os 
from preguntas_main import *
import time

def mostrar_hora():
    print(time.ctime(time.time()))


def limpiar_pantalla():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")


def mostrar_menu():
    print("╔══════════════════════════════════════╗")
    print("║            JUEGO PREGUNTADOS         ║")
    print("╠══════════════════════════════════════╣")
    print("║ Elegí una categoría para jugar:      ║")
    print("║                                      ║")
    print("║ 1. Fútbol                            ║")
    print("║ 2. Videojuegos                       ║")
    print("║ 3. Entretenimiento                   ║")
    print("╚══════════════════════════════════════╝")
    print("==========  HORA DE INICIO    ==========")
    mostrar_hora()

def obtener_opciones():
    entrada_opciones = False
    while entrada_opciones == False:
        entrada = input("Selecciona una categoría (1-3): ")
        if entrada == "1":
            return "Fútbol"
        elif entrada == "2":
            return "Videojuegos"
        elif entrada == "3":
            return "Entretenimiento"
        else:
            print("Opción inválida. Intenta nuevamente.")


def seleccionar_dificultad():
    print("\nDIFICULTADES DISPONIBLES:")
    print("1. Fácil")
    print("2. Intermedio")
    print("3. Difícil")
    entrada_valida = False
    while entrada_valida == False:
        dificultad = input("Elegí una dificultad (1-3): ")
        if dificultad == "1":
            return "Facil"
        if dificultad == "2":
            return "Media"
        if dificultad == "3":
            return "Dificil"
        print("Opción inválida. Intentá otra vez.")

def filtrar_preguntas_por_dificultad(lista_preguntas, nivel):
    lista_filtrada = []
    i = 0
    while i < len(lista_preguntas):
        if lista_preguntas[i]["puntos"] == nivel:
            lista_filtrada.append(lista_preguntas[i])
        i = i + 1
    if len(lista_filtrada) == 0:
        print("⚠ No se encontraron preguntas con dificultad:", nivel)
    return lista_filtrada

def hacer_pregunta(pregunta):
    print("")
    print("PREGUNTA:")
    print(pregunta["pregunta"])
    for clave in ["a", "b", "c", "d"]:
        print(clave + ")", pregunta["opciones"][clave])
    print("(⏰Tenés 10 segundos para responder)")
    respuesta = (input("Tu respuesta (a/b/c/d): "))
    if respuesta == pregunta["respuesta"]:
        print("¡Correcto!")
        return 1
    else:
        print("Incorrecto. La respuesta correcta era:", pregunta["respuesta"])
        return 0

def jugar(categoria, dificultad):
    preguntas = preguntas_por_categoria[categoria]
    preguntas_filtradas = filtrar_preguntas_por_dificultad(preguntas, dificultad)
    puntaje = 0

    if len(preguntas_filtradas) == 0:
        print("No hay preguntas disponibles para esa dificultad.")
        return

    indice = 0
    while indice < len(preguntas_filtradas):
        pregunta = preguntas_filtradas[indice]
        puntaje = puntaje + hacer_pregunta(pregunta)
        indice = indice + 1

    print("")
    print("\n🎉 JUEGO FINALIZADO 🎉")
    print("Tu puntaje total fue:", puntaje)

# ===================== PROGRAMA PRINCIPAL =====================
seguir_jugando = "si"

while seguir_jugando == "si":
    limpiar_pantalla()
    mostrar_menu()
    categoria = obtener_opciones()
    dificultad = seleccionar_dificultad()

    limpiar_pantalla()
    print("")
    print("Elegiste la categoría:", categoria)
    print("Elegiste la dificultad:", dificultad)

    jugar(categoria, dificultad)

    print("========= HORA DE FIN DE LA RONDA =========")
    mostrar_hora()

    seguir_jugando = input("\n¿Querés jugar una nueva ronda? (si/no): ")

print("\nGracias por jugar. ¡Hasta la próxima!")

