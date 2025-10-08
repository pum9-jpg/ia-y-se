import tkinter as tk
from tkinter import messagebox

# --- Lógica del juego ---
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

# --- Interfaz gráfica ---
class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("3 en Raya")
        self.jugador_actual = "X"
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.crear_tablero()

    def crear_tablero(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(
                    self.root,
                    text=" ",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    command=lambda f=fila, c=col: self.jugar(f, c)
                )
                boton.grid(row=fila, column=col)
                self.botones[fila][col] = boton

    def jugar(self, fila, col):
        if self.tablero[fila][col] == " ":
            self.tablero[fila][col] = self.jugador_actual
            self.botones[fila][col].config(text=self.jugador_actual)

            if hay_ganador(self.tablero, self.jugador_actual):
                messagebox.showinfo("Fin del juego", f"¡Jugador {self.jugador_actual} gana!")
                self.reiniciar()
                return

            if tablero_lleno(self.tablero):
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.reiniciar()
                return

            # Cambiar turno
            self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def reiniciar(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        for fila in range(3):
            for col in range(3):
                self.botones[fila][col].config(text=" ")
        self.jugador_actual = "X"

# --- Ejecutar ---
if __name__ == "__main__":
    root = tk.Tk()
    juego = TresEnRaya(root)
    root.mainloop()
