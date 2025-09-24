import tkinter as tk
from tkinter import messagebox

class TresEnRaya:
    def __init__(self, root):
        self.root = root
        self.root.title("3 en Raya - 2 Jugadores")

        self.turno = "X"  # X empieza
        self.botones = [[None for _ in range(3)] for _ in range(3)]

        self.crear_interfaz()

    def crear_interfaz(self):
        for fila in range(3):
            for col in range(3):
                boton = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2,
                                  command=lambda f=fila, c=col: self.presionar(f, c))
                boton.grid(row=fila, column=col)
                self.botones[fila][col] = boton

    def presionar(self, fila, col):
        boton = self.botones[fila][col]
        if boton["text"] == "":
            boton["text"] = self.turno
            if self.verificar_ganador():
                messagebox.showinfo("Juego terminado", f"¡Jugador {self.turno} ha ganado!")
                self.reiniciar_juego()
            elif self.empate():
                messagebox.showinfo("Juego terminado", "¡Empate!")
                self.reiniciar_juego()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        # Verifica filas, columnas y diagonales
        for i in range(3):
            if (self.botones[i][0]["text"] == self.botones[i][1]["text"] == self.botones[i][2]["text"] != ""):
                return True
            if (self.botones[0][i]["text"] == self.botones[1][i]["text"] == self.botones[2][i]["text"] != ""):
                return True

        if (self.botones[0][0]["text"] == self.botones[1][1]["text"] == self.botones[2][2]["text"] != ""):
            return True
        if (self.botones[0][2]["text"] == self.botones[1][1]["text"] == self.botones[2][0]["text"] != ""):
            return True

        return False

    def empate(self):
        for fila in self.botones:
            for boton in fila:
                if boton["text"] == "":
                    return False
        return True

    def reiniciar_juego(self):
        for fila in self.botones:
            for boton in fila:
                boton["text"] = ""
        self.turno = "X"

if __name__ == "__main__":
    root = tk.Tk()
    juego = TresEnRaya(root)
    root.mainloop()
