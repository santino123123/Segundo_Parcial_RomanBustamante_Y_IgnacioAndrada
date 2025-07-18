from usuario import limpiar_pantalla
import random

FILAS = 3
COLUMNAS = 3
MINAS = 2

def crear_tablero(filas, columnas, cantidad_minas):
    tablero = [[" " for _ in range(columnas)] for _ in range(filas)]
    minas_colocadas = 0
    while minas_colocadas < cantidad_minas:
        f = random.randint(0, filas - 1)
        c = random.randint(0, columnas - 1)
        if tablero[f][c] != "M":
            tablero[f][c] = "M"
            minas_colocadas += 1
    return tablero

def contar_minas_vecinas(tablero, f, c):
    total = 0
    for i in range(f - 1, f + 2):
        for j in range(c - 1, c + 2):
            if 0 <= i < FILAS and 0 <= j < COLUMNAS:
                if tablero[i][j] == "M":
                    total += 1
    return total

def descubrir(tablero, visible, f, c):
    if 0 <= f < FILAS and 0 <= c < COLUMNAS and visible[f][c] == "#":
        if tablero[f][c] == "M":
            visible[f][c] = "M"
        else:
            minas = contar_minas_vecinas(tablero, f, c)
            visible[f][c] = str(minas)
            if minas == 0:
                for i in range(f - 1, f + 2):
                    for j in range(c - 1, c + 2):
                        if (i != f or j != c):
                            descubrir(tablero, visible, i, j)

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def mostrar_diagonales(tablero):
    print("🔹 Diagonal principal:")
    for i in range(FILAS):
        print(tablero[i][i], end=" ")
    print("\n🔹 Diagonal secundaria:")
    for i in range(FILAS):
        print(tablero[i][COLUMNAS - 1 - i], end=" ")
    print("\n")

def pedir_coordenadas():
    while True:
        try:
            f = int(input("Elegí fila (0-2): "))
            c = int(input("Elegí columna (0-2): "))
            if 0 <= f < FILAS and 0 <= c < COLUMNAS:
                return f, c
            print("⚠️ Coordenadas fuera de rango. Intentá de nuevo.")
        except ValueError:
            print("⚠️ Entrada inválida. Usá solo números 0, 1 o 2.")

def turno_jugador(jugador, tablero, visible):
    print("Turno de", jugador)
    mostrar_tablero(visible)
    f, c = pedir_coordenadas()

    if tablero[f][c] == "M":
        visible[f][c] = "M"
        mostrar_tablero(visible)
        print("💥", jugador, "pisó una mina. ¡Perdió!")
        return False

    descubrir(tablero, visible, f, c)
    return True

def ganador_buscaminas(tablero, visible):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if tablero[i][j] != "M" and visible[i][j] == "#":
                return None
    return "empate"

def ordenar_fila(tablero, fila):
    tablero[fila].sort()

def jugar_buscaminas(modo):
    limpiar_pantalla()
    tablero = crear_tablero(FILAS, COLUMNAS, MINAS)
    visible = [["#" for _ in range(COLUMNAS)] for _ in range(FILAS)]

    jugadores = ["Jugador 1"]
    if modo == 2:
        jugadores.append("Jugador 2")

    turno = 0
    seguir = True

    while seguir:
        actual = jugadores[turno % len(jugadores)]
        seguir = turno_jugador(actual, tablero, visible)

        if seguir is False:
            mostrar_diagonales(tablero)
            ordenar_fila(tablero, 0)
            print("🔃 Fila 0 del tablero ordenada:", tablero[0])
            return jugadores[(turno + 1) % len(jugadores)]

        if ganador_buscaminas(tablero, visible) == "empate":
            print("🎉 ¡Empate! Ambos jugadores evitaron las minas.")
            mostrar_diagonales(tablero)
            ordenar_fila(tablero, 0)
            print("🔃 Fila 0 del tablero ordenada:", tablero[0])
            return "empate"

        turno += 1
