# ==================================================================================================================
#   CONFIGURACIÓN INICIAL DEL JUEGO (INICIO, SONIDO, RESOLUCIÓN, GUARDADOS Y MATRICES)
# ==================================================================================================================

from pygame import *
from random import *

FILE_NAME = "guardados.txt"  # Nombre del archivo que contiene las matrices de mapas

def guardar_archivo(file_path, content):
        archivo = open(file_path, 'w') # w crea o trunca el archivo
        archivo.write(content)
        archivo.close()

#lee la información de un archivo
#E: path
#S: string con el contenido del archivo
def leer_archivo(path):
        archivo = open(path, 'r')
        contenido = archivo.read()
        archivo.close()
        return contenido

# Tendremos la siguiente información:
# 0 = vacío
# 1 = pared
# 2 = jugador
# 3 = enemigo
# 4 = visión del enemigo
# 5 = escondite
# 6 = escondite usado
# 7 = salida

# Haremos las cuadrículas del grid de 36x36, por lo que la pantalla tendrá 36x35 de ancho y 36x20 de alto
tamaño_cuadro = 36  # tamaño de cada cuadro de la grid en píxeles
cantidad_cuadros_ancho = 35  # cantidad de cuadros en el ancho
cantidad_cuadros_alto = 20  # cantidad de cuadros en el alto
cantidad_cuadros_menu = 3

ancho = tamaño_cuadro * (cantidad_cuadros_ancho + cantidad_cuadros_menu) # ancho de la pantalla en píxeles
alto = tamaño_cuadro * cantidad_cuadros_alto  # alto de la pantalla en píxeles

# Genera una matriz para poder disparar
def generador_matriz_aleatoria():
    global cantidad_cuadros_ancho, cantidad_cuadros_alto
    matriz = [[0 for _ in range(cantidad_cuadros_ancho)] for _ in range(cantidad_cuadros_alto)]  # Inicializa la matriz con ceros (igual a la matriz de prueba)
    
    tamaño_acierto = 8  # Tamaño del acierto (no puede ser mayor a la cantidad de cuadros en el alto)

    # Con la matriz generada, crearemos un cuadro de 8x8 donde acertar la bala del jugador
    punto_inicio_cuadro = (randint(0, cantidad_cuadros_alto - tamaño_acierto), randint(0, cantidad_cuadros_alto - tamaño_acierto))   # Genera una posición aleatoria donde inciarlo
    for fila in range(cantidad_cuadros_alto):
        for columna in range(cantidad_cuadros_ancho):
            if (fila, columna) == punto_inicio_cuadro:  # Si la posición es la misma que la generada, se inicia el cuad
                for i in range(tamaño_acierto):  # Crea un cuadro de 8x8
                    for j in range(tamaño_acierto):
                        matriz[fila + i][columna + j] = 3  
                break  # Sale del bucle
    return matriz


# Configuración de la ventana 
init()
pantalla = display.set_mode((ancho, alto))  # Configura la ventana
display.set_caption("Dungeon's Sniper")  # Título de la ventana
clock = time.Clock()  # Crea un objeto de reloj para controlar la tasa de refresco, necesario para la física y el movimiento
running = True  # Variable para controlar el bucle principal del juego: mientras sea True, el juego seguirá corriendo
dt = 0  # delta time, utilizado para la física de la tasa de refresco 
fuente_texto = font.Font("assets/FUENTEJUEGO.TTF", 30)
guardados = eval(leer_archivo(FILE_NAME))
# print("Guardados cargados:", guardados)  # Imprime los guardados cargados

# ==================================================================================================================
#   SET DE VARIABLES
# ==================================================================================================================
# Variables para controlar el estado del juego
menu_activo = True  # Variable para controlar si se está en el menú o no
selector_activo = False  # Variable para controlar si se está en el selector de nivel o no
pasando_nivel_activo = False  # Variable para controlar si se está pasando de nivel o no
game_over_activo = False  # Variable para controlar si se está en el game over o no
ganar_juego_activo = False  # Variable para controlar si se ha ganado el juego o no

# Variables para controlar el disparo
sniping = False  # Variable para controlar el modo de disparo
angulo = 0  # Variable para controlar el ángulo de la mira
disparo = False  # Variable para controlar si se disparó o no
matriz_disparo = None  # Guarda la matriz de disparo
mostrando_disparo = False  # Variable para controlar si se está mostrando el disparo
cantidad_disparos = 5 # Variable para controlar la cantidad de disparos disponibles
coords_enemigo_eliminar = None  # Variable para guardar las coordenadas del enemigo que se quiere elminar

# Varibles para controlar eventos y tiempos
mostrando_disparo = False  # Variable para controlar si se está mostrando el disparo
tiempo_disparo= None # Variable para controlar el tiempo transcurrido desde el disparo
tiempo_pasando_nivel = None  # Variable para controlar el tiempo transcurrido desde que se pasó de nivel
tiempo_game_over = None  # Variable para controlar el tiempo transcurrido desde que se inició el game over
tiempo_mostrar_pantallas = 2000 # Variable para controlar cuanto tiempo se muestra el disparo, antes de volver al juego (en milisegundos)

