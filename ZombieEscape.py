from pygame import *
from random import *

matriz_prueba = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# Haremos las cuadrículas del grid de 36x36, por lo que la pantalla tendrá 36x35 de ancho y 36x20 de alto
tamaño_cuadro = 36  # tamaño de cada cuadro de la grid en píxeles
ancho = tamaño_cuadro * 35 # ancho de la pantalla en píxeles
alto = tamaño_cuadro * 20  # alto de la pantalla en píxeles

alto_matriz = len(matriz_prueba)  # largo de la matriz
ancho_matriz = len(matriz_prueba[0])  # ancho de la matriz

# En estas casillas, tendremos la siguiente información:
# 0 = vacío
# 1 = pared
# 2 = jugador
# 3 = enemigo
# 4 = visión del enemigo
# 5 = salida

# Configuración de la ventana 
init()
pantalla = display.set_mode((ancho, alto))  # Configura la ventana
display.set_caption("Dungeon's Sniper")  # Título de la ventana
clock = time.Clock()  # Crea un objeto de reloj para controlar la tasa de refresco, necesario para la física y el movimiento
running = True  # Variable para controlar el bucle principal del juego: mientras sea True, el juego seguirá corriendo
dt = 0  # delta time, utilizado para la física de la tasa de refresco 

def obtener_coords_jugador(): # Esta función obtiene las coordenadas del jugador en la matriz
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            if matriz_prueba[fila][columna] == 2:
                return fila, columna
    return None  # Si no se encuentra el jugador, devuelve None

def limpiar_vision_enemigos():  # Esta función calcula la visión de los enemigos en la matriz
    # Se recorre la matriz y se borra todos los elementos de visión (4)
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            if matriz_prueba[fila][columna] == 4:
                matriz_prueba[fila][columna] = 0

rango_vision = 5  # Rango de visión del enemigo

def enemigo_ve_jugador(fila, columna):  # Función que toma las coordenadas del enemigo y revisa si ve al jugador
    global rango_vision
    # Revisa línea recta en las 4 direcciones
    for direccion_x in [-1, 1]:  # Se revisa arriba y abajo
        for i in range(1, rango_vision + 1):  # Se revisa hasta el rango de visión, iniciando desde 1 para no contar la posición del enemigo
            x, y = fila + direccion_x* i, columna  # Se suman las direcciones a las coordeandas a revisar
            if not (0 <= x < len(matriz_prueba) and 0 <= y < len(matriz_prueba[0])):  # Revisa si está dentro de la matriz 
                break  # Se sale de la matriz
            if matriz_prueba[x][y] == 1:
                break  # Pared
            if matriz_prueba[x][y] == 2:
                return True  # Jugador encontrado
            
    for direccion_y in [-1, 1]:  # Se revisa izquierda y derecha
        for j in range(1, rango_vision + 1):  # Se revisa hasta el rango de visión, iniciando desde 1 para no contar la posición del enemigo
            x, y = fila , columna + direccion_y*j  # Se suman las direcciones a las coordeandas a revisar
            if not (0 <= x < len(matriz_prueba) and 0 <= y < len(matriz_prueba[0])):  # Revisa si está dentro de la matriz 
                break  # Se sale de la matriz
            if matriz_prueba[x][y] == 1:
                break  # Pared
            if matriz_prueba[x][y] == 2:
                return True  # Jugador encontrado
    return False


def vision_enemigos():
    global rango_vision
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            if matriz_prueba[fila][columna] == 3:
                # Para la visión del enemigo, se crean variables para las coordenadas de la matriz y se revisa en todos las direcciones, en forma de cruz
                A = 1  # Arriba
                B = 1  # Abajo
                I = 1  # Izquierda
                D = 1  # Derecha
                # Mientras subamos y no haya pared o enemigo, se crea el area de visión
                while (fila - A) >= 0 and matriz_prueba[fila - A][columna] not in [1, 2, 3] and A <= rango_vision:  
                    matriz_prueba[fila - A][columna] = 4
                    A += 1
                while (fila + B) < len(matriz_prueba) and matriz_prueba[fila + B][columna] not in [1, 2, 3] and B <= rango_vision:
                    matriz_prueba[fila + B][columna] = 4
                    B += 1
                while (columna - I) >= 0 and matriz_prueba[fila][columna - I] not in [1, 2, 3] and I <= rango_vision:
                    matriz_prueba[fila][columna - I] = 4
                    I += 1
                while (columna + D) < len(matriz_prueba[fila]) and matriz_prueba[fila][columna + D] not in [1, 2, 3] and D <= rango_vision:
                    matriz_prueba[fila][columna + D] = 4
                    D += 1


