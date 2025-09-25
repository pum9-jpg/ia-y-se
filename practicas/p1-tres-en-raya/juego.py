import pygame
import sys

# Inicializar pygame
pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 600, 600
LINEA_ANCHO = 15
TAM_CASILLA = ANCHO // 3

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (28, 170, 156)
ROJO = (200, 0, 0)

# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("3 en Raya")

# Tablero vacío (3x3)
tablero = [[None for _ in range(3)] for _ in range(3)]
jugador = "X"  # Comienza X

# Fuente para texto
fuente = pygame.font.Font(None, 60)


def dibujar_tablero():
    pantalla.fill(BLANCO)
    # Dibujar líneas verticales
    pygame.draw.line(pantalla, NEGRO, (TAM_CASILLA, 0), (TAM_CASILLA, ALTO), LINEA_ANCHO)
    pygame.draw.line(pantalla, NEGRO, (2 * TAM_CASILLA, 0), (2 * TAM_CASILLA, ALTO), LINEA_ANCHO)
    # Dibujar líneas horizontales
    pygame.draw.line(pantalla, NEGRO, (0, TAM_CASILLA), (ANCHO, TAM_CASILLA), LINEA_ANCHO)
    pygame.draw.line(pantalla, NEGRO, (0, 2 * TAM_CASILLA), (ANCHO, 2 * TAM_CASILLA), LINEA_ANCHO)


def dibujar_fichas():
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == "X":
                texto = fuente.render("X", True, ROJO)
                pantalla.blit(texto, (col * TAM_CASILLA + 60, fila * TAM_CASILLA + 40))
            elif tablero[fila][col] == "O":
                texto = fuente.render("O", True, AZUL)
                pantalla.blit(texto, (col * TAM_CASILLA + 60, fila * TAM_CASILLA + 40))


def verificar_ganador():
    # Revisar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] is not None:
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] is not None:
            return tablero[0][i]
    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] is not None:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] is not None:
        return tablero[0][2]
    return None


def mostrar_mensaje(mensaje):
    texto = fuente.render(mensaje, True, NEGRO)
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    pantalla.blit(texto, rect)
    pygame.display.flip()
    pygame.time.wait(2000)


# Bucle principal
ejecutando = True
dibujar_tablero()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            fila = y // TAM_CASILLA
            col = x // TAM_CASILLA

            if tablero[fila][col] is None:
                tablero[fila][col] = jugador
                ganador = verificar_ganador()
                if ganador:
                    dibujar_tablero()
                    dibujar_fichas()
                    mostrar_mensaje(f"Ganó {ganador}!")
                    tablero = [[None for _ in range(3)] for _ in range(3)]  # Reiniciar juego
                else:
                    jugador = "O" if jugador == "X" else "X"

    dibujar_tablero()
    dibujar_fichas()
    pygame.display.flip()

pygame.quit()
sys.exit()