# Variables para controlar la matriz del juego y la posición del jugador
matriz_juego = None  # Variable para guardar la matriz del juego, que se establecerá al seleccionar un nivel
player_pos = None  # Variable para guardar las coordenadas del jugador, que se establecerá al seleccionar un nivel

# ==================================================================================================================
#   SET DE IMÁGENES UTILIZADAS Y TEXTO
# ==================================================================================================================
mira = image.load("assets/CirculoMira.png")  # Carga la imagen de la mira
imagen_inicio = image.load("assets/ImagenMago.png")  # Carga la imagen de inicio
icono_municion = image.load("assets/IconoMunicion.png")  # Carga el icono de munición
gorro_seleccion = image.load("assets/GorroSeleccion.png")  # Carga el icono de selección de nivel

# ==================================================================================================================
#   FUNCIONES DEL JUEGO (DIBUJO Y MECÁNICAS)
# ==================================================================================================================

def verificar_validez_nivel(indi_nivel):  # Esta función verifica si el nivel es válido
    global guardados, cantidad_cuadros_ancho, cantidad_cuadros_alto
    tiene_1_solo_jugador = False  # Variable para verificar si hay un solo jugador en el nivel
    tiene_1_sola_salida = False  # Variable para verificar si hay una sola salida en el nivel
    for fila in range(len(guardados[indi_nivel])):
        if len(guardados[indi_nivel][fila]) != cantidad_cuadros_ancho:  # Revisa si la fila tiene la cantidad de columnas correcta
            break  # Si no tiene la cantidad de columnas correcta, se salta el nivel
        for columna in range(len(guardados[indi_nivel][fila])):
            if guardados[indi_nivel][fila][columna] == 2 and not tiene_1_solo_jugador:  # Revisa si hay un jugador
                tiene_1_solo_jugador = True  # Si hay un jugador, se cambia la variable a True
            elif guardados[indi_nivel][fila][columna] == 2 and tiene_1_solo_jugador:
                tiene_1_solo_jugador = False
                break
            if guardados[indi_nivel][fila][columna] == 7 and not tiene_1_sola_salida:  # Revisa si hay una salida
                tiene_1_sola_salida = True  # Si hay una salida, se cambia la variable a True
            elif guardados[indi_nivel][fila][columna] == 7 and tiene_1_sola_salida:
                tiene_1_sola_salida = False
                break
    
    if tiene_1_solo_jugador and tiene_1_sola_salida:  # Si hay un solo jugador y una sola salida, el nivel es válido
        return True 
    return False # Si no, el nivel no es válido

indi_nivel_seleccionado = 0  # Nivel seleccionado por el jugador

def dibujar_menu():  # Esta función muestra el menú principal del juego
    pantalla.blit(imagen_inicio, (0, 0))  # Pone la imágen de inicio en la pantalla