def movimiento_enemigos():
    global alto_matriz, ancho_matriz
    limpiar_vision_enemigos()  # Limpia la visión de los enemigos

    # Lista de enemigos a procesar: esto ya que un enemigo puede moverse a la una posición que no ha sido revisada, y por lo tanto, se vuelve a mover
    enemigos_originales = []  # Para evitar esto, se guardan las posiciones originales de los enemigos
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            if matriz_prueba[fila][columna] == 3:
                enemigos_originales.append((fila, columna))

    for fila, columna in enemigos_originales:
        if matriz_prueba[fila][columna] != 3:
            continue  # Ya se movió desde otra casilla, no pasa nada
        
        # Si en las coordenadas anotadas sigue habiendo un 3, significa que hay un enemigo que no se ha movido, por lo que se sigue con su movimiento
        elif enemigo_ve_jugador(fila, columna):  # Si el enemigo ve al jugador, se mueve hacia él
            player_pos = obtener_coords_jugador()
            if fila < player_pos[0]:  # El jugador se encuntra abajo del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_prueba[(fila + 1) % alto_matriz][columna] not in [1, 3]:
                    matriz_prueba[fila][columna] = 0
                    matriz_prueba[(fila + 1) % alto_matriz][columna] = 3
            elif fila > player_pos[0]:  # El jugador se encuntra arriba del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_prueba[(fila - 1) % alto_matriz][columna] not in [1, 3]:
                    matriz_prueba[fila][columna] = 0
                    matriz_prueba[(fila - 1) % alto_matriz][columna] = 3
            elif columna < player_pos[1]:  # El jugador se encuntra a la derecha del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_prueba[fila][(columna + 1) % ancho_matriz] not in [1, 3]:
                    matriz_prueba[fila][columna] = 0
                    matriz_prueba[fila][(columna + 1) % ancho_matriz] = 3
            elif columna > player_pos[1]:  # El jugador se encuntra a la izquierda del enemigo, por lo que el enemigo se mueve hacia él
                if matriz_prueba[fila][(columna - 1) % ancho_matriz] not in [1, 3]:  # Revisa si no hay pared o enemigo
                    matriz_prueba[fila][columna] = 0
                    matriz_prueba[fila][(columna - 1) % ancho_matriz] = 3
        else:  # Si el enemigo no ve al jugador, se mueve aleatoriamente
            no_movimiento = True
            while no_movimiento:  # Se usa este bucle para evitar que el enemigo no pueda moverse: si las coordeandas random son inválidas, se vuelve a elegir
                se_modifica = choice(["fila", "columna"])
                hacia = choice([-1, 1])
                if se_modifica == "fila":
                    nueva_fila = (fila + hacia) % len(matriz_prueba)
                    if matriz_prueba[nueva_fila][columna] not in [1, 5]:
                        matriz_prueba[fila][columna] = 0
                        matriz_prueba[nueva_fila][columna] = 3
                        no_movimiento = False
                else:
                    nueva_col = (columna + hacia) % len(matriz_prueba[0])
                    if matriz_prueba[fila][nueva_col] not in [1, 5]:
                        matriz_prueba[fila][columna] = 0
                        matriz_prueba[fila][nueva_col] = 3
                        no_movimiento = False

                
def game_over():
    print("GAME OVER, el jugador ha muerto")  # Aquí se puede agregar la lógica para el game over, como reiniciar el juego o mostrar un mensaje
                


