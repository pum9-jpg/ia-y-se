
class PracticaV1:
    """
    Esta clase contiene toda la lógica y el estado para un juego de Tres en Raya.
    """
    def __init__(self):
        """
        El constructor inicializa el tablero como una matriz 3x3 de espacios vacíos.
        """
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
        self.ganador = None

    def imprimir_tablero(self):
        """Muestra el estado actual del tablero de juego."""
        print("\n--- Tres en Raya ---")
        for fila in self.tablero:
            print(" | ".join(fila))
            print("---------")

    def movimiento_valido(self, fila, columna):
        """Verifica si una casilla está dentro del tablero y está vacía."""
        if 0 <= fila < 3 and 0 <= columna < 3 and self.tablero[fila][columna] == ' ':
            return True
        return False

    def hacer_movimiento(self, fila, columna):
        """Coloca la ficha del jugador actual si el movimiento es válido."""
        if self.movimiento_valido(fila, columna):
            self.tablero[fila][columna] = self.jugador_actual
            return True
        return False

    def cambiar_jugador(self):
        """Cambia el turno al otro jugador."""
        self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'

    def verificar_ganador(self):
        """Verifica todas las condiciones de victoria (filas, columnas, diagonales)."""
        # Verificar filas y columnas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != ' ':
                self.ganador = self.tablero[i][0]
                return self.ganador
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != ' ':
                self.ganador = self.tablero[0][i]
                return self.ganador

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            self.ganador = self.tablero[0][0]
            return self.ganador
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            self.ganador = self.tablero[0][2]
            return self.ganador
            
        return None
    
    def tablero_lleno(self):
        """Verifica si todas las casillas del tablero están ocupadas."""
        for fila in self.tablero:
            if ' ' in fila:
                return False
        return True

    def jugar(self):
        """
        Contiene el bucle principal que controla el flujo de la partida.
        """
        juego_interrumpido = False
        while not self.ganador and not self.tablero_lleno():
            self.imprimir_tablero()
            print(f"Turno del jugador: {self.jugador_actual}")

            try:
                # Pedir la fila y verificar si el usuario quiere salir
                entrada_fila = input("Elige una fila (0, 1, 2) o presiona 'Z' para salir: ")
                if entrada_fila.lower() == 'z':
                    juego_interrumpido = True
                    break

                # Pedir la columna y convertir ambas entradas a números
                entrada_columna = input("Elige una columna (0, 1, 2): ")
                fila = int(entrada_fila)
                columna = int(entrada_columna)

                if self.hacer_movimiento(fila, columna):
                    if self.verificar_ganador():
                        break
                    self.cambiar_jugador()
                else:
                    print("Movimiento inválido. Inténtalo de nuevo.")
            
            except ValueError:
                print("Entrada inválida. Por favor, ingresa solo números.")

        # Lógica para mostrar el mensaje final
        if juego_interrumpido:
            print("\nJuego terminado por el usuario.")
        else:
            self.imprimir_tablero()
            if self.ganador:
                print(f"¡Felicidades! El jugador '{self.ganador}' ha ganado.")
            else:
                print("¡Es un empate!")


# --- Inicio del Programa ---
# Este bloque de código se ejecuta solo cuando corres este archivo directamente.
if __name__ == "__main__":
    juego = PracticaV1()
    juego.jugar()