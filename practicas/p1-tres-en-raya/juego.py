# Juego de 3 en raya para dos jugadores

def mostrar_tablero(tablero):
    print("\n")
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)
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

def tres_en_raya():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0

    print("Bienvenido al juego 3 en raya")
    mostrar_tablero(tablero)

    while True:
        jugador = jugadores[turno % 2]
        print(f"Turno del jugador {jugador}")

        try:
            fila = int(input("Elige fila (0-2): "))
            col = int(input("Elige columna (0-2): "))
        except ValueError:
            print("Entrada inválida. Debes escribir números.")
            continue

        if fila not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Posición fuera de rango. Intenta de nuevo.")
            continue

        if tablero[fila][col] != " ":
            print("Esa posición ya está ocupada. Intenta de nuevo.")
            continue

        tablero[fila][col] = jugador
        mostrar_tablero(tablero)

        if hay_ganador(tablero, jugador):
            print(f"¡El jugador {jugador} gana!")
            break

        if tablero_lleno(tablero):
            print("¡Empate!")
            break

        turno += 1

# Ejecutar el juego
tres_en_raya()
