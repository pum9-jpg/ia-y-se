# Juego 3 en raya en consola (con tablero guía 1-9)

def imprimir_tablero(tablero):
    print("\n")
    for i, fila in enumerate(tablero):
        print("  " + "  |  ".join(fila))
        if i < 2:
            print("-----+-----+-----")
    print("\n")

def imprimir_tablero_guia():
    print("Tablero guía (elige un número del 1 al 9):\n")
    guia = [[str(i + j*3 + 1) for i in range(3)] for j in range(3)]
    for i, fila in enumerate(guia):
        print("  " + "  |  ".join(fila))
        if i < 2:
            print("-----+-----+-----")
    print("\n")

def hay_ganador(tablero, jugador):
    # Revisar filas
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
    # Revisar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
    # Revisar diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    return all(celda != " " for fila in tablero for celda in fila)

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador_actual = "X"

    imprimir_tablero_guia()  # Mostrar guía al inicio

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        print("Elige una casilla (1-9):")

        try:
            movimiento = int(input("> ")) - 1
            if movimiento < 0 or movimiento > 8:
                print("Número inválido. Debe ser entre 1 y 9.")
                continue
        except ValueError:
            print("Entrada inválida. Escribe un número del 1 al 9.")
            continue

        fila = movimiento // 3
        col = movimiento % 3

        if tablero[fila][col] == " ":
            tablero[fila][col] = jugador_actual
        else:
            print("Esa casilla ya está ocupada. Intenta otra vez.")
            continue

        if hay_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Jugador {jugador_actual} gana!")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break

        jugador_actual = "O" if jugador_actual == "X" else "X"

if __name__ == "__main__":
    jugar()