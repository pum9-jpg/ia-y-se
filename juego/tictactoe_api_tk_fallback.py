import tkinter as tk
from tkinter import messagebox
import requests
import random

# ===== CONFIGURACIÓN =====
API_URL = "https://russianboy29.pythonanywhere.com/api/tictactoe"
API_TIMEOUT = 3  # segundos de espera para la petición

# ===== JUEGO =====
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("3 en Raya 🤖 (API + fallback)")
        self.root.resizable(False, False)
        self.tablero = [" " for _ in range(9)]
        self.jugador_humano = "X"
        self.jugador_api = "O"
        self.turno = self.jugador_humano
        self.botones = []
        self.crear_interfaz()

    def crear_interfaz(self):
        frame = tk.Frame(self.root, bg="#222")
        frame.pack(padx=10, pady=10)

        for i in range(9):
            boton = tk.Button(
                frame,
                text=" ",
                font=("Arial", 28, "bold"),
                width=3,
                height=1,
                bg="#333",
                fg="white",
                command=lambda i=i: self.marcar(i)
            )
            boton.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.botones.append(boton)

        self.label_estado = tk.Label(
            self.root, text="Tu turno (X)", font=("Arial", 14), bg="#222", fg="white"
        )
        self.label_estado.pack(pady=10, fill="x")

        boton_reiniciar = tk.Button(self.root, text="Reiniciar", command=self.reiniciar)
        boton_reiniciar.pack(pady=(0,10))

    # ---- Acciones jugador ----
    def marcar(self, posicion):
        if self.turno != self.jugador_humano:
            return  # evitar clicks fuera de turno
        if self.tablero[posicion] != " ":
            return
        self.tablero[posicion] = self.jugador_humano
        self.botones[posicion].config(text=self.jugador_humano, state="disabled", disabledforeground="#00ffcc")

        if self.hay_ganador(self.jugador_humano):
            self.finalizar_juego("¡Ganaste! 🎉")
            return
        elif self.tablero_lleno():
            self.finalizar_juego("Empate 🤝")
            return

        # Turno de la IA
        self.turno = self.jugador_api
        self.label_estado.config(text="Turno de la IA...")
        # Espera breve para simular "pensamiento" y evitar bloqueos largos
        self.root.after(200, self.movimiento_api)

    # ---- Movimiento IA (API + fallback) ----
    def movimiento_api(self):
        # Primero intenta con la API
        movimiento = self.obtener_movimiento_api(self.tablero, self.jugador_api)

        if movimiento is None:
            print("API no devolvió movimiento válido. Usando IA local (fallback).")
            movimiento = self.movimiento_local(self.tablero, self.jugador_api)
            self.label_estado.config(text="IA (fallback) juega...")
        else:
            self.label_estado.config(text="IA juega...")

        if movimiento is None:
            # sin movimientos (tablero lleno)
            self.turno = self.jugador_humano
            self.label_estado.config(text="Tu turno (X)")
            return

        # aplicar movimiento
        if 0 <= movimiento <= 8 and self.tablero[movimiento] == " ":
            self.tablero[movimiento] = self.jugador_api
            self.botones[movimiento].config(text=self.jugador_api, state="disabled", disabledforeground="#ff6b6b")
        else:
            print("Movimiento final inválido o casilla ocupada (esto no debería pasar).")

        if self.hay_ganador(self.jugador_api):
            self.finalizar_juego("La IA ganó 🤖")
            return
        elif self.tablero_lleno():
            self.finalizar_juego("Empate 🤝")
            return

        self.turno = self.jugador_humano
        self.label_estado.config(text="Tu turno (X)")

    # ---- Llamada a la API (robusta) ----
    def obtener_movimiento_api(self, tablero, jugador):
        try:
            payload = {"board": tablero, "player": jugador}
            resp = requests.post(API_URL, json=payload, timeout=API_TIMEOUT)
            resp.raise_for_status()
            data = resp.json()
            # Intentos de varios formatos comunes
            move = None
            if isinstance(data, dict):
                for key in ("move", "position", "pos", "index"):
                    if key in data:
                        move = data[key]
                        break
            # Si la respuesta es solo un int o string numérico
            if move is None and isinstance(data, (int, str)):
                move = data

            # convertir a int si es posible
            if isinstance(move, str):
                move = move.strip()
                if move.isdigit():
                    move = int(move)
                else:
                    try:
                        move = int(float(move))
                    except:
                        move = None
            if isinstance(move, float):
                move = int(move)

            if isinstance(move, int):
                # aceptar 1-9 (API devuelve 1..9) o 0-8
                if 1 <= move <= 9:
                    move -= 1
                if 0 <= move <= 8:
                    if tablero[move] == " ":
                        print("API devolvió movimiento válido:", move)
                        return move
                    else:
                        print("API devolvió casilla ocupada:", move)
                else:
                    print("API devolvió índice fuera de rango:", move)

            print("Respuesta API no válida o inesperada:", data)
        except requests.exceptions.Timeout:
            print("La petición a la API tardó demasiado y se agotó el timeout.")
        except Exception as e:
            print("Error al conectar con la API:", e)
        return None

    # ---- IA local: minimax (fallback imbatible) ----
    def movimiento_local(self, tablero, jugador):
        # usa minimax para escoger el mejor movimiento
        _, mejor = self.minimax(tablero[:], jugador)
        if mejor is None:
            # fallback aleatorio por si acaso
            disponibles = [i for i,v in enumerate(tablero) if v == " "]
            return random.choice(disponibles) if disponibles else None
        return mejor

    def minimax(self, board, player):
        # returns (score, move)
        if self.hay_ganador_state(board, self.jugador_api):
            return (1, None)
        if self.hay_ganador_state(board, self.jugador_humano):
            return (-1, None)
        if " " not in board:
            return (0, None)

        if player == self.jugador_api:  # maximize
            best_score = -2
            best_move = None
            for i in range(9):
                if board[i] == " ":
                    board[i] = player
                    score, _ = self.minimax(board, self.jugador_humano)
                    board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move
        else:  # minimize
            best_score = 2
            best_move = None
            for i in range(9):
                if board[i] == " ":
                    board[i] = player
                    score, _ = self.minimax(board, self.jugador_api)
                    board[i] = " "
                    if score < best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move

    # ---- Utilidades ----
    def hay_ganador(self, jugador):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        return any(all(self.tablero[i] == jugador for i in c) for c in combos)

    def hay_ganador_state(self, board, jugador):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        return any(all(board[i] == jugador for i in c) for c in combos)

    def tablero_lleno(self):
        return " " not in self.tablero

    def finalizar_juego(self, mensaje):
        self.label_estado.config(text=mensaje)
        for boton in self.botones:
            boton.config(state="disabled")
        messagebox.showinfo("Resultado", mensaje)

    def reiniciar(self):
        self.tablero = [" " for _ in range(9)]
        for boton in self.botones:
            boton.config(text=" ", state="normal")
        self.turno = self.jugador_humano
        self.label_estado.config(text="Tu turno (X)")

# ===== EJECUCIÓN =====
if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="#222")
    app = TicTacToe(root)
    root.mainloop()
