from usuario import *
from importante import *
from buscaminas import *
import json
import csv



def mostrar_estadisticas(ruta_archivo):
    limpiar_pantalla()
    print("══════════════════════════════════════════")
    print("            📊 ESTADÍSTICAS 📊")
    print("══════════════════════════════════════════")
    if not os.path.exists(ruta_archivo):
        print("No hay estadísticas registradas aún.")
        return
    with open(ruta_archivo, "r") as archivo:
        historial = json.load(archivo)
        for estadistica in historial:
            print("──────────────────────────────────")
            print("Jugador:", estadistica["nombre"])
            print("Puntos Totales:", estadistica["puntos_totales"])
            print("Rondas Jugadas:", estadistica["rondas_jugadas"])
            print("Fecha:", estadistica["fecha"], "Hora:", estadistica["hora"])
    print("──────────────────────────────────")

def decidir_orden_jugadores(jugadores, ganador, eleccion):
    orden = []
    if eleccion == "si":
        orden.append(ganador)
        for j in jugadores:
            if j != ganador:
                orden.append(j)
    else:
        for j in jugadores:
            if j != ganador:
                orden.append(j)
        orden.append(ganador)
    return orden

def obtener_ganador_final(puntajes):
    ganador = None
    mayor_puntaje = -1
    for jugador in puntajes:
        if puntajes[jugador] > mayor_puntaje:
            mayor_puntaje = puntajes[jugador]
            ganador = jugador
    return ganador

def ejecutar_juego(jugar_buscaminas_func, jugar_preguntados_func):
    limpiar_pantalla()
    mostrar_menu()

    jugadores = []
    nombre1 = pedir_nombre()
    jugadores.append(nombre1)

    modo = int(input("¿Jugás solo (1) o con otro jugador (2)? "))
    if modo == 2:
        nombre2 = pedir_nombre()
        jugadores.append(nombre2)

    print("¿Querés empezar con:")
    print("1. Preguntados")
    print("2. Buscaminas")
    opcion = input("Elegí (1 o 2): ")

    orden_jugadores = []
    for jugador in jugadores:
        orden_jugadores.append(jugador)

    if opcion == "2":
        ganador = jugar_buscaminas_func(modo)
        if ganador != "empate":
            print(ganador, "ganó el Buscaminas y decide si empieza primero.")
            eleccion = input(f"{ganador} ¿querés jugar primero en Preguntados? (si/no): ")
            orden_jugadores = decidir_orden_jugadores(jugadores, ganador, eleccion)

    puntajes = {}
    for jugador in orden_jugadores:
        print("🎮 Turno de", jugador)
        total = jugar_preguntados_func(jugador)
        puntajes[jugador] = total

    limpiar_pantalla()
    print("🎉 RESULTADOS FINALES 🎉")
    for jugador in puntajes:
        print(jugador, "obtuvo", puntajes[jugador], "puntos")
    ganador_final = obtener_ganador_final(puntajes)
    print(f"🏆 ¡El ganador es {ganador_final}  ! 🏆")

def menu_principal():
    while True:
        limpiar_pantalla()
        print("══════════════════════════════════════════")
        print("            MENÚ PRINCIPAL")
        print("══════════════════════════════════════════")
        print("1. Ver estadísticas")
        print("2. Jugar Preguntados + Buscaminas")
        print("3. Salir")
        opcion = input("Elegí una opción (1-3): ")

        if opcion == "1":
            mostrar_estadisticas("estadisticas.json")
            input("Presioná Enter para volver al menú...")
        elif opcion == "2":
            ejecutar_juego(jugar_buscaminas, jugar_preguntados)
            input("Presioná Enter para volver al menú...")
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")
            input("Presioná Enter para continuar...")

with open("preguntas_exportadas.csv", "w", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["Categoría", "Pregunta", "Opción A", "Opción B", "Opción C", "Opción D", "Respuesta", "Dificultad"])
    for categoria, lista_preguntas in preguntas_por_categoria.items():
        for pregunta in lista_preguntas:
            escritor.writerow([
                categoria,
                pregunta["pregunta"],
                pregunta["opciones"]["a"],
                pregunta["opciones"]["b"],
                pregunta["opciones"]["c"],
                pregunta["opciones"]["d"],
                pregunta["respuesta"],
                pregunta["puntos"]
            ])
print("Preguntas exportadas correctamente a preguntas_exportadas.csv")

menu_principal()
