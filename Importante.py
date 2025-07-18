import random
import time
import json
import os
from preguntas import *

def seleccionar_dificultad(categoria):
    niveles = ["Facil", "Media", "Dificil"]
    return niveles[random.randint(0, 2)]

def filtrar_preguntas_por_dificultad(lista_preguntas, nivel):
    resultado = []
    for pregunta in lista_preguntas:
        if pregunta["puntos"] == nivel:
            resultado.append(pregunta)
    return resultado

def aplicar_comodin(pregunta):
    correcta = pregunta["respuesta"]
    claves = ["a", "b", "c", "d"]
    incorrectas = []
    for clave in claves:
        if clave != correcta:
            incorrectas.append(clave)

    eliminadas = []
    while len(eliminadas) < 2:
        r = random.choice(incorrectas)
        if r not in eliminadas:
            eliminadas.append(r)
    return eliminadas

def hacer_pregunta(pregunta, usar_comodin):
    print("")
    print("📢 PREGUNTA:")
    print(pregunta["pregunta"])
    eliminadas = []

    if usar_comodin:
        eliminadas = aplicar_comodin(pregunta)
        print("🎯 Comodín activado. Se eliminaron dos opciones incorrectas.")

    for clave in pregunta["opciones"]:
        if clave not in eliminadas:
            print(clave + ")", pregunta["opciones"][clave])

    respuesta = input("Tu respuesta (a/b/c/d): ")
    if respuesta == pregunta["respuesta"]:
        print("✅ ¡Correcto!")
        return 1
    print("❌ Incorrecto. La respuesta correcta era:", pregunta["respuesta"])
    return 0

def jugar_preguntados(nombre_jugador):
    puntos = 0
    vidas = 3
    rondas_jugadas = 0
    usar_comodin = False

    while rondas_jugadas < 5 and vidas > 0:
        categoria = random.choice(list(preguntas_por_categoria.keys()))
        dificultad = seleccionar_dificultad(categoria)
        preguntas_categoria = preguntas_por_categoria[categoria]
        preguntas_filtradas = filtrar_preguntas_por_dificultad(preguntas_categoria, dificultad)

        if len(preguntas_filtradas) == 0:
            continue

        seleccionada = preguntas_filtradas[random.randint(0, len(preguntas_filtradas) - 1)]

        print("")
        print("📚 Categoría:", categoria)
        print("🎯 Dificultad:", dificultad)
        print("❤️ Vidas:", vidas)
        print("⭐ Puntos:", puntos)

        if puntos >= 3 and not usar_comodin:
            decision = input("¿Querés usar el comodín 50/50? (si/no): ")
            if decision == "si":
                usar_comodin = True

        resultado = hacer_pregunta(seleccionada, usar_comodin)

        if resultado == 1:
            puntos += 1
        else:
            vidas -= 1

        rondas_jugadas += 1

    print("")
    print("🎉 JUEGO FINALIZADO 🎉")
    print("Puntaje final:", puntos)
    print("Vidas restantes:", vidas)

    if puntos == 5:
        print("🏆 ¡Increíble! Contestaste todas correctamente.")
    elif puntos >= 3:
        print("🎁 ¡Muy bien! Sos un genio del conocimiento.")
    elif puntos > 0:
        print("👍 Aprobaste. ¡Seguí practicando!")
    else:
        print("😅 Mejor suerte la próxima.")

    guardar_estadisticas(nombre_jugador, puntos, rondas_jugadas)
    return puntos

def guardar_estadisticas(nombre, total_puntos, rondas_jugadas):
    estadistica = {
        "nombre": nombre,
        "puntos_totales": total_puntos,
        "rondas_jugadas": rondas_jugadas,
        "fecha": time.strftime("%Y-%m-%d"),
        "hora": time.strftime("%H:%M:%S")
    }

    historial = []

    if not os.path.exists("estadisticas.json"):
        with open("estadisticas.json", "w") as f:
            f.write("[]")

    with open("estadisticas.json", "r") as archivo:
        contenido = archivo.read().strip()
        if contenido.startswith("[") and contenido.endswith("]"):
            if contenido != "":
                historial = json.loads(contenido)
        else:
            historial = []

    historial.append(estadistica)

    with open("estadisticas.json", "w") as archivo:
        json.dump(historial, archivo, indent=4)

    print("")
    print("📊 ESTADÍSTICAS GUARDADAS 📊")
    print("Jugador:", nombre)
    print("Total de puntos:", total_puntos)
    print("Rondas jugadas:", rondas_jugadas)
    print("Fecha:", estadistica["fecha"])
    print("Hora:", estadistica["hora"])
