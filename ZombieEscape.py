from pygame import *

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


def calcular_vision_enemigos():  # Esta función calcula la visión de los enemigos en la matriz
    # Se recorre la matriz y se borra todos los elementos de visión (4)
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            if matriz_prueba[fila][columna] == 4:
                matriz_prueba[fila][columna] = 0

    # Se recorre la matriz de nuevo, buscando enemigos (3)    
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            if matriz_prueba[fila][columna] == 3:
                # Aquí se puede implementar la lógica para calcular la visión del enemigo
                 # Para la visión del enemigo, se crean variables para las coordenadas de la matriz y se revisa en todos las direcciones, en forma de cruz
                A = 1  # Arriba
                B = 1  # Abajo
                I = 1  # Izquierda
                D = 1  # Derecha
                rango_vision = 3  # Rango de visión del enemigo
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
                # Anota las coordenadas del jugador
                player_pos = [fila, columna]
            elif matriz_prueba[fila][columna] == 3:
                # Dibuja al enemigo
                draw.rect(pantalla, "red", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
                calcular_vision_enemigos()  # Llama a la función para calcular la visión del enemigo
            elif matriz_prueba[fila][columna] == 4:
                # Dibuja el área de visión del enemigo
                draw.rect(pantalla, "orange", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))
            elif matriz_prueba[fila][columna] == 5:
                draw.rect(pantalla, "yellow", (columna*tamaño_cuadro, fila*tamaño_cuadro, tamaño_cuadro, tamaño_cuadro))


def obtener_coords_jugador(): # Esta función obtiene las coordenadas del jugador en la matriz
    for fila in range(len(matriz_prueba)):
        for columna in range(len(matriz_prueba[fila])):
            if matriz_prueba[fila][columna] == 2:
                return fila, columna


# Bucle que corre el juego mientras running sea True
while running:
    player_pos = obtener_coords_jugador()  # Obtiene las coordenadas del jugador
    # Si el evento detectado es QUIT, se deja de correr el juego
    for evento in event.get():
        if evento.type == QUIT:
            running = False

        elif evento.type == KEYDOWN:
            # Si se presiona la tecla W, A, S o D, se mueve el jugador en la dirección correspondiente, claramente evitando que se chocque con una pared
            # Gracias a los % len(matriz_prueba) y % len(matriz_prueba[0]), se genera un loop si el jugador intenta salir de la pantalla, como PAC-MAN
            if evento.key == K_w and matriz_prueba[(player_pos[0] - 1) % len(matriz_prueba)][player_pos[1]] != 1:
                matriz_prueba[player_pos[0]][player_pos[1]] = 0
                matriz_prueba[(player_pos[0] - 1) % len(matriz_prueba)][player_pos[1]] = 2
            if evento.key == K_s and matriz_prueba[(player_pos[0] + 1) % len(matriz_prueba)][player_pos[1]] != 1:
                matriz_prueba[player_pos[0]][player_pos[1]] = 0
                matriz_prueba[(player_pos[0] + 1) % len(matriz_prueba)][player_pos[1]] = 2
            if evento.key == K_a and matriz_prueba[player_pos[0]][(player_pos[1] - 1) % len(matriz_prueba[0])] != 1:
                matriz_prueba[player_pos[0]][player_pos[1]] = 0
                matriz_prueba[player_pos[0]][(player_pos[1] - 1) % len(matriz_prueba[0])] = 2
            if evento.key == K_d and matriz_prueba[player_pos[0]][(player_pos[1] + 1) % len(matriz_prueba[0])] != 1:
                matriz_prueba[player_pos[0]][player_pos[1]] = 0
                matriz_prueba[player_pos[0]][(player_pos[1] + 1) % len(matriz_prueba[0])] = 2
    print(matriz_prueba)
        

    # flip() the display to put your work on screen
    display.flip()

    # Llama a la función para dibujar la matriz
    dibujar_matriz()

    # Usa time.Clock() y la variable dt para limitar la tasa de refresco a 60 FPS
    dt = clock.tick(60) / 1000

quit()