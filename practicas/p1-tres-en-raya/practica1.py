def imprimir_tablero(tablero):
    """Esta función imprime el tablero de juego."""
    print(" " + tablero[0] + " | " + tablero[1] + " | " + tablero[2] + " ")
    print("---|---|---")
    print(" " + tablero[3] + " | " + tablero[4] + " | " + tablero[5] + " ")
    print("---|---|---")
    print(" " + tablero[6] + " | " + tablero[7] + " | " + tablero[8] + " ")

def verificar_ganador(tablero, jugador):
    """Esta función verifica si un jugador ha ganado."""
    lineas_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for linea in lineas_ganadoras:
        if tablero[linea[0]] == jugador and tablero[linea[1]] == jugador and tablero[linea[2]] == jugador:
            return True
    return False

def juego_tres_en_raya():
    """Función principal para ejecutar el juego."""
    tablero = [" "] * 9
    jugador_actual = "X"
    juego_activo = True

    print("¡Bienvenido al Tres en Raya!")
    print("Los jugadores se turnan para elegir una casilla del 1 al 9.")
    print("Puedes presionar 'z' en cualquier momento para salir.")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print("\n¡Que comience el juego!\n")

    while juego_activo:
        imprimir_tablero(tablero)
        print(f"Turno del jugador '{jugador_actual}'.")

        while True:
            
            entrada_usuario = input("Elige una casilla (1-9) o presiona 'z' para salir: ")

            # 1. Verificar si el usuario quiere salir
            if entrada_usuario.lower() == 'z':
                print("¡Juego terminado! Gracias por jugar.")
                juego_activo = False  # Cambia la bandera para salir del bucle principal
                break # Sale del bucle de pedir juzgada

            # 2. Continuar con la lógica normal si no quiere salir
            try:
                movimiento = int(entrada_usuario) - 1
                if 0 <= movimiento <= 8 and tablero[movimiento] == " ":
                    tablero[movimiento] = jugador_actual
                    break # Sale del bucle de pedir jugada porque es válida
                else:
                    print("Movimiento inválido. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número del 1 al 9.")
            
            # --- FIN DE LA MODIFICACIÓN ---

        # Si salimos del bucle porque el usuario presionó 'z', salimos también del bucle principal
        if not juego_activo:
            break

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡Felicidades! El jugador '{jugador_actual}' ha ganado. 🥳")
            juego_activo = False
        elif " " not in tablero:
            imprimir_tablero(tablero)
            print("¡Es un empate! 🤝")
            juego_activo = False
        else:
            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X"

# Iniciar el juego
juego_tres_en_raya()