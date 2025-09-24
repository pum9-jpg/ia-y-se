# Juego 3 en raya en consola

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

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

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        
        fila = int(input("Elige fila (0, 1, 2): "))
        col = int(input("Elige columna (0, 1, 2): "))

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

        # Cambiar de jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"

if __name__ == "__main__":
    jugar()
