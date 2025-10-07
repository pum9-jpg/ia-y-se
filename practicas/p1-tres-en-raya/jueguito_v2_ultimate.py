import tkinter as tk
from tkinter import messagebox
import openai
import threading
import random

# Configurar cliente IA (usa la API pública LLM7)
client = openai.OpenAI(
    base_url="https://api.llm7.io/v1",
    api_key="unused"  # O consigue una clave gratuita en https://token.llm7.io/
)

class TresEnRayaGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Tres en Raya con IA")
        self.ventana.geometry("500x620")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#f0f0f0')
        
        # Variables del juego
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        self.jugador_actual = 'X'
        self.game_over = False
        self.ganador = None
        
        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = tk.Label(self.ventana, text="TRES EN RAYA (Jugador vs IA)", 
                          font=('Arial', 18, 'bold'), bg='#f0f0f0', fg='#333333')
        titulo.pack(pady=10)

        frame_tablero = tk.Frame(self.ventana, bg='#f0f0f0')
        frame_tablero.pack(pady=20)

        self.botones = []
        for i in range(3):
            fila_botones = []
            for j in range(3):
                boton = tk.Button(frame_tablero, text='', font=('Arial', 20, 'bold'),
                                  width=6, height=3, bg='#ffffff', fg='#333333',
                                  command=lambda fila=i, columna=j: self.hacer_movimiento(fila, columna))
                boton.grid(row=i, column=j, padx=2, pady=2)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

        # Etiqueta de turno
        self.etiqueta_turno = tk.Label(self.ventana, text="Turno: Jugador (X)",
                                       font=('Arial', 14), bg='#f0f0f0', fg='#333333')
        self.etiqueta_turno.pack()

        # Etiqueta de estado de la API
        self.etiqueta_api = tk.Label(self.ventana, text="Estado API: Sin conexión aún",
                                     font=('Arial', 10, 'italic'), bg='#f0f0f0', fg='#666666')
        self.etiqueta_api.pack(pady=(0, 10))

        frame_controles = tk.Frame(self.ventana, bg='#f0f0f0')
        frame_controles.pack(pady=10)

        tk.Button(frame_controles, text="Reiniciar", font=('Arial', 12), bg='#4CAF50', fg='white',
                  command=self.reiniciar_juego).grid(row=0, column=0, padx=10)
        tk.Button(frame_controles, text="Salir", font=('Arial', 12), bg='#f44336', fg='white',
                  command=self.salir_juego).grid(row=0, column=1, padx=10)

    def hacer_movimiento(self, fila, columna):
        if self.game_over or self.tablero[fila][columna] != ' ' or self.jugador_actual != 'X':
            return

        self.tablero[fila][columna] = 'X'
        self.botones[fila][columna].config(text='X', state='disabled', bg='#e0e0e0')
        
        resultado = self.verificar_ganador()
        if resultado:
            self.game_over = True
            self.mostrar_resultado(resultado)
            return

        self.jugador_actual = 'O'
        self.etiqueta_turno.config(text="Turno: IA (O)")
        self.etiqueta_api.config(text="Estado API: Esperando respuesta...", fg='#888888')

        threading.Thread(target=self.turno_ia).start()

    def turno_ia(self):
        tablero_texto = '\n'.join([' '.join(fila) for fila in self.tablero])
        prompt = f"""Eres una IA que juega Tres en Raya. El tablero actual es:

{tablero_texto}

Las posiciones se numeran del 1 al 9 de izquierda a derecha y de arriba a abajo.
Devuelve solo el número de la posición (1-9) donde colocarías tu 'O' para intentar ganar o bloquear al oponente.
Responde solo con un número, sin texto adicional."""

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-nano-2025-04-14",
                messages=[{"role": "user", "content": prompt}]
            )
            respuesta = response.choices[0].message.content.strip()
            # Actualiza estado de API (simulado como éxito)
            self.ventana.after(0, lambda: self.etiqueta_api.config(
                text="Estado API: Código 200 - OK", fg='#2e7d32'))
        except Exception as e:
            respuesta = None
            print("Error al llamar a la IA:", e)
            self.ventana.after(0, lambda: self.etiqueta_api.config(
                text=f"Error de API: {str(e)[:40]}...", fg='#c62828'))

        if respuesta and respuesta.isdigit():
            pos = int(respuesta)
            if 1 <= pos <= 9:
                fila, columna = divmod(pos - 1, 3)
                self.ventana.after(500, lambda: self.movimiento_ia(fila, columna))
            else:
                self.movimiento_aleatorio()
        else:
            self.movimiento_aleatorio()

    def movimiento_aleatorio(self):
        posiciones = [(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == ' ']
        if posiciones:
            fila, columna = random.choice(posiciones)
            self.ventana.after(500, lambda: self.movimiento_ia(fila, columna))
            self.ventana.after(0, lambda: self.etiqueta_api.config(
                text="Estado API: Respuesta inválida, usando jugada aleatoria", fg='#f9a825'))

    def movimiento_ia(self, fila, columna):
        if self.game_over or self.tablero[fila][columna] != ' ':
            return

        self.tablero[fila][columna] = 'O'
        self.botones[fila][columna].config(text='O', state='disabled', bg='#d0e0ff')
        
        resultado = self.verificar_ganador()
        if resultado:
            self.game_over = True
            self.mostrar_resultado(resultado)
        else:
            self.jugador_actual = 'X'
            self.etiqueta_turno.config(text="Turno: Jugador (X)")
            self.etiqueta_api.config(text="Estado API: En espera de nueva jugada", fg='#666666')

    def verificar_ganador(self):
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != ' ':
                return fila[0]
        for c in range(3):
            if self.tablero[0][c] == self.tablero[1][c] == self.tablero[2][c] != ' ':
                return self.tablero[0][c]
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != ' ':
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != ' ':
            return self.tablero[0][2]
        if all(self.tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Empate'
        return None

    def mostrar_resultado(self, resultado):
        if resultado == 'X':
            mensaje = "¡Has ganado! 🎉"
        elif resultado == 'O':
            mensaje = "La IA ha ganado 🤖"
        else:
            mensaje = "¡Es un empate!"
        messagebox.showinfo("Resultado", mensaje)

    def reiniciar_juego(self):
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(text='', state='normal', bg='#ffffff')
        self.game_over = False
        self.jugador_actual = 'X'
        self.etiqueta_turno.config(text="Turno: Jugador (X)")
        self.etiqueta_api.config(text="Estado API: Sin conexión aún", fg='#666666')

    def salir_juego(self):
        if messagebox.askokcancel("Salir", "¿Deseas salir del juego?"):
            self.ventana.quit()

    def iniciar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    juego = TresEnRayaGUI()
    juego.iniciar()
