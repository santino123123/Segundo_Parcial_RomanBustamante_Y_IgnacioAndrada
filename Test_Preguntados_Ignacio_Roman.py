import random

# Desarrollar el núcleo del juego en consola. El juego debe:
# ●	Contener al menos 7 preguntas en total, organizadas en una lista de diccionarios.
# ●	Cada pregunta tendrá una categoría (las categorías tienen que tener relación con la temática que eligieron del juego, por ejemplo superhéroes) y dificultad (otorga más o menos puntaje).
# ●	Mostrar el enunciado, las opciones y registrar respuestas.
# ●	Calcular y mostrar el puntaje final.
# Se evaluará:
# ●	Uso de estructuras de datos (listas, diccionarios, sets, tuplas).
# ●	Control de flujo y condicionales.

def mostrar_general_preguntados():
    print("          P R E G U N T A D O S          ")
    print("1. Fútbol")
    print("2. Videojuegos")
    print("3. Entretenimiento")
    # print("0. Salir")

mostrar_general_preguntados()

# def obtener_opciones():
#     while True:
#         categoria = ""
#         pregunta = int(input("Seleccione una categoria (0/1/2/3): "))          
#         if pregunta == 1:
#             categoria == "Futbol"
#         elif pregunta == 2:
#             categoria == "Videojuego"
#         elif pregunta == 3:
#             categoria == "Entretenimiento"
#         if pregunta == 0:
#             break
#         else:
#             print("Opcion invalida...\nIntente nuevamente!")
#             break
#     return categoria

# obtener_opciones()



def obtener_opciones():
    entrada_valida = False
    while not entrada_valida:
        entrada = int(input("Selecciona una categoría (0-3): "))
        if entrada == 1:
            return 1
        elif entrada == 2:
            return 2
        elif entrada == 3:
            return 3
        else:
            print("Opción inválida. Intenta nuevamente.")
    # return entrada

obtener_opciones()

def mostrar_deficultad():
    print("1. Facil")
    print("2. Intermedio")
    print("3. Dificil")

mostrar_deficultad()


def obtener_dificultad():
    entrada_valida = False
    while not entrada_valida:
        dificultad = int(input("Selecciona una dificultad (1-3): "))
        if dificultad == 1:
            return 1
        elif dificultad == 2:
            return 2
        elif dificultad == 3:
            return 3
        else:
            print("Opción inválida. Intenta nuevamente.")
    # return dificultad

obtener_dificultad()


def obtener_lista_palabras() -> dict:
    preguntas_por_categoria = {
        "Fútbol": [
            {
                "pregunta": "¿Qué país ganó el primer Mundial de Fútbol en 1930?",
                "opciones": ["a) Brasil", "b) Uruguay", "c) Argentina", "d) Italia"],
                "respuesta": "b",
                "puntos": 1
            },
            {
                "pregunta": "¿Qué jugador tiene más goles en la historia de los Mundiales?",
                "opciones": ["a) Pelé", "b) Miroslav Klose", "c) Ronaldo", "d) Messi"],
                "respuesta": "b", 
                "puntos": 2
            },
            {
                "pregunta": "¿En qué año se fundó la FIFA?",
                "opciones": ["a) 1904", "b) 1910", "c) 1921", "d) 1930"],
                "respuesta": "a",
                "puntos": 1
            }
        ], 
        "Videojuegos": [
            {
                "pregunta": "¿Qué personaje dice 'It's-a me, Mario!'?",
                "opciones": ["a) Luigi", "b) Wario", "c) Mario", "d) Toad"],
                "respuesta": "c",
                "puntos": 1
            },
            {
                "pregunta": "¿Qué compañía creó la consola PlayStation?",
                "opciones": ["a) Nintendo", "b) Microsoft", "c) Sony", "d) Sega"],
                "respuesta": "c",
                "puntos": 1
            },
            {
                "pregunta": "¿Cuál fue el primer juego de la saga Legend of Zelda?",
                "opciones": ["a) Ocarina of Time", "b) A Link to the Past", "c) The Legend of Zelda", "d) Breath of the Wild"],
                "respuesta": "c",
                "puntos": 2
            }
        ],
        "Entretenimiento": [
            {
                "pregunta": "¿Qué actor interpretó a Iron Man en el MCU?",
                "opciones": ["a) Chris Evans", "b) Robert Downey Jr.", "c) Chris Hemsworth", "d) Mark Ruffalo"],
                "respuesta": "b",
                "puntos": 1
            },
            {
                "pregunta": "¿Cómo se llama el protagonista de Breaking Bad?",
                "opciones": ["a) Jesse Pinkman", "b) Walter White", "c) Saul Goodman", "d) Mike Ehrmantraut"],
                "respuesta": "b",
                "puntos": 1
            },
            {
                "pregunta": "¿Qué estudio animó la película 'El Rey León' original?",
                "opciones": ["a) Pixar", "b) DreamWorks", "c) Disney", "d) Studio Ghibli"],
                "respuesta": "c", 
                "puntos": 1
            }
        ]
    }
    return preguntas_por_categoria




# def obtener_lista_respuestas() -> list:
#     respuestas_por_categoria = {
#         "Deportes": [
#             "python", "javascript", "algoritmo"
#         ],
#         "Entretenimiento": [
#             "futbol", "basketball", "tenis"
#         ],
#         "videojuegos": [
#             "cso", "zelda", "pokemon", "minecraft"
#         ]
#     }
#     return respuestas_por_categoria

def seleccionar_categoria(lista_categorias):
    for i in range(len(lista_categorias)):
        print(f"{i + 1}. {lista_categorias[i]}")
    
    entrada_valida = False
    while not entrada_valida:
        entrada = input("Selecciona una categoría por número: ")
        if entrada.isdigit():  # solo si es número
            opcion = int(entrada)
            if opcion >= 1 and opcion <= len(lista_categorias):
                entrada_valida = True
                return lista_categorias[opcion - 1]
            else:
                print("Número fuera de rango. Intenta otra vez.")
        else:
            print("Eso no es un número. Intenta de nuevo.")

def obtener_categorias():
    categorias = []
    for clave in obtener_lista_palabras().keys():
        categorias.append(clave)
    return categorias


def seleccionar_palabra(palabras_por_categoria, categoria):
    palabra_elegida = random.choice(palabras_por_categoria[categoria])
    return palabra_elegida


def jugar_ahorcado():
    mostrar_general_preguntados()
    categorias = obtener_categorias()
    categoria = seleccionar_categoria(categorias)
    lista = obtener_lista_palabras(categoria)
    palabra = seleccionar_palabra(lista, categoria)
    print(f"Categoría seleccionada: {categoria}")
    print(f"Pregunta seleccionada: {palabra['pregunta']}")
    for opcion in palabra["opciones"]:
        print(opcion)


jugar_ahorcado()