def dibujar_matriz():
    # DISCLAIMER: El código no funciona correctamente con (fila, columna) en las coords, ya que no se dibujaría bien
    # Si se quisiera dibujar lo que sale en (0, 1) en la matriz y dibujamos (0, 1) en pantalla, se dibujaría abajo del la esquina inferior izquierda
    # (ya que no nos movemos horizontalmente y bajamos 1 verticalmente): este cuadro se dibujaría realmente en (1, 0), por lo que se debe hacer (columna, fila)
    # para que se dibuje todo correctamente. Al tener (0, 1) en la matriz y hacer (1, 0) en pantalla, nos movemos 1 a la derecha y 0 hacia abajo, por lo que se dibuja
    # correctamente en la posición (0, 1)

    # Se limpia la pantalla
    pantalla.fill("black")

    # Se recorre la matriz: esto para dibujar los cuadros generales de la matriz
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            # Se pintan los cuadros según el valor de la matriz (0 es vacío, 1 es pared, 2 es jugador y 3 es enemigo)
            if matriz_prueba[fila][columna] == 1:
                draw.rect(pantalla, "blue", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz_prueba[fila][columna] == 2:
                # Dibuja el jugador
                draw.rect(pantalla, "green", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz_prueba[fila][columna] == 3:
                # Dibuja al enemigo
                draw.rect(pantalla, "red", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
                vision_enemigos()  # Llama a la función para calcular la visión del enemigo
            elif matriz_prueba[fila][columna] == 4:
                # Dibuja el área de visión del enemigo
                draw.rect(pantalla, "orange", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz_prueba[fila][columna] == 5:
                draw.rect(pantalla, "yellow", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))

# Bucle que corre el juego mientras running sea True
while running:
    player_pos = obtener_coords_jugador()  # Obtiene las coordenadas del jugador
    sniping = False  # Variable para controlar el modo de disparo
    if player_pos is None:  # Si no se encuentra el jugador, se termina el juego
        game_over()

    # Si el evento detectado es QUIT, se deja de correr el juego
    for evento in event.get():
        if evento.type == QUIT:
            running = False

        
        elif evento.type == KEYDOWN:
            if not player_pos is None:  # Si el jugador no es None, se revisa si se presionan las teclas
                # Si se presiona la tecla W, A, S o D, se mueve el jugador en la dirección correspondiente, claramente evitando que se chocque con una pared
                # Gracias a los alto_matriz y ancho_matriz, se genera un loop si el jugador intenta salir de la pantalla, como PAC-MAN
                if evento.key == K_w and matriz_prueba[(player_pos[0] - 1) % alto_matriz][player_pos[1]] not in [1, 3]: # Revisa si no hay pared o enemigo
                    matriz_prueba[player_pos[0]][player_pos[1]] = 0
                    matriz_prueba[(player_pos[0] - 1) % alto_matriz][player_pos[1]] = 2
                    movimiento_enemigos()  # Llama a la función para mover los enemigos cada que el jugador se mueve
                if evento.key == K_s and matriz_prueba[(player_pos[0] + 1) % alto_matriz][player_pos[1]] not in [1, 3]: # Revisa si no hay pared o enemigo
                    matriz_prueba[player_pos[0]][player_pos[1]] = 0
                    matriz_prueba[(player_pos[0] + 1) % alto_matriz][player_pos[1]] = 2
                    movimiento_enemigos()  # Llama a la función para mover los enemigos cada que el jugador se mueve
                if evento.key == K_a and matriz_prueba[player_pos[0]][(player_pos[1] - 1) % ancho_matriz] not in [1, 3]: # Revisa si no hay pared o enemigo
                    matriz_prueba[player_pos[0]][player_pos[1]] = 0
                    matriz_prueba[player_pos[0]][(player_pos[1] - 1) % ancho_matriz] = 2
                    movimiento_enemigos()  # Llama a la función para mover los enemigos cada que el jugador se mueve
                if evento.key == K_d and matriz_prueba[player_pos[0]][(player_pos[1] + 1) % ancho_matriz] not in [1, 3]: # Revisa si no hay pared o enemigo
                    matriz_prueba[player_pos[0]][player_pos[1]] = 0
                    matriz_prueba[player_pos[0]][(player_pos[1] + 1) % ancho_matriz] = 2
                    movimiento_enemigos()  # Llama a la función para mover los enemigos cada que el jugador se mueve
                if evento.key == K_SPACE:  # Si se presiona la barra espaciadora, se activa el modo de disparo
                    sniping = True

        

    # flip() the display to put your work on screen
    display.flip()

    # Llama a la función para dibujar la matriz
    if not sniping:  # Si no está en modo de disparo, se dibuja la matriz de juego
        dibujar_matriz()

    # Usa time.Clock() y la variable dt para limitar la tasa de refresco a 60 FPS
    dt = clock.tick(60) / 1000

quit()