def dibujar_menu_seleccion_nivel():
    global indi_nivel_seleccionado
    pantalla.fill("black")

    # Letras para el título y las instrucciones
    titulo = fuente_texto.render("Selector de nivel", False, "white")
    instrucciones = fuente_texto.render("<- / -> para cambiar de nivel", False, "gray")
    confirmar = fuente_texto.render("Enter para jugar", False, "gray")

    # Se pone el título y las instrucciones en la pantalla, centradas 
    # Nos ubicamos en la mitad (ancho // 2) y restamos la mitad del ancho del texto para centrarlo: esto se hace con todas las intstrucciones
    pantalla.blit(titulo, ((ancho // 2) - titulo.get_width() // 2, 50)) 
    pantalla.blit(instrucciones, ((ancho // 2) - instrucciones.get_width() // 2, 100))  
    pantalla.blit(confirmar, ((ancho // 2) - confirmar.get_width() // 2, 400))

    # Se hace igual con el gorro, que funciona como elemento decorativo
    pantalla.blit(gorro_seleccion, ((ancho // 2) - gorro_seleccion.get_width() // 2, 300)) 

    # Texto del nivel seleccionado y los niveles que hay disponibles
    texto_nivel = fuente_texto.render(f"Nivel {indi_nivel_seleccionado + 1} de {len(guardados)}", False, "green" if verificar_validez_nivel(indi_nivel_seleccionado) else "red")  # Se pone el texto del nivel seleccionado, con color verde si es válido y rojo si no lo es
    pantalla.blit(texto_nivel, ((ancho // 2) - texto_nivel.get_width() // 2, 200))

    if not verificar_validez_nivel(indi_nivel_seleccionado):
        texto_error = fuente_texto.render("Nivel inválido", False, "red")
        pantalla.blit(texto_error, ((ancho // 2) - texto_error.get_width() // 2, 250))  # Se pone el texto de error si el nivel no es válido

def cambio_nivel(nivel):  # Esta función cambia el nivel del juego
    global indi_nivel_seleccionado
    indi_nivel_seleccionado = (indi_nivel_seleccionado + nivel) % len(guardados)  # Cambia el nivel seleccionado a uno de la lista de niveles válidos

def dibujar_hud():  # Esta función muestra el HUD del juego
    global ancho, alto, cantidad_cuadros_ancho, tamaño_cuadro,cantidad_disparos
    draw.rect(pantalla, "black", (cantidad_cuadros_ancho * tamaño_cuadro, 0, ancho*tamaño_cuadro, alto*tamaño_cuadro))  # Dibuja un rectángulo gris en la parte derecha para el HUD
    disparos_restantes = fuente_texto.render(f"x{cantidad_disparos}", False, "white")  # Renderiza el texto de la cantidad de disparos restantes
    pantalla.blit(disparos_restantes, ((cantidad_cuadros_ancho + 1.35)* tamaño_cuadro, 20))  # Dibuja el texto en la pantalla
    pantalla.blit(icono_municion, ((cantidad_cuadros_ancho + 0.9)* tamaño_cuadro, 30))  # Dibuja el icono de munición en la pantalla

def dibujar_matriz(matriz):
    # DISCLAIMER: El código no funciona correctamente con (fila, columna) en las coords, ya que no se dibujaría bien
    # Si se quisiera dibujar lo que sale en (0, 1) en la matriz y dibujamos (0, 1) en pantalla, se dibujaría abajo del la esquina inferior izquierda
    # (ya que no nos movemos horizontalmente y bajamos 1 verticalmente): este cuadro se dibujaría realmente en (1, 0), por lo que se debe hacer (columna, fila)
    # para que se dibuje todo correctamente. Al tener (0, 1) en la matriz y hacer (1, 0) en pantalla, nos movemos 1 a la derecha y 0 hacia abajo, por lo que se dibuja
    # correctamente en la posición (0, 1)

    # Se limpia la pantalla
    pantalla.fill("black")

    # Se recorre la matriz: esto para dibujar los cuadros generales de la matriz
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            # Se pintan los cuadros según el valor de la matriz (0 es vacío, 1 es pared, 2 es jugador y 3 es enemigo)
            if matriz[fila][columna] == 1:
                draw.rect(pantalla, "blue", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz[fila][columna] == 2:
                # Dibuja el jugador
                draw.rect(pantalla, "green", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz[fila][columna] == 3:
                # Dibuja al enemigo
                draw.rect(pantalla, "red", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
                vision_enemigos()  # Llama a la función para calcular la visión del enemigo
            elif matriz[fila][columna] == 4:
                # Dibuja el área de visión del enemigo
                draw.rect(pantalla, "orange", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz[fila][columna] == 5:
                draw.rect(pantalla, "violet", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz[fila][columna] == 6:
                draw.rect(pantalla, "pink", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz[fila][columna] == 7:
                draw.rect(pantalla, "yellow", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))

def paso_de_nivel():  # Esta función se encarga de pasar al siguiente nivel
    global indi_nivel_seleccionado, matriz_juego, pasando_nivel_activo, tiempo_pasando_nivel, ganar_juego_activo, cantidad_disparos
    
    pasando_nivel_activo = True  # Activa la variable para pasar al siguiente nivel
    tiempo_pasando_nivel = time.get_ticks()  # Guarda el tiempo de inicio del paso de nivel
    cantidad_disparos = 5  # Reinicia la cantidad de disparos a 5 al pasar de nivel

    cambio_nivel(indi_nivel_seleccionado + 1)  # Cambia al siguiente nivel
    while not verificar_validez_nivel(indi_nivel_seleccionado):  # Si el nivel no es válido, se cambia al siguiente nivel
        cambio_nivel(indi_nivel_seleccionado + 1)  # Cambia al siguiente nivel
        if cambio_nivel == len(guardados):
            ganar_juego_activo = True  # Si se llega al último nivel, se activa la variable de ganar el juego
            pasando_nivel_activo = False  # Si se llega al último nivel, se activa la variable de ganar el juego
    matriz_juego = guardados[indi_nivel_seleccionado]  # Se carga la matriz del nivel seleccionado


def dibujar_paso_de_nivel():  # Esta función se encarga de pasar al siguiente nivel
    pantalla.fill("black")
    # Letras para el mensaje de éxito y el paso de nivel
    mensaje_exito = fuente_texto.render("¡Felicidades! Pasaste de nivel", False, "white")
    nivel_a_pasar = fuente_texto.render(f"Pasando al nivel {indi_nivel_seleccionado + 1}", False, "gray")

    # Se pone el título y las instrucciones en la pantalla, centradas 
    # Nos ubicamos en la mitad (ancho // 2) y restamos la mitad del ancho del texto para centrarlo: esto se hace con todas las intstrucciones
    pantalla.blit(mensaje_exito, ((ancho // 2) - mensaje_exito.get_width() // 2, 50)) 
    pantalla.blit(nivel_a_pasar, ((ancho // 2) - nivel_a_pasar.get_width() // 2, 100))  

    # Se hace igual con el gorro, que funciona como elemento decorativo
    pantalla.blit(gorro_seleccion, ((ancho // 2) - gorro_seleccion.get_width() // 2, 300)) 


def dibujar_ganar_juego():  # Esta función se encarga de mostrar el mensaje de victoria al jugador
    global indi_nivel_seleccionado, matriz_juego
    pantalla.fill("black")
    cambio_nivel(indi_nivel_seleccionado + 1)  # Cambia al siguiente nivel

    # Letras para el título y las instrucciones
    mensaje_exito = fuente_texto.render("¡Felicidades! Lograste terminar el juego", False, "white")

    while not verificar_validez_nivel(indi_nivel_seleccionado):  # Si el nivel no es válido, se cambia al siguiente nivel
        cambio_nivel(indi_nivel_seleccionado + 1)  # Cambia al siguiente nivel
    matriz_juego = guardados[indi_nivel_seleccionado]  # Se carga la matriz del nivel seleccionado
    nivel_a_pasar = fuente_texto.render(f"Pasando al nivel {indi_nivel_seleccionado + 1}", False, "gray")

    # Se pone el título y las instrucciones en la pantalla, centradas 
    # Nos ubicamos en la mitad (ancho // 2) y restamos la mitad del ancho del texto para centrarlo: esto se hace con todas las intstrucciones
    pantalla.blit(mensaje_exito, ((ancho // 2) - mensaje_exito.get_width() // 2, 50)) 
    pantalla.blit(nivel_a_pasar, ((ancho // 2) - nivel_a_pasar.get_width() // 2, 100))  


def dibujar_game_over():
    print("GAME OVER, el jugador ha muerto")  # Aquí se puede agregar la lógica para el game over, como reiniciar el juego o mostrar un mensaje

def obtener_coords_jugador(): # Esta función obtiene las coordenadas del jugador en la matriz
    global matriz_juego
    for fila in range(len(matriz_juego)):
        for columna in range(len(matriz_juego[fila])):
            if matriz_juego[fila][columna] == 2 or matriz_juego[fila][columna] == 6:  # Revisa si hay un jugador o un escondite usado
                return fila, columna
    return None  # Si no se encuentra el jugador, devuelve None

def limpiar_vision_enemigos():  # Esta función calcula la visión de los enemigos en la matriz
    global matriz_juego
    # Se recorre la matriz y se borra todos los elementos de visión (4)
    for fila in range(len(matriz_juego)):
        for columna in range(len(matriz_juego[fila])):
            if matriz_juego[fila][columna] == 4:
                matriz_juego[fila][columna] = 0

rango_vision = 5  # Rango de visión del enemigo

def enemigo_ve_jugador(fila, columna):  # Función que toma las coordenadas del enemigo y revisa si ve al jugador
    global rango_vision, matriz_juego
    # Revisa línea recta en las 4 direcciones
    for direccion_x in [-1, 1]:  # Se revisa arriba y abajo
        for i in range(1, rango_vision + 1):  # Se revisa hasta el rango de visión, iniciando desde 1 para no contar la posición del enemigo
            x, y = fila + direccion_x* i, columna  # Se suman las direcciones a las coordeandas a revisar
            if not (0 <= x < len(matriz_juego) and 0 <= y < len(matriz_juego[0])):  # Revisa si está dentro de la matriz 
                break  # Se sale de la matriz
            if matriz_juego[x][y] == 1:
                break  # Pared
            if matriz_juego[x][y] == 2:
                return True  # Jugador encontrado
            
    for direccion_y in [-1, 1]:  # Se revisa izquierda y derecha
        for j in range(1, rango_vision + 1):  # Se revisa hasta el rango de visión, iniciando desde 1 para no contar la posición del enemigo
            x, y = fila , columna + direccion_y*j  # Se suman las direcciones a las coordeandas a revisar
            if not (0 <= x < len(matriz_juego) and 0 <= y < len(matriz_juego[0])):  # Revisa si está dentro de la matriz 
                break  # Se sale de la matriz
            if matriz_juego[x][y] == 1:
                break  # Pared
            if matriz_juego[x][y] == 2:
                return True  # Jugador encontrado
    return False


def vision_enemigos():
    global rango_vision, matriz_juego
    for fila in range(len(matriz_juego)):
        for columna in range(len(matriz_juego[fila])):
            if matriz_juego[fila][columna] == 3:
                # Para la visión del enemigo, se crean variables para las coordenadas de la matriz y se revisa en todos las direcciones, en forma de cruz
                A = 1  # Arriba
                B = 1  # Abajo
                I = 1  # Izquierda
                D = 1  # Derecha
                # Mientras subamos y no haya un elemento prohibido, se crea el area de visión
                while (fila - A) >= 0 and matriz_juego[fila - A][columna] not in [1, 2, 3, 5, 6, 7] and A <= rango_vision:  
                    matriz_juego[fila - A][columna] = 4
                    A += 1
                while (fila + B) < len(matriz_juego) and matriz_juego[fila + B][columna] not in [1, 2, 3, 5, 6, 7] and B <= rango_vision:
                    matriz_juego[fila + B][columna] = 4
                    B += 1
                while (columna - I) >= 0 and matriz_juego[fila][columna - I] not in [1, 2, 3, 5, 6, 7] and I <= rango_vision:
                    matriz_juego[fila][columna - I] = 4
                    I += 1
                while (columna + D) < len(matriz_juego[fila]) and matriz_juego[fila][columna + D] not in [1, 2, 3, 5, 6, 7] and D <= rango_vision:
                    matriz_juego[fila][columna + D] = 4
                    D += 1


def movimiento_enemigos():
    global matriz_juego, cantidad_cuadros_alto, cantidad_cuadros_ancho
    limpiar_vision_enemigos()  # Limpia la visión de los enemigos

    # Lista de enemigos a procesar: esto ya que un enemigo puede moverse a la una posición que no ha sido revisada, y por lo tanto, se vuelve a mover
    enemigos_originales = []  # Para evitar esto, se guardan las posiciones originales de los enemigos
    for fila in range(len(matriz_juego)):
        for columna in range(len(matriz_juego[fila])):
            if matriz_juego[fila][columna] == 3:
                enemigos_originales.append((fila, columna))

    for fila, columna in enemigos_originales:
        if matriz_juego[fila][columna] != 3:
            continue  # Ya se movió desde otra casilla, no pasa nada
        
        # Si en las coordenadas anotadas sigue habiendo un 3, significa que hay un enemigo que no se ha movido, por lo que se sigue con su movimiento
        elif enemigo_ve_jugador(fila, columna):  # Si el enemigo ve al jugador, se mueve hacia él
            player_pos = obtener_coords_jugador()
            if fila < player_pos[0]:  # El jugador se encuntra abajo del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_juego[(fila + 1) % cantidad_cuadros_alto][columna] not in [1, 3, 5, 6, 7]:
                    matriz_juego[fila][columna] = 0
                    matriz_juego[(fila + 1) % cantidad_cuadros_alto][columna] = 3
            elif fila > player_pos[0]:  # El jugador se encuntra arriba del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_juego[(fila - 1) % cantidad_cuadros_alto][columna] not in [1, 3, 5, 6, 7]:
                    matriz_juego[fila][columna] = 0
                    matriz_juego[(fila - 1) % cantidad_cuadros_alto][columna] = 3
            elif columna < player_pos[1]:  # El jugador se encuntra a la derecha del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_juego[fila][(columna + 1) % cantidad_cuadros_ancho] not in [1, 3, 5, 6, 7]:
                    matriz_juego[fila][columna] = 0
                    matriz_juego[fila][(columna + 1) % cantidad_cuadros_ancho] = 3
            elif columna > player_pos[1]:  # El jugador se encuntra a la izquierda del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_juego[fila][(columna - 1) % cantidad_cuadros_ancho] not in [1, 3, 5, 6, 7]:  # Revisa si no hay pared o enemigo
                    matriz_juego[fila][columna] = 0
                    matriz_juego[fila][(columna - 1) % cantidad_cuadros_ancho] = 3
        else:  # Si el enemigo no ve al jugador, se mueve aleatoriamente
            no_movimiento = True
            while no_movimiento:  # Se usa este bucle para evitar que el enemigo no pueda moverse: si las coordeandas random son inválidas, se vuelve a elegir
                se_modifica = choice(["fila", "columna"])
                hacia = choice([-1, 1])
                if se_modifica == "fila":
                    nueva_fila = (fila + hacia) % len(matriz_juego)
                    if matriz_juego[nueva_fila][columna] not in [1, 2, 3, 5, 6, 7]:
                        matriz_juego[fila][columna] = 0
                        matriz_juego[nueva_fila][columna] = 3
                        no_movimiento = False
                else:
                    nueva_col = (columna + hacia) % len(matriz_juego[0])
                    if matriz_juego[fila][nueva_col] not in [1, 2, 3, 5, 6, 7]:
                        matriz_juego[fila][columna] = 0
                        matriz_juego[fila][nueva_col] = 3
                        no_movimiento = False


def administrar_movimiento_jugador(direccion):  # Esta función administra el movimiento del jugador
    global player_pos, matriz_juego, cantidad_cuadros_alto, cantidad_cuadros_ancho,pasando_nivel_activo, tiempo_pasando_nivel
    # Movimiento hacia arriba
    if direccion == "arriba":
        if matriz_juego[(player_pos[0] - 1) % cantidad_cuadros_alto][player_pos[1]] != 1: # Revisa si no hay pared
            # Tocar un enemigo
            if matriz_juego[(player_pos[0] - 1) % cantidad_cuadros_alto][player_pos[1]] == 3:
                matriz_juego[player_pos[0]][player_pos[1]] = 0  # Elimina al jugador de la matriz
                return # Se acaba la ejecucción de la función, ya que el jugador ha muerto
            
            # Ganar el nivel
            elif matriz_juego[(player_pos[0] - 1) % cantidad_cuadros_alto][player_pos[1]] == 7:
                paso_de_nivel()  # Llama a la función para pasar configurar el paso de nivel
                return # Se acaba la ejecucción de la función, ya ganó el nivel

            # Salida del escondite anterior
            if matriz_juego[player_pos[0]][player_pos[1]] == 6: # Si estaba en un escondite, sale de él
                matriz_juego[player_pos[0]][player_pos[1]] = 5  # Se crea el escondite vacío
            else: # Si no estaba en un escondite, se marca la posición como vacía
                matriz_juego[player_pos[0]][player_pos[1]] = 0

                # Entrar a un nuevo escondite
            if matriz_juego[(player_pos[0] - 1) % cantidad_cuadros_alto][player_pos[1]] == 5:
                matriz_juego[(player_pos[0] - 1) % cantidad_cuadros_alto][player_pos[1]] = 6 # Se marca el escondite como usado
            elif matriz_juego[(player_pos[0] - 1) % cantidad_cuadros_alto][player_pos[1]] == 0:  # Si no hay escondite, se marca la posición como jugador
                matriz_juego[(player_pos[0] - 1) % cantidad_cuadros_alto][player_pos[1]] = 2
            
    # Movimiento hacia abajo
    if direccion == "abajo":
        if matriz_juego[(player_pos[0] + 1) % cantidad_cuadros_alto][player_pos[1]] != 1: # Revisa si no hay pared
            # Tocar un enemigo
            if matriz_juego[(player_pos[0] + 1) % cantidad_cuadros_alto][player_pos[1]] == 3:
                matriz_juego[player_pos[0]][player_pos[1]] = 0  # Elimina al jugador de la matriz
                return # Se acaba la ejecucción de la función, ya que el jugador ha muerto
            
            # Ganar el nivel
            if matriz_juego[(player_pos[0] + 1) % cantidad_cuadros_alto][player_pos[1]] == 7:
                paso_de_nivel()  # Llama a la función para pasar configurar el paso de nivel
                return # Se acaba la ejecucción de la función, ya ganó el nivel
            
            # Salida del escondite anterior
            if matriz_juego[player_pos[0]][player_pos[1]] == 6: # Si estaba en un escondite, sale de él
                matriz_juego[player_pos[0]][player_pos[1]] = 5  # Se crea el escondite vacío
            else: # Si no estaba en un escondite, se marca la posición como vacía
                matriz_juego[player_pos[0]][player_pos[1]] = 0

            # Entrar a un nuevo escondite
            if matriz_juego[(player_pos[0] + 1) % cantidad_cuadros_alto][player_pos[1]] == 5:
                matriz_juego[(player_pos[0] + 1) % cantidad_cuadros_alto][player_pos[1]] = 6 # Se marca el escondite como usado
            else:  # Si no hay escondite, se marca la posición como jugador
                matriz_juego[(player_pos[0] + 1) % cantidad_cuadros_alto][player_pos[1]] = 2
                
    # Movimiento hacia la izquierda        
    if direccion == "izquierda":
        if matriz_juego[player_pos[0]][(player_pos[1] - 1) % cantidad_cuadros_ancho] != 1: # Revisa si no hay pared
            # Tocar un enemigo
            if matriz_juego[player_pos[0]][(player_pos[1] - 1) % cantidad_cuadros_ancho] == 3:
                matriz_juego[player_pos[0]][player_pos[1]] = 0  # Elimina al jugador de la matriz
                return # Se acaba la ejecucción de la función, ya que el jugador ha muerto
            
            # Ganar el nivel
            if matriz_juego[player_pos[0]][(player_pos[1] - 1) % cantidad_cuadros_ancho] == 7:
                paso_de_nivel()  # Llama a la función para pasar configurar el paso de nivel
                return # Se acaba la ejecucción de la función, ya ganó el nivel

            # Salida del escondite anterior
            if matriz_juego[player_pos[0]][player_pos[1]] == 6: # Si estaba en un escondite, sale de él
                matriz_juego[player_pos[0]][player_pos[1]] = 5  # Se crea el escondite vacío
            else: # Si no estaba en un escondite, se marca la posición como vacía
                matriz_juego[player_pos[0]][player_pos[1]] = 0

            # Entrar a un nuevo escondite
            if matriz_juego[player_pos[0]][(player_pos[1] - 1) % cantidad_cuadros_ancho] == 5:
                matriz_juego[player_pos[0]][(player_pos[1] - 1) % cantidad_cuadros_ancho] = 6 # Se marca el escondite como usado
            else:  # Si no hay escondite, se marca la posición como jugador
                matriz_juego[player_pos[0]][(player_pos[1] - 1) % cantidad_cuadros_ancho] = 2

    # Movimiento hacia la derecha
    if direccion == "derecha":
        if matriz_juego[player_pos[0]][(player_pos[1] + 1) % cantidad_cuadros_ancho] != 1:  # Si no hay pared
             # Tocar un enemigo
            if matriz_juego[player_pos[0]][(player_pos[1] + 1) % cantidad_cuadros_ancho] == 3:
                matriz_juego[player_pos[0]][player_pos[1]] = 0  # Elimina al jugador de la matriz
                return # Se acaba la ejecucción de la función, ya que el jugador ha muerto
            
            # Ganar el nivel
            if matriz_juego[player_pos[0]][(player_pos[1] + 1) % cantidad_cuadros_ancho] == 7:
                paso_de_nivel()  # Llama a la función para pasar configurar el paso de nivel
                return # Se acaba la ejecucción de la función, ya ganó el nivel
            
            # Salida del escondite anterior
            if matriz_juego[player_pos[0]][player_pos[1]] == 6: # Si estaba en un escondite, sale de él
                matriz_juego[player_pos[0]][player_pos[1]] = 5  # Se crea el escondite vacío
            else: # Si no estaba en un escondite, se marca la posición como vacía
                matriz_juego[player_pos[0]][player_pos[1]] = 0

            # Entrar a un nuevo escondite
            if matriz_juego[player_pos[0]][(player_pos[1] + 1) % cantidad_cuadros_ancho] == 5:
                matriz_juego[player_pos[0]][(player_pos[1] + 1) % cantidad_cuadros_ancho] = 6 # Se marca el escondite como usado
            else:  # Si no hay escondite, se marca la posición como jugador
                matriz_juego[player_pos[0]][(player_pos[1] + 1) % cantidad_cuadros_ancho] = 2

    movimiento_enemigos()  # Llama a la función para mover los enemigos antes de mover al jugador


def sniping_mode(cursor_pos, disparo=False):
    global angulo, matriz_disparo
    pantalla.fill("black")  # Limpia la pantalla
    if not disparo:  # Si no se disparó, la mira gira
        angulo += 2
    if disparo:
        dibujar_matriz(matriz_disparo)
    # Aumentar ángulo (puedes ajustar la velocidad aquí)
    # Rotar la imagen
    imagen_rotada = transform.rotate(mira, angulo)  # Rota la imagen de la mira
    pantalla.blit(imagen_rotada, (cursor_pos[0] - imagen_rotada.get_width() // 2, cursor_pos[1] - imagen_rotada.get_height() // 2))  # Dibuja la imagen rotada en la posición del cursor

def cursor_en_pos_valida(cursor_pos, matriz):
    global tamaño_cuadro
    # Se obtiene la posición del mouse y se convierte a coordenadas de la matriz
    fila = cursor_pos[1] // tamaño_cuadro
    columna = cursor_pos[0] // tamaño_cuadro
    # Se revisa si la posición está dentro de la matriz
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
        if matriz[fila][columna] == 3:
            return True  # Si la posición es un enemigo, se devuelve True
        return False  # Si la posición no es un enemigo, se devuelve False
    return None  # Si la posición no está dentro de la matriz, se devuelve None

def administrar_disparo():
    global disparo, cantidad_disparos, mostrando_disparo, tiempo_disparo, matriz_disparo, coords_enemigo_eliminar, matriz_juego
    disparo = True  # Se activa la variable de disparo (esto detiene la rotación de la mira)
    cantidad_disparos -= 1  # Se resta 1 al contador de disparos
    mostrando_disparo = True  # Se activa la variable para mostrar el disparo
    tiempo_disparo = time.get_ticks()  # Se guarda el tiempo en el que se disparó
    if cursor_en_pos_valida(mouse.get_pos(), matriz_disparo) == None:
        print("No es válido disparar aquí")
        # Lógica para que no ocurra nada si el disparo no es válido
        disparo = False
        mostrando_disparo = False
        tiempo_disparo = None  # Reinicia el tiempo de cuando se disparó
        cantidad_disparos += 1  # Se suma 1 al contador de disparos, ya que no se disparó
    elif cursor_en_pos_valida(mouse.get_pos(), matriz_disparo) == True:
        # Si el disparo es válido, se elimina el enemigo al que se le hizo click
        matriz_juego[coords_enemigo_eliminar[1]][coords_enemigo_eliminar[0]] = 0
        limpiar_vision_enemigos()  # Llama a la función para eliminar los restos del área de visión del enemigo eliminado

# Bucle que corre el juego mientras running sea True
while running:
    if not menu_activo and not selector_activo:  # Si no se está en el menú ni en el selector de nivel, se busca la posición del jugador
        player_pos = obtener_coords_jugador()  # Obtiene las coordenadas del jugador
        if player_pos is None:  # Si no se encuentra el jugador, se termina el juego
            game_over_activo = True  # Se activa la variable de game over

    # Si el evento detectado es QUIT, se deja de correr el juego
    for evento in event.get():
        if evento.type == QUIT:
            running = False

        
        elif evento.type == KEYDOWN:
            if evento.key == K_SPACE and menu_activo:  # Si se presiona la tecla ESCAPE, se sale del juego
                menu_activo = False  # Se sale del menú
                selector_activo = True  # Se activa el selector de nivel

            if evento.key == K_LEFT and selector_activo:  # Si se presiona la tecla izquierda, se cambia al nivel anterior
                # Aquí se puede agregar la lógica para cambiar al nivel anterior
                print("Cambiando al nivel anterior")
                cambio_nivel(-1)

            elif evento.key == K_RIGHT and selector_activo:  # Si se presiona la tecla derecha, se cambia al siguiente nivel
                # Aquí se puede agregar la lógica para cambiar al nivel anterior
                print("Cambiando al siguiente nivel")
                cambio_nivel(+1)

            elif evento.key == K_RETURN and selector_activo:  # Si se presiona la tecla ENTER, se inicia el juego
                if verificar_validez_nivel(indi_nivel_seleccionado):  # Verifica si el nivel que se va a cargar es válido
                    selector_activo = False  # Se desactiva el selector de nivel
                    matriz_juego = guardados[indi_nivel_seleccionado]  # Se carga la matriz del nivel seleccionado

            elif not player_pos is None and not sniping and not menu_activo and not selector_activo:  # Si el jugador no es None y no se está en otro modo, se revisa si se presionan las teclas
                # Si se presiona la tecla W, A, S o D, se mueve el jugador en la dirección correspondiente, claramente evitando que se chocque con una pared
                # Gracias a los alto_matriz y ancho_matriz, se genera un loop si el jugador intenta salir de la pantalla, como PAC-MAN
                if evento.key == K_w:  # Si se presiona la tecla W, se mueve el jugador hacia arriba
                    administrar_movimiento_jugador("arriba")  # Llama a la función para mover al jugador hacia arriba

                if evento.key == K_s:  # Si se presiona la tecla S, se mueve el jugador hacia abajo
                    administrar_movimiento_jugador("abajo")  # Llama a la función para mover al jugador hacia abajo

                if evento.key == K_a:  # Si se presiona la tecla A, se mueve el jugador hacia la izquierda
                    administrar_movimiento_jugador("izquierda")  # Llama a la función para mover al jugador hacia la izquierda

                if evento.key == K_d:  # Si se presiona la tecla D, se mueve el jugador hacia la derecha
                    administrar_movimiento_jugador("derecha")  # Llama a la función para mover al jugador hacia la derecha
            
            if evento.key == K_SPACE and not mostrando_disparo and not menu_activo:  # Si se presiona la barra espaciadora, se desactiva el modo de disparo
                    sniping = False
            
            if evento.key == K_ESCAPE:  # Si se presiona la tecla ESCAPE, se vuelve al menú
                if not menu_activo:  # Si no se está en el menú, se vuelve al menú
                    menu_activo = True  # Se activa el menú
                    selector_activo = False  # Se desactiva el selector de nivel
                    
        elif evento.type == MOUSEBUTTONDOWN and not player_pos is None:  # Si se presiona el cursor, se revisa si se hizo click a un enemigo
            if not sniping:  # Si no se está en modo de disparo, se revisa si se hizo click en un enemigo
                x, y = mouse.get_pos()
                x_en_juego = x // tamaño_cuadro  # Convierte la posición del mouse a coordenadas de la matriz
                y_en_juego = y // tamaño_cuadro  # Convierte la posición del mouse a coordenadas de la matriz
                if matriz_juego[y_en_juego][x_en_juego] == 3 and cursor_en_pos_valida((x, y), matriz_juego):  # Si se hizo click en un enemigo
                    # Se activa el modo sniping
                    sniping = True
                    matriz_disparo = generador_matriz_aleatoria()
                    coords_enemigo_eliminar = (x_en_juego, y_en_juego)  # Guarda las coordenadas del enemigo a eliminar
                    print(coords_enemigo_eliminar)
            elif sniping and not disparo and cantidad_disparos > 0:  # Si se está en modo de disparo, no se ha disparado y hay disparos disponibles, se activa la dinámica de disparar
               administrar_disparo()  # Llama a la función para administrar el disparo
        
    if tiempo_disparo is not None and time.get_ticks() - tiempo_disparo >= tiempo_mostrar_pantallas:  # Si se disparó, se revisa si el tiempo transcurrido es mayor al tiempo de mostrar el disparo
        sniping = False  # Se desactiva el modo de disparo
        disparo = False  # Se desactiva la variable de disparo
        mostrando_disparo = False  # Se desactiva la variable para mostrar el disparo
        tiempo_disparo = None  # Se reinicia el tiempo de cuando se disparó
            
    if tiempo_pasando_nivel is not None and time.get_ticks() - tiempo_pasando_nivel >= tiempo_mostrar_pantallas:  # Si se está pasando de nivel, se revisa si el tiempo transcurrido es mayor al tiempo de mostrar el paso de nivel
        pasando_nivel_activo = False  # Se desactiva el paso de nivel

    # flip() the display to put your work on screen
    display.flip()

    # Llama a las respectivas funciones de dibujo, según el estado del juego
    if menu_activo :  # Si se está en el menú, se dibuja el menú
        dibujar_menu()
    elif selector_activo:  # Si se está en el selector de nivel, se dibuja el selector de nivel
        dibujar_menu_seleccion_nivel()
    elif pasando_nivel_activo:  # Si se está pasando de nivel, se dibuja el paso de nivel
        dibujar_paso_de_nivel()
    elif game_over_activo:  # Si se está en el game over, se dibuja el game over
        dibujar_game_over()

    elif not sniping:  # Si no está en modo de disparo, se dibuja la matriz de juego
        dibujar_matriz(matriz_juego)
    elif sniping and disparo:
        # Si se se disparó, si cambia la rotación de la mira en el modo disparo
        sniping_mode(mouse.get_pos(), disparo)
    elif sniping:  # Si está en modo de disparo, se dibuja la matriz de disparo
        sniping_mode(mouse.get_pos())
    if not menu_activo and not selector_activo and not pasando_nivel_activo:  # Si no se está en alguna otra pantalla, se dibuja el HUD
        dibujar_hud()

    # Usa time.Clock() y la variable dt para limitar la tasa de refresco a 60 FPS
    dt = clock.tick(60) / 1000
    # x, y = mouse.get_pos()  # Obtiene la posición del mouse
    # print (y//tamaño_cuadro, x//tamaño_cuadro)  # Imprime la posición del mouse

quit()