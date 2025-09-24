import random

class TresEnRaya: 
    def __init__(self): 
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)] 
        self.jugador_actual = 'X' 
        self.game_over = False 
        self.ganador = None 

    def imprimir_tablero(self):
        print("\n   |   |   ")
        for i in range(3):
            print(f" {self.tablero[i][0]} | {self.tablero[i][1]} | {self.tablero[i][2]} ")
            if i < 2:
                print("___|___|___")
            else:
                print("   |   |   ")
        print()

    def movimiento_valido(self, fila, columna):
        return 0 <= fila < 3 and 0 <= columna < 3 and self.tablero[fila][columna] == ' '

    def hacer_movimiento(self, fila, columna, jugador):
        if self.movimiento_valido(fila, columna):
            self.tablero[fila][columna] = jugador
            return True
        return False

    def verificar_ganador(self):
        # Verificar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]
        
        # Verificar columnas
        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != ' ':
                return self.tablero[0][col]
        
        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]
        
        # Verificar empate
        if all(self.tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Empate'
        
        return None

    def movimientos_disponibles(self):
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == ' ':
                    movimientos.append((i, j))
        return movimientos

    def jugar(self):
        print("=== JUEGO DE TRES EN RAYA ===")
        print("Jugador 1: X")
        print("Jugador 2: O")
        print("Para jugar, ingresa fila (0-2) y columna (0-2) separados por espacio")
        print("Ejemplo: '1 2' para la fila 1, columna 2\n")
        
        while not self.game_over:
            self.imprimir_tablero()
            
            jugador_nombre = "Jugador 1 (X)" if self.jugador_actual == 'X' else "Jugador 2 (O)"
            print(f"Turno de {jugador_nombre}")
            
            try:
                entrada = input("Ingresa tu movimiento (fila columna): ").split()
                if len(entrada) != 2:
                    print("Por favor ingresa dos números separados por espacio")
                    continue
                
                fila, columna = int(entrada[0]), int(entrada[1])
                
                if not self.hacer_movimiento(fila, columna, self.jugador_actual):
                    print("Movimiento inválido. Esa celda ya está ocupada o las coordenadas no son válidas.")
                    continue
                
            except ValueError:
                print("Por favor ingresa números válidos (0-2)")
                continue
            except IndexError:
                print("Por favor ingresa números entre 0 y 2")
                continue
            
            # Verificar estado del juego
            resultado = self.verificar_ganador()
            if resultado:
                self.game_over = True
                self.ganador = resultado
                self.imprimir_tablero()
                
                if resultado == 'X':
                    print("¡Felicidades Jugador 1! ¡Has ganado!")
                elif resultado == 'O':
                    print("¡Felicidades Jugador 2! ¡Has ganado!")
                else:
                    print("¡Es un empate!")
                
                break
            
            # Cambiar turno
            self.jugador_actual = 'O' if self.jugador_actual == 'X' else 'X'
        
        # Preguntar si quiere jugar de nuevo
        jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo == 's':
            nuevo_juego = TresEnRaya()
            nuevo_juego.jugar()
        else:
            print("¡Gracias por jugar!")

# Ejecutar
if __name__ == "__main__":
    juego = TresEnRaya()
    juego.jugar()